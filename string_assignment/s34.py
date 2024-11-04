# 34. Write a program that checks if a string contains any numeric characters.
s = input("Enter any string: ")
digit = False
for x in s:
    if x.isdigit():
        digit = True
        break
print(digit)
