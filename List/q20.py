#How would you split a list into two parts at a given index?
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
user_input=int(input("Enter index where list need to be splitted: ")) 
l1,l2=l[:user_input:],l[user_input::] 
print(f"List 1: {l1}") 
print(f"List 2: {l2}")