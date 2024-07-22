def find_maximum(a, b, c):
    """Function to find the maximum of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = 6
num2 = 9
num3 = 56
maximum_number = find_maximum(num1, num2, num3)
print("The maximum of the three numbers is:", maximum_number)
