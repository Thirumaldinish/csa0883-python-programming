def are_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if (char_s in mapping_s_to_t and mapping_s_to_t[char_s] != char_t) or \
           (char_t in mapping_t_to_s and mapping_t_to_s[char_t] != char_s):
            return False
        mapping_s_to_t[char_s] = char_t
        mapping_t_to_s[char_t] = char_s
    
    return True

# Sample input
s = "egg"
t = "add"

# Check if the strings are isomorphic
result = are_isomorphic(s, t)
print(result)  # Output: True
