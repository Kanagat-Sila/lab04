"""
EX >> 1
import math

d = int(input("Input degree: "))
z = math.ceil(3.14 * d / 180)

print("Output radian: ",z)
"""

"""
EX >> 2
import math

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, secont value: "))

s = (a + b)/2*h

print("Expected Output: ",s)

"""

"""
EX >> 3
import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

s = math.ceil(n * (l * l)/4 * math.tan(math.pi/n))

print("The area of the polygon is: ",s)

"""

import math 

l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))

s = float(h * l)

print("Expected Output: ",s)
