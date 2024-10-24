#How would you find the longest consecutive sequence in a list of numbers?
l1=[1,4,5,6,7,8,9,10,11,12,2,3,4,5,6,7,8,2,3,4,5,6,7,8,9] 
longest=0 
longest_list=[l1[0]] 
streak=1 
temp=[l1[0]] 
 
for i in range(1,len(l1)): 
    if l1[i]==l1[i-1]+1: 
        temp.append(l1[i]) 
        streak+=1 
    else: 
        if streak>longest: 
            longest=streak 
            longest_list=temp.copy() 
        streak=1 
        temp=[l1[i]] 
     
     
if streak>longest: 
    longest=streak 
    longest_list=temp.copy() 
print(f"Longest sequence of list is : {longest_list} with length {longest}") 