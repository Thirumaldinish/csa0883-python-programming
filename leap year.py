def is_leap_year(year):
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



def greatest_of_three_numbers(a, b, c):
    """
    Find the greatest of three numbers.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The greatest of the three numbers.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
num1 = 10
num2 = 20
num3 = 15

greatest = greatest_of_three_numbers(num1, num2, num3)
print(f"The greatest of {num1}, {num2}, and {num3} is {greatest}.")
