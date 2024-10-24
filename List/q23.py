#How would you sort a list without using any built-in sort functions (e.g., using asorting algorithm like bubble sort)?
l=[1,3,45,65,22,4,76,444,56,19,1,2,5] 
sorted_list=[] 
for item in l: 
    i=0 
    for x in sorted_list: 
       if item<x: 
        sorted_list.insert(i,item) 
        i=i+1 
        break 
       i=i+1 
    else: 
      sorted_list.append(item) 
print(sorted_list) 