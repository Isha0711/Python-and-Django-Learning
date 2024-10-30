#How do you sort a dictionary by its values?
d={400:"dipesh",500:"isha",600:"vaskar",}
sorted_d=dict(sorted(d.items(),key=lambda item:item[1])) 
print(sorted_d) 