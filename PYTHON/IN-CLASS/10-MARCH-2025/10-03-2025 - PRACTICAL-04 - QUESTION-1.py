# Use If-Else and write a program that reads an integer and determines and prints if the number is even or odd. (i.e. divisible by 2)

# Input of integer number
Number = int(input("Type your number here: "))

# Checking whether integer odd or even
if (Number % 2 == 0):
    print("The number you entered is even")
else: 
    print("The number you entered is odd")