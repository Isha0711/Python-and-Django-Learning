#How would you find the majority element in a list (the element that appears more than half the time)?
l1=[1,4,5,6,7,8,9,10,11,8,8,12,2,8,8,8,3,8,8,8,8,4,5,6,7,8,2,3,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,5,6,7,8,9] 
majority_number=len(l1)//2 
for items in l1: 
    if l1.count(items)>majority_number: 
     print(f"The number that appear majority of time is: {items}") 
     break 
else: 
     print("No number occur in majority") 


