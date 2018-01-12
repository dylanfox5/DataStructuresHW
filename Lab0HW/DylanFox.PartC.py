#Dylan Fox
#Write a program that accepts a number N from stdin and prints out the volume of a sphere with radius N meters.

import math

r = float(input("radius: "))
print("volume is: ", (4/3) * math.pi * r ** 3)
