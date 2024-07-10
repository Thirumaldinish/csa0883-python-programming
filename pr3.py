# Initialize two variables
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
even_numbers = []

for num in numbers:
    if num == 20:
        break
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers before 20:", even_numbers)
