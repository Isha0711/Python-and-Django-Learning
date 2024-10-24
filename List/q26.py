#How would you remove duplicates from a list while preserving the original order?
l=[1,3,45,3,65,19,22,4,76,444,56,19,1,2,5] 
no_duplicate=[] 
for items in l: 
    if items not in no_duplicate: 
     no_duplicate.append(items) 
print(no_duplicate) 