#How do you find the key with the maximum value in a dictionary?
d={400:"dipesh",500:"isha",600:"vaskar",}
max_value=max(d.values()) 
k=[k for k,v in d.items() if v==max_value][0] 
print(f"Maximum value is {max_value} and its key is: {k}") 
