# List, Set, & String: Given a list of strings, create a set  containing all unique characters across all strings, then  return a list of these characters sorted alphabetically. 
l = ["apple", "banana", "berry"]
unique = set()
for x in l:
    unique.update(x)
sorted = sorted(unique)
print(sorted)
