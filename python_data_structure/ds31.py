# Tuple, Dictionary, & List: Given a list of tuples, where  each tuple contains a product name and a price, create a  dictionary where the keys are product names, and the values  are the average prices of those products (in case of multiple  occurrences). 
l=[("Shampoo",300),("Conditioner",200),("Rice",600),("Shampoo",500),("Rice",350)]
price_dict ={}
count={}

for product,price in l:
 if product in price_dict:
  price_dict[product]+=price
  count[product]+=1
 else:
  price_dict[product]=price
  count[product]=1

for product in price_dict:
 price_dict[product]/=count[product]
 
print(price_dict)