# List & Dictionary: Given a list of numbers, create a  dictionary where each key is a number and the value is its  frequency in the list. 
numbers = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1  
print(freq)