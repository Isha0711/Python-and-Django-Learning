#How do you freeze a set to make it immutable?

s = {1, 2, 3, 4}
immutable_set = tuple(s)
print("Immutable Set:", immutable_set)