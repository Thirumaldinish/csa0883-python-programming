def nth_largest_number(lst, N):
    if N > len(lst) or N <= 0:
        return "N is out of the valid range."
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[N - 1]
lst = [14, 67, 48, 23, 5, 62]
N = 4
result = nth_largest_number(lst, N)
print(f"{N}th Largest number: {result}")
