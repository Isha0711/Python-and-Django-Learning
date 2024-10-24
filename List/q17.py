#Given two lists, how would you find the common elements between them?
l1=[10,20,30,40,50,60] 
l2=[10,20,200,300,400,50,600] 
common_list=[] 
for item in l1: 
   if item in l2: 
      common_list.append(item) 
print(common_list) 