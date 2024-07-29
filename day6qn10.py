def find_first_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            right = mid - 1
    return -1

def find_last_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            left = mid + 1
    return -1

def search_range(nums, target):
    start = find_first_position(nums, target)
    if start == -1:
        return [-1, -1]
    end = find_last_position(nums, target)
    return [start, end]
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(nums, target)
print(result)
