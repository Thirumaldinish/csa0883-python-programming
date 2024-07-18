str = input("Enter the string: ")
char = input("Enter the character to be searched: ")

index = -1
for i, c in enumerate(str):
    if c == char:
        index = i
        break

if index!= -1:
    print(f"{char} is found in string at index: {index}")
else:
    print(f"{char} is not found in string")
