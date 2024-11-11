# String, List, & Dictionary: Given a paragraph, count the  frequency of each word (case-insensitive) and return a  dictionary where the keys are the words and the values are  their frequencies.
paragraph = "This is a test. This test is only a test."
words = paragraph.lower().split() 
frequency = {}
for word in words:
    word = word.strip(".") 
    frequency[word] = frequency.get(word, 0) + 1 
print(frequency)