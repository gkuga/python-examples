import polars as pl


def main() -> None:
    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
            "team": ["red", "blue", "red", "blue", "red"],
            "score": [85, 72, 93, 64, 78],
        }
    )
    print("DataFrame:")
    print(df)

    # Expressions: select columns and derive new ones
    print("\nselect + with_columns:")
    print(
        df.select("name", "score").with_columns(
            (pl.col("score") >= 80).alias("passed"),
        )
    )

    # Filter rows
    print("\nfilter (score > 75):")
    print(df.filter(pl.col("score") > 75))

    # Aggregate per group
    print("\ngroup_by team:")
    print(
        df.group_by("team")
        .agg(
            pl.len().alias("members"),
            pl.col("score").mean().alias("avg_score"),
            pl.col("score").max().alias("max_score"),
        )
        .sort("team")
    )

    # Lazy API: build a query plan and execute it with collect()
    lazy = (
        df.lazy()
        .filter(pl.col("team") == "red")
        .sort("score", descending=True)
        .select("name", "score")
    )
    print("\nlazy query plan:")
    print(lazy.explain())
    print("\nlazy result:")
    print(lazy.collect())


if __name__ == "__main__":
    main()
