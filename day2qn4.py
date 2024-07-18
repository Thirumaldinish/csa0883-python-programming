def count_sentences_starting_with_b(paragraph):
    # Split the paragraph into sentences using '.'
    sentences = paragraph.split('.')
    
    # Remove leading and trailing whitespaces from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Count the number of sentences starting with 'B'
    count = sum(1 for sentence in sentences if sentence.startswith('B'))

    return count

# Sample input
paragraph = '''The apple doesn't fall. ...
All that glitters are not gold. ...
A picture is worth a thousand words. ...
Beggars can't be choosers. ...
A bird in the hand. ...
Better safe than sorry. ...
An apple a day keeps doctor away. ...
Blood is thicker than water. ...'''

result = count_sentences_starting_with_b(paragraph)
print(f"Number of sentences that start with 'B': {result}")
