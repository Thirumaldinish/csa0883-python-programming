def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def print_fibonacci_sequence(n):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input
n = int(input("Enter the value of N: "))

# Find the Nth Fibonacci number
nth_fibonacci = fibonacci(n)
print(f"The {n}th Fibonacci number is: {nth_fibonacci}")

# Print the Fibonacci sequence up to the Nth number
sequence = print_fibonacci_sequence(n)
print("Fibonacci sequence up to the Nth number:")
print(" ".join(map(str, sequence)))
