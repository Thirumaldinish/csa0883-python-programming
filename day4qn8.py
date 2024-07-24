def is_tech_number(n):
    str_num = str(n)
    length = len(str_num)
    if length % 2 != 0:
        return False
    first_half = int(str_num[:length//2])
    second_half = int(str_num[length//2:])
    return (first_half + second_half) ** 2 == n

# Example usage
number = 2025
result = is_tech_number(number)

if result:
    print(f"{number} is a Tech number.")
else:
    print(f"{number} is not a Tech number.")
