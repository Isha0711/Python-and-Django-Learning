# Set & List: Write a Python program that removes all  elements from a list that appear more than once, preserving  the original order. 
l = [1, 2, 2, 3, 4, 4, 5]
unique = []
seen = set()
for item in l:
    if l.count(item) == 1:
        unique.append(item)
print(unique)