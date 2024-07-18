def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in input_string if char not in vowels])
    return result

# Sample input
input_string = input("Enter a string: ")

# Remove vowels
string_without_vowels = remove_vowels(input_string)

# Display the result
print(f"The string without vowels is: {string_without_vowels}")
