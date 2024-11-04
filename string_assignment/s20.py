#20. Find the longest word in a given string.
s= input("Enter any string: ")
word = s.split()
longest = ""
for x in word:
    if len(x) > len(longest):
        longest = x
print(longest)