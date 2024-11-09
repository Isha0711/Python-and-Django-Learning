# Write a function fibonacci(n) that returns the first n numbers in the  Fibonacci sequence. 
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_seq = [0, 1]  
    while len(fib_seq) < n:
        temp = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(temp)
    return fib_seq
