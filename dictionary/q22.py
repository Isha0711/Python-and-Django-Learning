#How do you count the occurrences of each element in a list using a dictionary?

l=[1,2,3,4,5,6,3,4,5,8,4,1,4,6,8,90,56,3,4,5,6,7,8,9] 
count_dic={} 
for items in l: 
    if items in count_dic: 
       count_dic[items]=count_dic[items]+1 
    else: 
        count_dic[items]=1

print(count_dic) 