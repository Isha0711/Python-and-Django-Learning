# Tuple, List & Set: Write a Python program that takes a  list of tuples, where each tuple contains a name and an age,  and returns a set of unique ages, and creates a new list of  tuples with the names of people who are older than 30. 
l=[("Ram",50),("Sita",45),("Hari",24),("Gita",12),("Rita",45)]
unique = set()
new_list=[]
for name,age in l:
 unique.add(age)
 if age>30:
  new_list.append((name,age))
print(unique)
print(new_list)