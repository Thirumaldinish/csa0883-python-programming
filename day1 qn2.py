def create_list_of_tuples(lower, upper):
    return [(num, num ** 2) for num in range(lower, upper + 1)]
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
result = create_list_of_tuples(lower_range, upper_range)
print("List of tuples:", result)
