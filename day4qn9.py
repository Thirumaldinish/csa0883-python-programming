def is_prime_number(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Example usage
number = 29
result = is_prime_number(number)

if result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
