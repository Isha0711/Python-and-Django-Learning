#25. Write a Python program to convert a string from snake_case to camelCase.
s = input("Enter any string: ")
camelCase = ""
capital = False
for x in s:
    if x == "_":
        capital = True
    elif capital:
        camelCase += x.upper()
        capital = False
    else:
        camelCase += x
print(camelCase)