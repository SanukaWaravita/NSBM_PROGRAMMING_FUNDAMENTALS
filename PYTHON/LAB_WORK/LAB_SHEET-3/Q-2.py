# Write a complete program to ask user enter three integer numbers, and then tell the user the largest value and smallest value among the three members.

# Input of three numbers
num1 = float(input("Type your first number here: "))
num2 = float(input("Type your second number here: "))
num3 = float(input("Type your third number here: "))

# Determining the highest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Determining the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Display the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")