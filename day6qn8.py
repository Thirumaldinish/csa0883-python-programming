import itertools
input_dict = {1: ['a', 'b'], 2: ['c', 'd']}
lists_of_letters = [letters for key, letters in input_dict.items()]
combinations = list(itertools.product(*lists_of_letters))
formatted_combinations = [''.join(combo) for combo in combinations]
print(','.join(formatted_combinations))
