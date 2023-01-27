from circles import *

def main():
    radius = 3
    area, circum = calcCircleParams(radius)
    print("A circle of radius " + str(radius) + " has an area of " + str(area) + " and a circumference of " + str(circum))

main()