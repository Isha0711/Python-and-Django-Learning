#How do you combine two dictionaries, summing values for common keys?

d1={100:"Nikita",200:"Pragyan",300:"Aayush",400:"Archana"}
d2={400:"dipesh",500:"isha",600:"vaskar",}
common_dict={} 
for k,v in d1.items(): 
   common_dict[k]=v 
for k,v in d2.items(): 
    if k in common_dict: 
       common_dict[k]+=v 
    else: 
       common_dict[k]=v 
print(common_dict) 