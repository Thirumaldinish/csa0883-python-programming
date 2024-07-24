def string_operations(str1, str2):
    concatenated = str1 + str2
    reversed_str1 = str1[::-1]
    reversed_str2 = str2[::-1]
    slice_str1 = str1[:5]  
    slice_str2 = str2[:5]  
    
    
    length_str1 = len(str1)
    length_str2 = len(str2)
    
    return {
        "concatenated": concatenated,
        "reversed_str1": reversed_str1,
        "reversed_str2": reversed_str2,
        "slice_str1": slice_str1,
        "slice_str2": slice_str2,
        "length_str1": length_str1,
        "length_str2": length_str2
    }

# Example usage
str1 = "Hello"
str2 = "World"
results = string_operations(str1, str2)

print("Concatenated:", results["concatenated"])
print("Reversed str1:", results["reversed_str1"])
print("Reversed str2:", results["reversed_str2"])
print("Slice str1:", results["slice_str1"])
print("Slice str2:", results["slice_str2"])
print("Length of str1:", results["length_str1"])
print("Length of str2:", results["length_str2"])
