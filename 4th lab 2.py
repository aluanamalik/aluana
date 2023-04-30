#Write a Python program to convert degree to radian
pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#Write a Python program to calculate the area of a trapezoid
height = float(input("Input height: "))
a = float(input("Input a : "))
b = float(input("Input b: "))
area = ((a+b)/2)*height
print(area)

#Write a Python program to calculate the area of regular polygon
numOfSides= float(input("Input Number Of Sides: "))
lenOfSides = float(input("Input Length of Sides : "))
area = (((numOfSides*lenOfSides)*lenOfSides/2)/2)
print(area)

#Write a Python program to calculate the area of a parallelogram
HeightOfParallelogram= float(input("Input Height of parallelogram: "))
lenOfBase = float(input("Input Length of base : "))
area = (HeightOfParallelogram*lenOfBase)
print(area)
