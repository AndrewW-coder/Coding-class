def leapyear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def cal_days(month, day, year):
    days_in_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][leapyear(year)] 
    days = 0
    for i in range(month - 1):
        days += days_in_month[i]
    days += day
    print(days)
    return days
cal_days(12, 31, 2021)

