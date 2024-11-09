# Write a recursive function fibonacci_recursive(n) to return the n-th  Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:  
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  