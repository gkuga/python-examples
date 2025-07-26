from datetime import datetime, timezone, timedelta

# Naive datetime (タイムゾーン情報なし)
naive_dt = datetime.now()
print("Naive datetime:", naive_dt)
print("Naive is aware?", naive_dt.tzinfo is not None and naive_dt.tzinfo.utcoffset(naive_dt) is not None)

# Aware datetime (タイムゾーン付き: UTC)
aware_dt_utc = datetime.now(timezone.utc)
print("\nAware datetime (UTC):", aware_dt_utc)
print("Aware is aware?", aware_dt_utc.tzinfo is not None and aware_dt_utc.tzinfo.utcoffset(aware_dt_utc) is not None)

# Aware datetime with custom timezone (e.g., JST +09:00)
jst = timezone(timedelta(hours=9))
aware_dt_jst = datetime.now(jst)
print("\nAware datetime (JST):", aware_dt_jst)
print("JST Offset:", aware_dt_jst.utcoffset())
