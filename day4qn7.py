def is_armstrong_number(n):
    
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n


number = 153
result = is_armstrong_number(number)

if result:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
