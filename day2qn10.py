def reverse_number(number):
    return number[::-1]

def is_mirror(number):
    return number == reverse_number(number)

# Sample input
number = input("Enter the number: ")

# Reverse the number
reversed_number = reverse_number(number)

print(f"Mirror image: {reversed_number}")

if is_mirror(number):
    print("The number is a mirror number.")
else:
    print("The number is not a mirror number.")
