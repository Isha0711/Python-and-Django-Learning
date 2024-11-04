# 32. Write a program to find the shortest word in a string.
s = input("Enter any string: ")
word = s.split()
shortest = word[0]
for x in word:
    if len(x) < len(shortest):
        shortest = x
print(shortest)