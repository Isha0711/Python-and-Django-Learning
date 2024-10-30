#28. How do you invert a dictionary, i.e., swap keys and values?
d={100:"Nikita",200:"Pragyan",300:"Aayush",400:"Archana",500:"Isha"}
reverse_d={v:k for k,v in d.items()} 
print(reverse_d) 