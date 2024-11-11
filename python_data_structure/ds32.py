# Set, Dictionary, & List: Given a list of words, create a  dictionary where the key is the word length, and the value is  a set of words of that length. 
l = ["day","apple", "banana", "cat", "orange", "date"]
result = {}
for x in l:
    length = len(x)
    if length not in result:
        result[length] = set()
    result[length].add(x)
print(result)
