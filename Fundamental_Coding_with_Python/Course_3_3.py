
# time = '12:34:56'
def calculatingSeconds(time, seconds):
    time_part = [ int(part) for part in time.split(":")]
    seconds_since_start = time_part[0] * 3600 + time_part[1] * 60 + time_part[2]
    total_seconds = (seconds_since_start + seconds ) % (24*3600)
    hour, reminder = divmod(total_seconds, 3600)
    minutes , seconds = divmod(reminder, 60)
    print(f"{hour} : {minutes} : {seconds}")
    return f"{hour:02d} : {minutes:02d} : {seconds:02d}"

time = '12:34:56'
seconds = 50 
calculatingSeconds(time, seconds)


# Quiz 1
# https://codesignal.com/learn/course/92/unit/3/practice/1
def add_seconds_to_times(timePoints, seconds):
    # TODO: implement the function
    result = []
    for timepoint in timePoints:
        time_temp = [int(time) for time in timepoint.split(":")]
        time_to_seconds = time_temp[0] * 3600+ time_temp[1] * 60 + time_temp[2]
        total_seconds = (time_to_seconds + seconds) % (3600 * 24)
        hours, reminder = divmod(total_seconds, 3600)
        minutes, sec = divmod(reminder, 60)
        hmstime = f"{hours:02d}:{minutes:02d}:{sec:02d}"
        result.append(hmstime)
    print(result)
    return result

add_seconds_to_times(['10:00:00', '23:30:00'], 3600)
# ['11:00:00', '00:30:00']

# Quiz 2
# https://codesignal.com/learn/course/92/unit/3/practice/2
def time_period_length(time_period):
    # TODO: implement the function
    start = time_period.split(" ")[0]
    end = time_period.split(" ")[-1]
    time_p = [start, end]
    res = []
    for time_ in time_p:
        time_part = [int(part) for part in time_.split(":")]
        total_second = time_part[0] * 3600 + time_part[1] * 60 + time_part[0]
        res.append(total_second)
    if res[0] > res[1]:
        res[1] = res[1] + (3600*24)
        new_time_second = res[1] - res[0]
        hours, reminder = divmod(new_time_second, 3600)
        minutes, seconds = divmod(reminder, 60)
    else:
        new_time_second = res[1] - res[0]
        hours, reminder = divmod(new_time_second, 3600)
        minutes, seconds = divmod(reminder, 60)
    print(hours*60+minutes)
    return hours*60+minutes

time_period = "00:00:00 - 23:59:59"
time_period_length(time_period)
# 1439


# Quiz 3
# https://codesignal.com/learn/course/92/unit/3/practice/3

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year):
    return [31,
            29 if is_leap_year(year) else 28,
            31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

def add_days(date, n):
    year, month, day = map(int, date.split("-"))

    while n > 0:
        dim = get_days_in_month(year)
        days_left_in_month = dim[month - 1] - day

        if n <= days_left_in_month:
            day += n
            n = 0
        else:
            n -= (days_left_in_month + 1)
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
    print(f"{year:04d}-{month:02d}-{day:02d}")
    return f"{year:04d}-{month:02d}-{day:02d}"

# '2000-01-01'
add_days('1999-01-01', 365)


from datetime import datetime, timedelta

def add_days(date: str, n: int) -> str:
    # 문자열을 datetime 객체로 변환
    initial_date = datetime.strptime(date, "%Y-%m-%d")
    
    # n일을 더함
    new_date = initial_date + timedelta(days=n)
    
    # 다시 문자열 형식으로 변환
    print(new_date.strftime("%Y-%m-%d"))
    return new_date.strftime("%Y-%m-%d")

# '2000-01-01'
add_days('1999-01-01', 365)


