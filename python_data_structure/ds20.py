# List & Dictionary: Given a list of students with their  names and grades (e.g., ("John", 85)), return a dictionary where the keys are the grades and the values are lists of  students who received that grade. 
students = [("Ram", 85), ("Hari", 90), ("Sita", 85), ("Gita", 90)]
grades = {}
for name, grade in students:
    grades.setdefault(grade, []).append(name)  
print(grades)