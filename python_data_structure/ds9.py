# Set & Dictionary: Write a Python program that checks if a dictionary has all unique values using a set. 
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
unique = set(dict.values())
all_unique = len(unique) == len(dict) 
print(all_unique)