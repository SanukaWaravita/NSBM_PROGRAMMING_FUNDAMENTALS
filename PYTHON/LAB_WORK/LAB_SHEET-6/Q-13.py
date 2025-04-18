# Write a Python program to calculate and display the length of the hypotenuse of a right-angled triangle where the lengths of the two sides adjacent to the right angle are 3 units and 4 units, respectively. 

import math

a = 3
b = 4

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of the hypotenuse of a right-angled triangle is: {c}")