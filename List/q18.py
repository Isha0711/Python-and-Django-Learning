#How would you create a new list that contains only the unique elements from an existing list?
l=[10,20,30,40,10,40,"Hello",'hello',"Hello","Py","World."] 
unique_list=[item for item in l if l.count(item)==1] 
print(unique_list)