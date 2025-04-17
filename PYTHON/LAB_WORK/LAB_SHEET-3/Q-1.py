# Write a program to input two numbers and display the highest number.

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Determine and display the highest number
if num1 > num2:
    print(f"The highest number is: {num1}")
elif num2 > num1:
    print(f"The highest number is: {num2}")
else:
    print("Both numbers are equal.")