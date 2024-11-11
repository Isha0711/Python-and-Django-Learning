# Tuple, List & Set: Write a Python program that takes a  list of tuples, where each tuple contains a name and an age,  and returns a set of names whose age is greater than the average age of all people in the list.
l = [("Ram", 25), ("Hari", 29), ("Gita", 40), ("Sita", 32)]
above_average = set()
total = sum(age for name,age in l) 
average = total / len(l)
for name, age in l:
    if age > average:
        above_average.add(name)
print(above_average)
