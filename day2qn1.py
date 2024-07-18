def count_vowels_and_consonants(statement):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0

    for char in statement:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    print(f"Number of vowels = {num_vowels}")
    print(f"Number of consonants = {num_consonants}")

    if num_vowels > num_consonants:
        print("Vowels are more.")
    elif num_consonants > num_vowels:
        print("Consonants are more.")
    else:
        print("Vowels and consonants are equal.")

# Sample input
statement = "Saveetha School of Engineering"
count_vowels_and_consonants(statement)
