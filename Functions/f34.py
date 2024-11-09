# Use a lambda function with map() to convert a list of temperatures  from Celsius to Fahrenheit.
temps=[32,36,35,38]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))
print(fahrenheit)