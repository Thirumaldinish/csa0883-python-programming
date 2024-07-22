
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
element_to_search = 3
concatenated_tuple = tuple1 + tuple2
try:
    index_of_element = concatenated_tuple.index(element_to_search)
except ValueError:
    index_of_element = -1


count_of_element = concatenated_tuple.count(element_to_search)
print("Concatenated Tuple:", concatenated_tuple)
print(f"Index of element {element_to_search}:", index_of_element)
print(f"Count of element {element_to_search}:", count_of_element)
