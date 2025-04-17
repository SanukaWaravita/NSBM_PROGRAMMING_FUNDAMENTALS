# Input Marks of 10 students and output the maximum, minimum and average marks. 

marks = []

# Get marks for 10 students
print("Enter marks of 10 students:")
for i in range(10):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

# Calculate maximum, minimum, and average
maximum = max(marks)
minimum = min(marks)
average = sum(marks) / len(marks)

# Output the results
print(f"\nMaximum mark: {maximum}")
print(f"Minimum mark: {minimum}")
print(f"Average mark: {average}")