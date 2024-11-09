# Write a function sum_of_squares(n) that returns the sum of squares  of the first n natural numbers.
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2 
    return total
