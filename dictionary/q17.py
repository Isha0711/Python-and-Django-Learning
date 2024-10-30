#How do you reverse the key-value pairs in a dictionary?
d={400:"dipesh",500:"isha",600:"vaskar",}
reverse_d={v:k for k,v in d.items()} 
print(reverse_d) 