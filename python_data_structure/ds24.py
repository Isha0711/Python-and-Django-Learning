# String, Tuple, & Dictionary: Write a Python program  that takes a string and returns a dictionary where the keys  are words and the values are tuples, with the first element as  the length of the word and the second as the count of vowels  in the word. 
s = "Python programming language is fun"
vowels = "aeiou"
word = {}
count = 0
for x in s.split():
    length = len(x)
    for i in x.lower():
     if i in vowels:
      count+=1
    word[x] = (length, count)
print(word)
