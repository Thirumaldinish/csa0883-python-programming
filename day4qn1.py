def find_duplicates(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

# Example usage
example_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 3]
duplicates = find_duplicates(example_list)
print("Duplicate elements:", duplicates)
