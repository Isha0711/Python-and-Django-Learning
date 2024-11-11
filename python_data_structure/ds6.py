#  List & Set: Write a Python program to find the common  elements between two lists using a set for efficiency.
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common = set(l1) & set(l2) 
print(common)