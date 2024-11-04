# 30. Write a Python program that checks if a string starts and ends with the same character.
s = input("Enter any string: ")
result = len(s) > 0 and s[0] == s[-1]
print(result)