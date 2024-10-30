#How do you convert two lists (keys and values) into a dictionary?
l1 = [10, 20, 30, 40, 50]
l2 = ['ravi','shyam','hari','sita','gita']

d = {}

for i in range(min(len(l1), len(l2))):
    d[l1[i]] = l2[i] 

print(d)