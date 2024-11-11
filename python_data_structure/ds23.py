# Dictionary, List, & Set: Given a list of students and their  grades, create a dictionary that groups students by their  grade, and return a set of all unique grades. 
students = [("Ram", "A"), ("Hari", "B"), ("Sita", "A"), ("Gita", "C")]
grade_dict = {}
unique = set()
for name, grade in students:
    unique.add(grade)
    if grade in grade_dict:
        grade_dict[grade].append(name)
    else:
        grade_dict[grade] = [name]
print(grade_dict)
print(unique)
