#How do you check if two sets are disjoint?
set1 = {1, 2, 3,4}
set2 = {4, 5, 6}

disjoint = True

for element in set1:
    for item in set2:
        if element == item:
            disjoint = False
            break  
    if not disjoint:
        break  

if disjoint:
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")