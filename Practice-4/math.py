import math

# Tasl-1

degree = float(input("Input degree: "))

print("Output radian: ", degree * (math.pi/180))

# Task-2

height = float(input("Height: "))
basef = float(input("Base, first value: "))
bases = float(input("Base, second vale: "))

print("Expected Ouput: ", ((basef + bases) * height) / 2)

# Task-3

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = (sides * length**2) / (4 * math.tan(math.pi / sides))

print("The area of polygon is: ", area)

# Task-4

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

print("Expected Output: ", base * height)
