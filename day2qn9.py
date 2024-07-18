def remove_common_words(s1, s2):
    # Convert sentences to sets of words
    set1 = set(s1.split())
    set2 = set(s2.split())

    # Find common words
    common_words = set1.intersection(set2)

    # Remove common words from both sentences
    s1_result = ' '.join([word for word in s1.split() if word not in common_words])
    s2_result = ' '.join([word for word in s2.split() if word not in common_words])

    return s1_result, s2_result

# Sample input
s1 = "sky is blue in color"
s2 = "Raj likes sky blue color"

# Remove common words and print results
s1_result, s2_result = remove_common_words(s1, s2)
print(s1_result)
print(s2_result)
