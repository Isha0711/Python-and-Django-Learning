# 29. Write a program that takes a string and removes the first and last characters.
s = input("Enter any string: ")
if len(s) > 2:
    result = s[1:-1]
else:
    result = ""
print(result)