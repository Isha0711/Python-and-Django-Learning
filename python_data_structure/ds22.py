# String & Tuple: Write a program that takes a string,  creates a tuple of each word in the string, and sorts the tuple  in reverse alphabetical order. 
s= "Python programming is both fun and educational".lower()
words_tuple = tuple(s.split())
sorted = tuple(sorted(words_tuple, reverse=True))
print(sorted)
