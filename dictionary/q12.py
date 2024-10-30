#How do you merge two dictionaries?
d1={400:"dipesh",500:"isha",600:"vaskar",}
d2={100:"ram",200:"shyam"}
d3={**d1, **d2}
print(d3)