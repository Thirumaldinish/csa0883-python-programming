def count_words(s):
    words = s.split()
    return len(words)
input_string = "Hello, welcome to the world of Python."
word_count = count_words(input_string)

print(f"The number of words in the string is: {word_count}")
