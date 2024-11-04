#27. Write a program to convert all spaces in a string to underscores.
s = input("Enter any string: ")
result = ""
for x in s:
    if x == " ":
        result += "_"
    else:
        result += x
print(result)