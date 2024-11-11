# Dictionary, List, & String: Given a string of sentences,  create a dictionary where the keys are the words (case insensitive) and the values are lists of sentences in which each word appears. 
s = "Python is fun. Python learning takes time. But I enjoy it."
sentence = s.split(". ")
result = {}
for x in sentence:
    words = x.lower().split()
    for i in words:
        if i not in result:
            result[i] = []
        result[i].append(x)
print(result)
