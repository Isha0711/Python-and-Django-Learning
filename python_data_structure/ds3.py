# Set & String: Write a Python program that takes two strings  and returns the set of unique characters that appear in both  strings. 
s1 = "hello"
s2 = "world"
common = set(s1) & set(s2)  
print(common)