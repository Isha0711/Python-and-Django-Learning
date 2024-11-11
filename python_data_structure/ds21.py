# List, Set & Tuple: Given a list of tuples, where each  tuple contains two integers, return a list of tuples where the  sum of the integers in each tuple is unique. 
l = [(1, 2), (3, 4), (5, -2), (2, 3)]
unique = set()
result = []
for t in l:
    total = sum(t)
    if total not in unique:
        unique.add(total)
        result.append(t)
print(result)
