# 31. Write a Python program that counts how many times each vowel appears in a given string.
s = input("Enter any string: ")
vowels = "aeiou"
freq = {}
for x in s:
    if x in vowels:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
print(freq)