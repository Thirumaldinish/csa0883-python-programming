def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def non_prime_numbers(A, B):
    non_primes = [num for num in range(A, B + 1) if not is_prime(num)]
    return non_primes

# Test case
A, B = 12, 19
output = non_prime_numbers(A, B)
print(output)
