import math
print("Enter the radius of the circle")
"""Input validation"""
radius = float(input())
"""Formula to calculate the area of a circle"""
a = float(math.pi*radius*radius)
"""Formula to calculate the area of a circle"""
c = float(2*math.pi*radius)
print("The area of the circle is " + str(a))
print("The circumference of the circle is " + str(c))

