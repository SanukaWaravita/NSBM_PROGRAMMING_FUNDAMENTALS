# Write a program to input 3 numbers and display the highest number.

# Accepting user input of the three integers
num1 = int(input("Type your first number: "))
num2 = int(input("Type your second number: "))
num3 = int(input("Type your third number here: "))

# Determining the highest number
if (num1 >= num2 and num1 >= num3):
    largestno = num1
elif (num2 >= num1 and num2 >= num3):
    largestno = num2
else:
    largestno = num3

# Printing the largest number
print (f"The largest number is:  {largestno}")