# Write a function factorial(n) that returns the factorial of a given number n.
def factorial(n):
 if n==0 or n==1:
  return 1
 else: 
  return n * factorial(n-1)
