# Write a function is_anagram(s1, s2) that checks if two strings s1 and  s2 are anagrams of each other. 
def is_anagram(s1, s2):
    s1_sorted = sorted(s1.replace(" ", "").lower()) 
    s2_sorted = sorted(s2.replace(" ", "").lower())
    return s1_sorted == s2_sorted