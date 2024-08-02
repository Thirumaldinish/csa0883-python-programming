def is_composite(n):
    if n < 4:
        return False  # 0, 1, 2, 3 are not composite
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test case
number = 12
print(f"{number} is a composite number: {is_composite(number)}")
