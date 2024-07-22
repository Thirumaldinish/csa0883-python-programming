def count_occurrences(numbers, target):
    """Function to count the number of occurrences of the target number in the tuple."""
    count = numbers.count(target)
    return count


numbers = (3, 6, 8, 9, 8, 9, 12, 35, 8)
target_number = 8


occurrences = count_occurrences(numbers, target_number)


print(f"The number {target_number} occurs {occurrences} times in the tuple.")
