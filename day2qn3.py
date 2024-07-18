def count_lines_and_words(paragraph):
    # Split the paragraph into lines
    lines = paragraph.strip().split('\n')
    number_of_lines = len(lines)
    
    print(f"Number of lines: {number_of_lines}")
    print("Number of words in each line:")
    
    for i, line in enumerate(lines):
        # Split each line into words
        words = line.split()
        number_of_words = len(words)
        print(f"Line {i + 1}: {number_of_words}")

# Sample input
paragraph = '''This is the most straightforward way to count the number 
of lines in a text file in Python. The readlines() method reads 
all 
lines from a file and stores it in a list. Next, use the len() 
function 
to find the length of the list which is nothing but total lines 
present in a file.'''

count_lines_and_words(paragraph)
