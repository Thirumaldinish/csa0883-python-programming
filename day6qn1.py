
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
def perfect_squares_in_range(lower, upper):
    perfect_squares = []
    for num in range(lower, upper + 1):
        if (num ** 0.5).is_integer() and sum_of_digits(num) < 10:
            perfect_squares.append(num)
    return perfect_squares
lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))
result = perfect_squares_in_range(lower_range, upper_range)
print(result)
