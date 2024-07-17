def remove_duplicates_and_sort(array):
    num_count = {}
    for num in array:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    unique_numbers = [num for num in num_count if num_count[num] == 1]
    unique_numbers.sort()
    
    return unique_numbers


array = [15, 14, 25, 14, 32, 14, 31]
sorted_array = remove_duplicates_and_sort(array)

print("Sorted Array =", sorted_array)
