from datetime import datetime, timedelta, timezone

def parse_moment(s: str) -> datetime:
    date_part, tz_part = s.strip().split()
    y, m, d = map(int, date_part.split("-"))

    sign = 1 if tz_part[3] == "+" else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timezone(sign * timedelta(hours=hh, minutes=mm))

    return datetime(y, m, d, 0, 0, 0, tzinfo=offset)

a = parse_moment(input())
b = parse_moment(input())

diff_seconds = abs((a.astimezone(timezone.utc) - b.astimezone(timezone.utc)).total_seconds())
print(int(diff_seconds // 86400))