# 8. Check if a given string is a palindrome (reads the same backward as forward).
s = input("Enter a string: ")
if s == s[::-1]:  
    print("String is Palindrome")
else:
    print("String is not Palindrome")