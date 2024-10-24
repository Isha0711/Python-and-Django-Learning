#How would you find pairs of elements in a list that sum up to a specific number?
l=[1,3,45,3,65,19,22,4,76,444,56,19,1,2,5] 
user_input=int(input("Enter number: ")) 
pairs=[] 
for i in range(len(l)): 
    for j in range(i+1,len(l)): 
     if l[i]+l[j]==user_input: 
      pairs.append([l[i],l[j]]) 
print(pairs) 