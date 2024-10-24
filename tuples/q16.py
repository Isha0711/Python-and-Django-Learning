#How do you sort a list of tuples based on the second element in each tuple?

list_of_tuple=[(1,2,3),(3,2,1),(4,7,8),(5,4,3,2),(6,3),(9,0)] 
for i in range(len(list_of_tuple)):  
    for j in range(0, len(list_of_tuple)-i-1): 
      if list_of_tuple[j][1] > list_of_tuple[j + 1][1]: 
        list_of_tuple[j], list_of_tuple[j + 1] = list_of_tuple[j + 1], list_of_tuple[j] 
print(list_of_tuple) 