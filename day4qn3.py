def is_substring(sub, main):
    return sub in main

# Example usage
main_string = "Hello, welcome to the world of Python."
substring = "welcome"
result = is_substring(substring, main_string)

if result:
    print(f"'{substring}' is a substring of '{main_string}'")
else:
    print(f"'{substring}' is not a substring of '{main_string}'")
