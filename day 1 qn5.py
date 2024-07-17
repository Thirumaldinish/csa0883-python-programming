def count_negative_numbers(lst):
    return len([num for num in lst if num < 0])

# Sample Input
lst = [16, -18, 27, -16, 23, -21, 19]

# Get the number of negative numbers in the list
negative_count = count_negative_numbers(lst)

print("Number of negative numbers in the list:", negative_count)
