#13. Write a program to compare two strings lexicographically and determine which one comes first alphabetically.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if s1 < s2:
    print(f'"{s1}" comes before "{s2}" alphabetically.')
elif s1 > s2:
    print(f'"{s1}" comes after "{s2}" alphabetically.')
else:
    print(f'"{s1}" and "{s2}" are the same alphabetically.')
