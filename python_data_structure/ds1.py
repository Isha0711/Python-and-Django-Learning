# String & List: Given a sentence, split the sentence into words,  remove duplicate words (maintaining the order), and return the result as a list. 
sentence = "this is a test this is only a test"
words = sentence.split()  
new = []
for word in words:
    if word not in new:  
        new.append(word)
print(new)