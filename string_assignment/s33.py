# 33. Write a Python program that finds and prints the longest repeated substring in a given string.
s = input("Enter any string: ")
result = ""
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        ss = s[i:j]
        if s.count(ss) > 1 and len(ss) > len(result):
            result = ss
print(result)
