# Use a FOR loop and write a program to input marks of 10 students and display the average.

total = 0
for x in range (1, 11):
    marks = float(input(f"Enter marks for student {i + 1}: "))
    total_marks += marks

average_marks = total_marks / 10
print(f"The average marks of the 10 students is: {average_marks}")