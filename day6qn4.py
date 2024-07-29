
def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False
def count_composite_numbers(arr):
    count = 0
    for num in arr:
        if is_composite(num):
            count += 1
    return count
arr = [16, 18, 27, 16, 23, 21, 19]
result = count_composite_numbers(arr)
print(f"Number of Composite Numbers = {result}")
