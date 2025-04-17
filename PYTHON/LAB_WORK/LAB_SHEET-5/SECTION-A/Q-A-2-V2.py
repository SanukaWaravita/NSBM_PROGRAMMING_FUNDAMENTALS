# Write a Python program to calculate and print the total of 10 marks and the average. If the average is less than 50 program should print “Fail!” otherwise “Pass!”

for _ in range(10):
    mark = float(input("Enter the marks here"))
    total = total+mark

avg = total / 10 

print("Total Marks:", total)
print("Average Marks:", avg)