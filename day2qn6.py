def sort_word(word):
    # Convert the word to a list of characters
    char_list = list(word)
    
    # Sort the list of characters in normal order
    char_list_sorted_normal = sorted(char_list)
    
    # Sort the list of characters in reverse order
    char_list_sorted_reverse = sorted(char_list, reverse=True)
    
    # Convert the sorted lists back to strings with spaces between characters
    normal_order = ' '.join(char_list_sorted_normal)
    reverse_order = ' '.join(char_list_sorted_reverse)
    
    return normal_order, reverse_order

# Sample input
word = input("Enter the word: ")

normal_order, reverse_order = sort_word(word)
print(f"Alphabetical Order Normal: {normal_order}")
print(f"Alphabetical Order Reverse: {reverse_order}")
