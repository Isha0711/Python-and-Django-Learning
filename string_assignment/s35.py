# 35. Write a Python program to replace every second character of a string with *.
s = input("Enter any string: ")
result = ""
for i in range(len(s)):
    if i % 2 == 1:
        result += "*"
    else:
        result += s[i]
print(result)