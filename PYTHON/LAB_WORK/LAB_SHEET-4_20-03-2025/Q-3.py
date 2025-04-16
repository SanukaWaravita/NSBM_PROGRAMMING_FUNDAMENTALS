<<<<<<< HEAD
# Create a text-based, menu-driven program that allows the user to choose whether to calculate the circumference of a circle, the area of a circle or the volume of a sphere. The program should then input a radius from the user, perform the appropriate calculation and display the result. 

# Circumference of a circle
# Area of a circle
# Volume of a sphere

pi = 3.14159

print("Select your operation:")
print("A - Circumference of a circle")
print("B - Area of a circle")
print("C - Volume of a sphere")

operation = input("Type your selection here: ")

if operation == 'A' or operation == 'B':
    cradius = float(input("Type the radius of the circle here: "))
else:
    sradius = float(input("Type the radius of the sphere here: "))

if operation == "A":
    circumference = 2 * pi * cradius
    print(f"The circumference of the circle is: {circumference}")
elif operation == "B":
    area = pi * cradius ** 2
    print(f"The area of the  circle is: {area}")
else:  
    volume = (4/3) * pi * sradius ** 3
=======
# Create a text-based, menu-driven program that allows the user to choose whether to calculate the circumference of a circle, the area of a circle or the volume of a sphere. The program should then input a radius from the user, perform the appropriate calculation and display the result. 

# Circumference of a circle
# Area of a circle
# Volume of a sphere

pi = 3.14159

print("Select your operation:")
print("A - Circumference of a circle")
print("B - Area of a circle")
print("C - Volume of a sphere")

operation = input("Type your selection here: ")

if operation == 'A' or operation == 'B':
    cradius = float(input("Type the radius of the circle here: "))
else:
    sradius = float(input("Type the radius of the sphere here: "))

if operation == "A":
    circumference = 2 * pi * cradius
    print(f"The circumference of the circle is: {circumference}")
elif operation == "B":
    area = pi * cradius ** 2
    print(f"The area of the  circle is: {area}")
else:  
    volume = (4/3) * pi * sradius ** 3
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print(f"The volume of the sphere is: {volume}")