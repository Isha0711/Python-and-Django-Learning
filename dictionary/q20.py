#How do you get a dictionary’s items as a list of tuples?
d={400:"dipesh",500:"isha",600:"vaskar",}
dic_items=[(k,v) for k,v in d.items()] 
print(dic_items) 
