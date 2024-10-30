#How do you find the intersection of two dictionaries (keys that exist in both)?
d1={100:"Nikita",200:"Anshu",300:"Aayush",400:"Archana",500:"Isha"}
d2={500:"Kritika",600:"Anshu",300:"Niki",700:"Isha"} 
print("Keys that exist in both dictionaries with their values in  are :") 
print("Key\tD1Values\t\tD2values") 
for k,v in d1.items(): 
    if k in d2: 
      print(k,"\t",v,"\t\t\t",d2[k]) 