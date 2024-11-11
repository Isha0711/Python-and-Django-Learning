#  Set & Dictionary: Given a dictionary of words as keys  and their definitions as values, return a set containing all the  words whose definitions contain a specific keyword. 

dictionary = {
    "apple": "Apple is red in color.",
    "banana": "Banana is yellow in color.",
    "carrot": "Carrot is a vegetable and is orange."
}
k = "color"
words = {word for word, d in dictionary.items() if k in d}
print(words)