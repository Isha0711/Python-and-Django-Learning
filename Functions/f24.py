# Write a recursive function reverse_string_recursive(s) to reverse a  string. 
def reverse_string_recursive(s):
    if len(s) <= 1:  
        return s
    return s[-1] + reverse_string_recursive(s[:-1])