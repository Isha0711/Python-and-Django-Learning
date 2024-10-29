#How do you check if one set is a subset of another set?

s1={10,20,30,40,50}
s2={10,20,30}

for item in s1:
    if item not in s2:
        print("s1 is not subset of s2 ")
        break
else:
        print("s1 is subset of s2 ")

for item in s2:
    if item not in s1:
        print("s2 is not subset of s1 ")
        break
else:
        print("s2 is subset of s1")