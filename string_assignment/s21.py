# 21. Write a program that splits a string by commas and then sorts each word in alphabetical order.
s = input("Enter any string with at least one comma: ")
word = s.split(",")
sort = ",".join(sorted(word))
print(sort)