# Input of the radius of the circle
radius = float(input("Type the radius of the circle here: "))

# Defining of constant value to pi
pi = 3.14149

# Calculating diameter, circumference and area
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius 

# Printing calculation
print(f"Diameter of the circle is 2 ⨉ {radius} = {diameter}")
print(f"Circumference of the circle is 2 ⨉ pi ⨉ {radius} = {circumference}")
print(f"Area of the circle is pi ⨉ {radius} ⨉ {radius} = {area}")