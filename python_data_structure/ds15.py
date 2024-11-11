# List, Dictionary, & String: Given a list of sentences,  create a dictionary where each key is a unique word and the  value is the total number of sentences in which that word  appears.
sentences = ["This is a test", "This is only a test", "Another test case"]
word_counts = {}
for sentence in sentences:
    words = set(sentence.lower().split()) 
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)