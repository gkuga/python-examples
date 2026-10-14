"""Measure peak memory (RSS) and output size of each method on large synthetic data.

Each method runs in its own process so peak RSS is not shared between them.

    uv run bench.py
"""
import resource
import subprocess
import sys
import time
from datetime import datetime

import numpy as np
import polars as pl

from main import AcRunAnalyzer

N_AC = 300
DAYS = 30
FREQ_MIN = 1


def make_large() -> pl.DataFrame:
    rng = np.random.default_rng(0)
    n = DAYS * 24 * 60 // FREQ_MIN
    ts = (np.datetime64("2026-09-01T00:00") + np.arange(n) * np.timedelta64(FREQ_MIN, "m")).astype("datetime64[us]")
    frames = []
    for i in range(N_AC):
        # Flip state rarely (about every 2 hours) so runs are long
        flips = rng.random(n) < FREQ_MIN / 120
        state = (np.cumsum(flips) % 2).astype(np.int8)
        frames.append(
            pl.DataFrame(
                {
                    "zone_id": f"z{i // 10}",
                    "air_conditioner_id": f"ac-{i}",
                    "measured_at": ts,
                    "start_stop": state,
                }
            )
        )
    return pl.concat(frames)


def max_rss_mb() -> float:
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # bytes on macOS, KiB on Linux
    return rss / 1024 / 1024 if sys.platform == "darwin" else rss / 1024


def run_one(method: str) -> None:
    df = make_large()
    base = max_rss_mb()
    t0 = time.perf_counter()
    out = getattr(AcRunAnalyzer(), method)(df)
    elapsed = time.perf_counter() - t0
    print(
        f"{method:24s} rows={out.height:>10,} size={out.estimated_size('mb'):8.1f}MB "
        f"peak+={max_rss_mb() - base:8.1f}MB time={elapsed:6.2f}s"
    )


def main() -> None:
    if len(sys.argv) > 1:
        run_one(sys.argv[1])
        return
    df = make_large()
    print(f"input rows={df.height:,} size={df.estimated_size('mb'):.1f}MB "
          f"({N_AC} ACs x {DAYS} days, every {FREQ_MIN} min)", flush=True)
    for m in ["ranges_by_state_change", "ranges_by_time_gap", "ranges_per_record"]:
        subprocess.run([sys.executable, __file__, m], check=True)


if __name__ == "__main__":
    main()
