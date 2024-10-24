#How would you find the second largest element in a list without using built-in sorting functions?
l=[1,3,45,65,22,4,76,444,56,19,1,2,5] 
sorted_list=[] 
for item in l: 
     i=0 
     for x in sorted_list: 
         if item<x: 
             sorted_list.insert(i,item) 
             i+=1 
             break 
         i+=1 
     else: 
         sorted_list.append(item)

print(f"The second largest element is :{sorted_list[-2]}") 