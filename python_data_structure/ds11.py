# Tuple & Set: Given a tuple of numbers, return a set of  all even numbers from the tuple. 
numbers = (1, 2, 3, 4, 5, 6)
even = {n for n in numbers if n % 2 == 0}
print(even)