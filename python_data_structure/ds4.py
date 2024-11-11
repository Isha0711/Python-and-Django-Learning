# Tuple & List: Given a list of tuples where each tuple contains  two numbers, return a new list containing the product of the  two numbers in each tuple. 
tuple_list = [(1, 2), (3, 4), (5, 6)]
products = [a * b for a, b in tuple_list]  
print(products)