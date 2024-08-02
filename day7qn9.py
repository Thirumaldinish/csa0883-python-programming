def is_harshad_number(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0

# Test case
number = 18
print(f"{number} is a Harshad number: {is_harshad_number(number)}")
