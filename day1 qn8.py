def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Sample Input
nums = [1, 2, 3, 1]

# Find the peak element index
peak_index = find_peak_element(nums)

print("Peak element index:", peak_index)
