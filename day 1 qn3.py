def is_composite(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return True
        i += 6
    return False

def count_composite_numbers(array):
    count = 0
    for num in array:
        if is_composite(num):
            count += 1
    return count
array = [16, 18, 27, 16, 23, 21, 19]
composite_count = count_composite_numbers(array)

print("Number of composite numbers in the array:", composite_count)
