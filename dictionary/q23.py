#How do you group a list of items by a certain property using a dictionary?
list=['Isha','Dipesh','Nikita',"Archana",'Aayush']
d={} 
for words in list: 
    first_letter=words[0] 
    if first_letter in d: 
      d[first_letter].append(words) 
    else: 
      d[first_letter]=[] 
      d[first_letter].append(words) 

print(d) 