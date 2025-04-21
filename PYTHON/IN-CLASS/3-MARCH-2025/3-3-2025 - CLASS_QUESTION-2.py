# Question: Write a program to input a number and display the entered number as a positive, negative or a zero. 
number = int(input("Enter a number here: "))

if(number > 0):
    print("The number you have entered is positive.")
elif(number < 0):
    print("The number you have entered is negative.")
else:
    print("The number you have entered is a zero.")