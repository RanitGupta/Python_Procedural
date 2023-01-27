import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circum(radius):
    return math.pi * 2.0 * radius

def calcCircleParams(radius):
    return circle_area(radius), circle_circum(radius)