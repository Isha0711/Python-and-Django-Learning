# String, List, & Dictionary: Write a program that takes a  string and returns a dictionary where the keys are the first  characters of words in the string, and the values are lists of  words that start with that character. 
s="apple apron banana cat dog car deer"
word= s.split()
result={}
for x in word:
 first=x[0]
 if first not in result:
  result[first] = []
 result[first].append(x)
print(result)