# Tuple, List, & Set: Given a list of tuples, each containing  two integers, create a set of sums of all the pairs, and return  the result as a sorted list. 
l = [(1, 2), (3, 4), (5, -2), (2, 3)]
total=set()
for t in l:
 add = sum(t)
 total.add(add)
sorted = sorted(total)
print(sorted)
