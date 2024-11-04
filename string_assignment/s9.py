# 9. Write a program that checks if a substring exists within a string.

s=input("Enter a string: ")
ss= input("Enter the substring to find in the string: ")
if (s.find(ss))==-1:
 print("Substring doesn't exist within the string")
else:
 print("The substring exists within the string")
