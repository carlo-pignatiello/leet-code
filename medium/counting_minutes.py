from datetime import datetime

def counting_minutes(s: str) -> int:
    splitted_time = s.split('-')
    start, end = splitted_time[0], splitted_time[1]
    parsed_start = parse_time(start)
    parsed_end = parse_time(end)
    s = datetime.strptime(parsed_start, "%H:%M:%S")
    e = datetime.strptime(parsed_end, "%H:%M:%S")
    if s < e:
        return (e - s).seconds // 60
    return 24 * 60 - (s - e).seconds // 60

def parse_time(s: str):
    if s[-2:] == "pm":
        new_h = int(s[:-2].split(":")[0]) + 12
        return str(new_h if new_h != 24 else 0) + ":" + s[:-2].split(":")[1] + ":00"
    return s[:-2] + ":00"


print(counting_minutes("12:30pm-12:00am"))
print(counting_minutes("1:23am-1:08am"))