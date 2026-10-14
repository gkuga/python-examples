from datetime import datetime

import polars as pl


def make_sample() -> pl.DataFrame:
    """Air conditioner ON/OFF samples (start_stop: 1=ON, 0=OFF, null=missing).

    Rows are intentionally shuffled to show that normalization sorts them.
    """
    t = lambda h, m: datetime(2026, 10, 14, h, m)  # noqa: E731
    rows = [
        # zone A / ac-1: ON 9:00-9:30, ON again 10:00 until the end (no OFF yet)
        ("A", "ac-1", t(9, 0), 1),
        ("A", "ac-1", t(9, 10), None),  # missing -> forward filled to 1
        ("A", "ac-1", t(9, 20), 1),
        ("A", "ac-1", t(9, 30), 0),
        ("A", "ac-1", t(9, 40), None),  # missing -> forward filled to 0
        ("A", "ac-1", t(10, 0), 1),
        ("A", "ac-1", t(10, 10), 1),
        # zone A / ac-2: starts OFF, ON 9:20-9:40
        ("A", "ac-2", t(9, 0), 0),
        ("A", "ac-2", t(9, 20), 1),
        ("A", "ac-2", t(9, 40), 0),
        # zone B / ac-3: leading null stays null, then ON 9:10-9:20
        ("B", "ac-3", t(9, 0), None),
        ("B", "ac-3", t(9, 10), 1),
        ("B", "ac-3", t(9, 20), 0),
        # zone B / ac-4: ON, then no data for 110 minutes while still ON, OFF at 11:10
        ("B", "ac-4", t(9, 0), 1),
        ("B", "ac-4", t(9, 10), 1),
        ("B", "ac-4", t(11, 0), 1),
        ("B", "ac-4", t(11, 10), 0),
    ]
    df = pl.DataFrame(
        rows,
        schema={
            "zone_id": pl.String,
            "air_conditioner_id": pl.String,
            "measured_at": pl.Datetime,
            "start_stop": pl.Int8,
        },
        orient="row",
    )
    return df.sample(fraction=1.0, shuffle=True, seed=0)


class AcRunAnalyzer:
    def __normalize_start_stop(self, df: pl.DataFrame) -> pl.DataFrame:
        if df.is_empty():
            return df
        # Fill in missing data.
        return (
            df.sort(["air_conditioner_id", "measured_at"])
            .with_columns(pl.col("start_stop").fill_null(strategy="forward").over("air_conditioner_id"))
        )

    def ranges_by_state_change(self, df_ac_mode_past: pl.DataFrame) -> pl.DataFrame:
        """A range is a run of consecutive ON rows; it ends at the next record (OFF)."""
        df = self.__normalize_start_stop(df_ac_mode_past)  # already sorted
        keys = ["zone_id", "air_conditioner_id"]
        ranges = (
            df.with_columns(
                prev=pl.col("start_stop").shift(1).over(keys),
                next_t=pl.col("measured_at").shift(-1).over(keys),
            )
            # A new run starts whenever the state differs from the previous row
            .with_columns(run_id=((pl.col("start_stop") != pl.col("prev")).fill_null(True)).cum_sum().over(keys))
            .filter(pl.col("start_stop") == 1)
            .group_by(keys + ["run_id"])
            .agg(
                start=pl.col("measured_at").min(),
                end=pl.col("next_t").last(),  # row after the last ON row = OFF time (null if none)
            )
            .drop("run_id")
        )
        # group_by does not guarantee output order
        return ranges.sort(keys + ["start"])

    def ranges_by_time_gap(self, df_ac_mode_past: pl.DataFrame) -> pl.DataFrame:
        """A range is a group of ON rows with no gap longer than 60 minutes."""
        df_normalized = self.__normalize_start_stop(df_ac_mode_past)

        df_running = (
            df_normalized.filter(pl.col("start_stop") == 1)
            .sort(["zone_id", "air_conditioner_id", "measured_at"])
        )
        df_session = df_running.with_columns(
            # Calculate the difference from the previous `measured_at` value for each `air_conditioner_id` and `zone_id`
            time_diff=pl.col("measured_at").diff().over(["air_conditioner_id", "zone_id"])
        ).with_columns(
            # If more than 60 minutes have passed since the previous data, set a new session flag (1).
            is_new_session=(
                (pl.col("time_diff") > pl.duration(minutes=60)) | pl.col("time_diff").is_null()
            )
        ).with_columns(
            # Generate a session ID by calculating the cumulative sum of the flags
            session_id=pl.col("is_new_session").cum_sum().over(["air_conditioner_id", "zone_id"])
        )

        # Get the start and end datetimes by grouping
        ranges = (
            df_session.group_by(["air_conditioner_id", "zone_id", "session_id"])
            .agg([
                pl.col("measured_at").min().alias("start"),
                pl.col("measured_at").max().alias("end"),
                pl.len().alias("record_count"),   # Number of records in a session
            ])
            .drop("session_id")   # Remove Unnecessary Session IDs
            .sort(["air_conditioner_id", "zone_id", "start"])
        )

        return ranges

    def ranges_per_record(self, df_ac_mode_past: pl.DataFrame) -> pl.DataFrame:
        """Every ON row becomes its own range, ending at the next record (no merging)."""
        ranges = (
            self.__normalize_start_stop(df_ac_mode_past)
            .with_columns(
                end=pl.col("measured_at")
                .shift(-1)
                .over(["zone_id", "air_conditioner_id"])
            )
            .filter(pl.col("start_stop") == 1)
            .select(
                "zone_id",
                "air_conditioner_id",
                start=pl.col("measured_at"),
                end=pl.col("end"),
            )
        )
        return ranges


def main() -> None:
    pl.Config.set_tbl_rows(30)
    df = make_sample()
    print("input (sorted for readability):")
    print(df.sort(["air_conditioner_id", "measured_at"]))

    analyzer = AcRunAnalyzer()

    print("\n[1] by state change (ON -> OFF):")
    print(analyzer.ranges_by_state_change(df))

    print("\n[2] by time gap (> 60 min):")
    print(analyzer.ranges_by_time_gap(df))

    print("\n[3] per record (no merging):")
    print(analyzer.ranges_per_record(df))


if __name__ == "__main__":
    main()
