# Write a program to allow the user to input 10 numbers and display the average.

total = 0
count = 0

while count < 10:
    #number = float(input("Enter number " + str(count + 1) + ": "))
    number = float(input("Enter a number: "))
    total += number
    count += 1

average = total / 10
print("The average of the 10 numbers is:", average)