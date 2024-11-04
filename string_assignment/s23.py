# 23. Write a Python program that checks if a string contains only alphabets (no digits or special characters).
s = input("Enter any string: ")
alpha = True
for x in s:
    if not x.isalpha():
        alpha = False
        break
print(alpha)