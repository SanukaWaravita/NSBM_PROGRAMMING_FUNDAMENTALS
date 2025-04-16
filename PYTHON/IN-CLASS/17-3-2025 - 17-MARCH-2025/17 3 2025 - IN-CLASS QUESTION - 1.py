<<<<<<< HEAD
# Write a program to allow the user to input 10 numbers and display the average.

total = 0
count = 0

while count < 10:
    #number = float(input("Enter number " + str(count + 1) + ": "))
    number = float(input("Enter a number: "))
    total += number
    count += 1

average = total / 10
=======
# Write a program to allow the user to input 10 numbers and display the average.

total = 0
count = 0

while count < 10:
    #number = float(input("Enter number " + str(count + 1) + ": "))
    number = float(input("Enter a number: "))
    total += number
    count += 1

average = total / 10
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print("The average of the 10 numbers is:", average)