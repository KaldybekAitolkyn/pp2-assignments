from datetime import datetime, timedelta, timezone

def parse_dt(s: str) -> datetime:
    parts = s.strip().split()
    date_part, time_part, tz_part = parts[0], parts[1], parts[2]

    y, m, d = map(int, date_part.split("-"))
    hh, mm, ss = map(int, time_part.split(":"))

    sign = 1 if tz_part[3] == "+" else -1
    off_h, off_m = map(int, tz_part[4:].split(":"))
    tz = timezone(sign * timedelta(hours=off_h, minutes=off_m))

    return datetime(y, m, d, hh, mm, ss, tzinfo=tz)

start = parse_dt(input())
end = parse_dt(input())

start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

print(int((end_utc - start_utc).total_seconds()))