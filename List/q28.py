#How would you check if one list is a subset of another list?
l1=[x for x in range(50) if x%2!=0] 
l2=[x for x in range(1,100) ] 
 
for items in l1: 
    if items not in l2: 
        print("l1 is not subset of l2.") 
        break 
else: 
    print("l1 is subset of l2.") 
 
for items in l2: 
    if items not in l1: 
        print("l2 is not subset of l1.") 
        break 
else: 
    print("l2 is subset of l1.") 