# polars ac_runs

Turn air conditioner ON/OFF time series (`start_stop`: 1=ON, 0=OFF) into
running ranges (`start`, `end`) per `zone_id` / `air_conditioner_id`, and
compare two ways of doing it.

Both first sort and forward-fill missing `start_stop` per air conditioner.

1. `ranges_by_state_change`: `(state != prev).cum_sum().over(keys)` gives each
   consecutive run of the same state an id. A range is a run of ON rows;
   `end` is the time of the next record (the OFF), or null if still running.
2. `ranges_by_time_gap`: keep only ON rows, start a new session when the gap
   from the previous ON row exceeds 60 minutes. `end` is the last ON record.
3. `ranges_per_record`: no merging. Every ON row becomes a range ending at the
   next record, so the output has as many rows as there are ON records.

The two differ when OFF lasts less than 60 minutes (2 merges it into one
session), when data is missing for more than 60 minutes while ON (2 splits
it), and in what `end` means (OFF time vs. last ON measurement).

```sh
uv run main.py
uv run bench.py  # peak memory and output size on 300 ACs x 30 days of 1-minute data
```

On that data, peak memory while computing is about the same (~1GB) for all
three, but 3 returns ~6.5M rows (~150MB) vs. ~50K rows (~1MB) for 1 and 2,
and that result stays in memory for whatever runs next.
