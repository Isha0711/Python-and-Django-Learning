# String, Tuple, & List: Given a string, convert it into a list  of tuples where each tuple contains a character and its index  in the string.
s = "hello"
t = [(char, i) for i, char in enumerate(s)]  
print(t)