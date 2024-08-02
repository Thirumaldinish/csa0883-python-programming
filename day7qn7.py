def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def anniversary_check():
    date_input = input("Enter Date (DD/MM/YYYY): ")
    day, month, year = map(int, date_input.split('/'))
    
    if is_leap_year(year):
        print(f"Given Anniversary Year: Leap Year. Next Anniversary Date: {day}/{month}/{year + 4}")
    else:
        print(f"Given Anniversary Year: Non Leap Year. Anniversary Date: {day}/{month}/{year - 1}")

anniversary_check()
