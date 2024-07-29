
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_prime_numbers(arr):
    return [num for num in arr if is_prime(num)]
arr = [26, 28, 47, 26, 43, 51, 29]
prime_numbers = find_prime_numbers(arr)
print("Prime numbers in Array elements =", prime_numbers)
