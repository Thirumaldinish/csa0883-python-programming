def calculate_averages():
    positive_numbers = []
    negative_numbers = []

    while True:
        try:
            num = float(input("Enter the number (-1 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if num == -1:
            break
        elif num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)

    if positive_numbers:
        avg_positive = sum(positive_numbers) / len(positive_numbers)
    else:
        avg_positive = 0

    if negative_numbers:
        avg_negative = sum(negative_numbers) / len(negative_numbers)
    else:
        avg_negative = 0

    print(f"Average of positive numbers: {avg_positive:.2f}")
    print(f"Average of negative numbers: {avg_negative:.2f}")

# Call the function to start the process
calculate_averages()
