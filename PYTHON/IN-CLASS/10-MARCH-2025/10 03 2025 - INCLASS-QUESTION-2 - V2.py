# Write a program to input 3 numbers and display the highest number.

# Input
no1 = int(input("Enter your first number: "))
no2 = int(input("Enter your second number: "))
no3 = int(input("Enter your third number: "))

# Process
max = no1
if (no2 > max):
    max = no2
if (no3 > max):
    max = no3

# Printing
print(f"The highest is {max}")