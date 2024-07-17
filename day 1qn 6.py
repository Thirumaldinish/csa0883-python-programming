def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_non_composite_numbers(array):
    return [num for num in array if is_prime(num) or num == 1]

# Sample Input
array = [26, 28, 47, 26, 43, 51, 29]

# Get the non-composite numbers in the array
non_composite_numbers = find_non_composite_numbers(array)

print("Non-composite numbers in the arra
