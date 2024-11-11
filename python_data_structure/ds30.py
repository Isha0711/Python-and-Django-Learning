# String, Set, & List: Given a string of space-separated  words, return a sorted list of words that appear more than  once, without duplicates. 
s="python is very very fun fun"
word=s.split()
result=set()
count={}
for x in word:
  count[x]=count.get(x,0)+1

for x,count in count.items():
 if count>1:
  result.add(x)
  
print(sorted(result))
