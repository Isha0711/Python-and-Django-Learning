# Write a recursive function gcd_recursive(a, b) to find the greatest  common divisor of two numbers. 
def gcd_recursive(a, b):
    if b == 0:  
        return a
    return gcd_recursive(b, a % b)