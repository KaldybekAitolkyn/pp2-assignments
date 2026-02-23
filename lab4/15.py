from datetime import datetime, timedelta, timezone

def is_leap(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def parse_line(s: str) -> datetime:
    date_part, tz_part = s.strip().split()
    y, m, d = map(int, date_part.split("-"))

    sign = 1 if tz_part[3] == "+" else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    tz = timezone(sign * timedelta(hours=hh, minutes=mm))

    return datetime(y, m, d, 0, 0, 0, tzinfo=tz)

def birthday_in_year(year: int, bm: int, bd: int, btz) -> datetime:
    if bm == 2 and bd == 29 and not is_leap(year):
        bd = 28
    return datetime(year, bm, bd, 0, 0, 0, tzinfo=btz)

birth_dt = parse_line(input())
cur_dt = parse_line(input())

bm, bd = birth_dt.month, birth_dt.day
btz = birth_dt.tzinfo

cur_utc = cur_dt.astimezone(timezone.utc)

cand = birthday_in_year(cur_dt.year, bm, bd, btz)
cand_utc = cand.astimezone(timezone.utc)

if cand_utc < cur_utc:
    cand = birthday_in_year(cur_dt.year + 1, bm, bd, btz)
    cand_utc = cand.astimezone(timezone.utc)

diff_sec = int((cand_utc - cur_utc).total_seconds())

if diff_sec <= 0:
    print(0)
else:
    print((diff_sec + 86400 - 1) // 86400)