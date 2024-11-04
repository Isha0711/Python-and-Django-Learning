# 3. Write a Python program that counts the number of vowels in a given string.
v=0
s=(input("Enter a string: ")).lower()
v+=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
print(v)