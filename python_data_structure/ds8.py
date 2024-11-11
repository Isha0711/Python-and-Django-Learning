# List, Tuple, & Set: Given a list of tuples (where each tuple  contains numbers), create a set containing the unique  elements that appear across all the tuples. 
tuple_list = [(1, 2), (2, 3), (4, 5)]
unique = set()
for t in tuple_list:
    unique.update(t)  
print(unique)