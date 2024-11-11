# Dictionary & Tuple: Given a dictionary, return a sorted list  of tuples where each tuple is a key-value pair from the  dictionary, sorted by the dictionary’s values. 
dict = {'a': 3, 'b': 1, 'c': 2}
sorted = sorted(dict.items(), key=lambda item: item[1]) 
print(sorted)