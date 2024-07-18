def count_matching_characters(s1, s2):
    # Determine the length of the shorter string
    min_length = min(len(s1), len(s2))
    match_count = 0

    # Compare characters at the same index in both strings
    for i in range(min_length):
        if s1[i] == s2[i]:
            match_count += 1

    return match_count

# Sample input
s1 = "what"
s2 = "watch"
matches = count_matching_characters(s1, s2)
print(matches)
