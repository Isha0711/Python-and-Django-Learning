# 24. Write a program to find the frequency of each character in a string.
s = input("Enter any string: ")
freq = {}
for x in s:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)
