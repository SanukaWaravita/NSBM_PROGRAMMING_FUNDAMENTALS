# Write a program to allow the user to input numbers and display the highest. 
number1 = int(input("Type your first number here: "))
number2 = int(input("Type you second number here: "))

if(number1 > number2):
    print("The highest number is: ", number1)
else:
    print("The highest number is: ", number2)