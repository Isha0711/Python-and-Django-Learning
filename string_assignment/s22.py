#22. Write a program that removes punctuation from a string.
s = input("Enter any string: ")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""
for x in s:
    if x not in punc:
        result += x
print(result)