# Write a function longest_word(words) that returns the longest word  from a list of words.
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):  
            longest = word
    return longest

