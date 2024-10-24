#How do you find the length of the longest tuple in a list of tuples?

tuples_of_tuple=[(4, 5, 1), (7, 19), (14, 8, 0, 2, 10, 3, 5), (19, 11, 6, 6, 1, 5, 10), (18, 0), (13, 6)]
count=0 
longest_length=0 
longest_tuple=() 
for i in range(len(tuples_of_tuple)): 
    if isinstance(tuples_of_tuple[i],tuple): 
        longest_length=len(tuples_of_tuple[i]) 
        longest_tuple=tuples_of_tuple[i] 
        count=i 
        break 
for i in range(count,len(tuples_of_tuple)): 
    if isinstance(tuples_of_tuple[i],tuple): 
        if len(tuples_of_tuple[i])>longest_length: 
            longest_length=len(tuples_of_tuple[i]) 
            longest_tuple=tuples_of_tuple[i] 
         
print(f"Length of longest tuple is : {longest_length}") 
print(f"Longest tuple : {longest_tuple}") 