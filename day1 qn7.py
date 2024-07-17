def find_mth_maximum(array, m):
    sorted_array = sorted(array, reverse=True)
    return sorted_array[m-1] if m <= len(sorted_array) else None

def find_nth_minimum(array, n):
    sorted_array = sorted(array)
    return sorted_array[n-1] if n <= len(sorted_array) else None

def calculate_results(mth_max, nth_min):
    if mth_max is not None and nth_min is not None:
        sum_result = mth_max + nth_min
        diff_result = mth_max - nth_min
        prod_result = mth_max * nth_min
        return sum_result, diff_result, prod_result
    return None, None, None

# Sample Input
array = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

# Find Mth maximum and Nth minimum
mth_max = find_mth_maximum(array, M)
nth_min = find_nth_minimum(array, N)

# Calculate sum, difference, and product
sum_result, diff_result, prod_result = calculate_results(mth_max, nth_min)

# Print results
print(f"Mth maximum (M={M}): {mth_max}")
print(f"Nth minimum (N={N}): {nth_min}")
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
