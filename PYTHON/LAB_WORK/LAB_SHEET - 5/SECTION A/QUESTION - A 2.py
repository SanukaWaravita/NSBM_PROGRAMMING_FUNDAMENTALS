<<<<<<< HEAD
# Write a Python program to calculate and print the total of 10 marks and the average. If the average is less than 50 program should print “Fail!” otherwise “Pass!”

total = 0
count = 0

while count < 10:
    marks = int(input("Type the marks here: "))
    total += marks
    count += 1

average = total / 10 

if average <= 50:
    print("Fail!")
else: 
=======
# Write a Python program to calculate and print the total of 10 marks and the average. If the average is less than 50 program should print “Fail!” otherwise “Pass!”

total = 0
count = 0

while count < 10:
    marks = int(input("Type the marks here: "))
    total += marks
    count += 1

average = total / 10 

if average <= 50:
    print("Fail!")
else: 
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print("Pass!")