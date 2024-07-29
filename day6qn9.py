import datetime

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    day_of_week_index = date.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[(day_of_week_index + 1) % 7]
day = 31
month = 8
year = 2019
print(get_day_of_week(day, month, year))
