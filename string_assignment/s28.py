# 28. Write a Python program that repeats a string n times where n is provided by the user.
s = input("Enter any string: ")
n = int(input("Enter the number of repetitions: "))
result = ""
for _ in range(n):
    result += s
print(result)
