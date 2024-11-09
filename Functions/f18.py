# Write a function calculate_area(shape, dimension) that calculates the  area of a shape (circle, square, or rectangle) based on the given  dimensions. 
import math
def calculate_area(shape, dimension):
    if shape == "circle":
        return math.pi * (dimension ** 2)
    elif shape == "square":
        return dimension * dimension
    elif shape == "rectangle":
        length, width = dimension
        return length * width
    else:
        return "Unknown shape"