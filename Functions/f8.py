# Write a function count_vowels(s) that returns the number of vowels  in the string s. 
def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count
