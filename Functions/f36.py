#Write a function multiply_all(*args) that multiplies all the numbers  passed as arguments. 
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result