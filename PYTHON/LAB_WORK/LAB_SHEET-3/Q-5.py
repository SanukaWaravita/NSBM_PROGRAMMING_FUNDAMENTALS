# Write a program that reads in two integers and determines and prints if the first is a multiple of the second. 

# Input two integers
num1 = int(input("Type your first number here: "))
num2 = int(input("Type your second number here: "))

# Determine if the first number is a multiple of the second
if num2 == 0:
    print("The second number cannot be zero.")
elif num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}")
else:
    print(f"{num1} is not a multiple of {num2}")