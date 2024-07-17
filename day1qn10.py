def sumsquare(l):
    odd_sum = sum(x**2 for x in l if x % 2 != 0)
    even_sum = sum(x**2 for x in l if x % 2 == 0)
    return [odd_sum, even_sum]

# Sample Input
num_elements = int(input("Enter the number of elements: "))
l = [int(input("Enter the element: ")) for _ in range(num_elements)]

# Calculate the sum of squares of odd and even numbers
result = sumsquare(l)

print("Sum of squares of odd numbers:", result[0])
print("Sum of squares of even numbers:", result[1])
