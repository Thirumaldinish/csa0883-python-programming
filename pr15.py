def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Input
n = 3

# Print the pattern
print_pattern(n)
