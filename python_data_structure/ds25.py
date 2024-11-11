# Set, List, & String: Given two lists of strings, return a  list of strings that are in both lists, but only include those  that have more than 3 vowels. 
l1 = ["beautiful", "amazing", "wonderful", "okay"]
l2 = ["wonderful", "awesome", "beautiful", "perfect"]
common = []
vowels="aeiou"
count=0
for word in set(l1).intersection(set(l2)):
    for x in word.lower():
     if x in vowels:
      count+=1
    if count > 3:
        common.append(word)
print(common)
