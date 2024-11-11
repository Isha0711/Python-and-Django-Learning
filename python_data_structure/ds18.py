#  String, List, & Set: Given a string, find all the unique  words (case-insensitive) that appear in the string and return them as a sorted list.
text = "This is a test. This test is only a test."
words = text.split()
unique = sorted(set(word.strip(".").lower() for word in words)) 
print(unique)