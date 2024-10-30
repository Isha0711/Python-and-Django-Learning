#How do you get the value for a key without raising an error if the key doesn't exist?
d={400:"dipesh",500:"isha",600:"vaskar",}
print(d.get("ram","Not found")) 
print(d.get(100,"Not found")) 