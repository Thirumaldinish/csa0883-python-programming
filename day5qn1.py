def is_leap_year(year):
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    return False
n = int(input("Enter the year: "))
if is_leap_year(n):
    print("Leap year")
else:
    print("Not a leap year")
