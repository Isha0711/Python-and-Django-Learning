# Write a function is_palindrome(s) that checks if the input string s is a  palindrome. 
def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]
