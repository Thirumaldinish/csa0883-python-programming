def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Test cases
test_cases = ["SIGN UP", "AT-LEAST", "1245", "!@#$%", "145*999=144855"]
for test in test_cases:
    print(f"Original: {test} | Reversed: {reverse_string(test)}")
