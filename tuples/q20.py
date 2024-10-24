#How do you check if a tuple contains other tuples as elements?

tuples_of_tuple=(10,20,30,40,50,60,(30,20)) 
for items in tuples_of_tuple: 
    if isinstance(items,tuple): 
        print("It contains tuple as another element.") 
        break 
else: 
    print("It does not contain another tuple as element.") 