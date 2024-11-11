# String & Dictionary: Given a string, count the occurrences of  each character and return the result as a dictionary.
s = "hello"
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1  
print(count)