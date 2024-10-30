#How do you create a dictionary with default values for missing keys?

d={400:"dipesh",500:"isha",600:"vaskar",}
(d.setdefault(100,"Hello")) 
print(d) 
d={100:"Nikita",200:"Pragyan",300:"Isha",400:"Archana",500:"Ayush"}
(d.setdefault(600,"Blah")) 
print(d) 