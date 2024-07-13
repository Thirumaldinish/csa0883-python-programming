def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_non_primes(A, B):
    non_primes = []
    for num in range(A, B + 1):
        if not is_prime(num):
            non_primes.append(num)
    return non_primes

# Sample Input
A = 12
B = 19

# Find and print non-prime numbers between A and B
non_primes = find_non_primes(A, B)
print("Non-prime numbers between", A, "and", B, "are:", ", ".join(map(str, non_primes)))
