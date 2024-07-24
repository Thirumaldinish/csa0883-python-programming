def is_perfect_number(n):
    
    if n <= 0:
        return False
    
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == n

# Example usage
number = 28
result = is_perfect_number(number)

if result:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
