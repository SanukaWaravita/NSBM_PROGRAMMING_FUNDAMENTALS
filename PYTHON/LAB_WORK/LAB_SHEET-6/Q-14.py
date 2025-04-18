# Write a Python program that prompts the user to enter a number and calculates its factorial using the math library. Display the result. (Ex: factorial of number 5 is calculated as 5! = 5*4*3*2*1). 

import math

number = int(input("Enter your number here: "))

factorial = math.factorial(number)

print(f"The factorial of the number {number} is: {factorial}")