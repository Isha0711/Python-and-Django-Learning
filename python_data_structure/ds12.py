# List & Dictionary: Write a Python program to group a  list of words by their starting letter into a dictionary, where  the key is the starting letter and the value is a list of words. 
words = ["apple", "banana", "orange", "cashew", "dates"]
grouped = {}
for x in words:
    first = x[0]
    grouped.setdefault(first, []).append(x)  
print(grouped)