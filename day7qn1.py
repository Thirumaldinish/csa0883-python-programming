from itertools import permutations

def unique_permutations(nums):
    return list(set(permutations(nums)))

# Test case
nums = [1, 1, 2]
output = unique_permutations(nums)
print(output)
