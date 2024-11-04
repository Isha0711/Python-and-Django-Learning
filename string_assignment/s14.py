#14. Check if two strings are anagrams of each other (contain the same letters in different orders).

s1= input("Enter the first string: ")
s2= input("Enter the second string: ")

if sorted(s1)==sorted(s2):
 print("The two strings are anagrams of each other")
else:
 print("The two strings aren't anagrams of each other")