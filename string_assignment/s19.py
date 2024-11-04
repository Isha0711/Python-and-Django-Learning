#19. Write a program to remove duplicate characters from a string while preserving the order of characters.
s= input("Enter any string: ")
result = ""
for x in s:
    if x not in result:
        result += x
print(result)
