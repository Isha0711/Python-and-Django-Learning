#  String, Set, & Dictionary: Given a string, create a  dictionary where each key is a character, and the value is a  set of indices where that character appears in the string. 
s = "hello world"
i = {}
for x, char in enumerate(s):
    if char not in i:
        i[char] = set()
    i[char].add(x)
print(i)