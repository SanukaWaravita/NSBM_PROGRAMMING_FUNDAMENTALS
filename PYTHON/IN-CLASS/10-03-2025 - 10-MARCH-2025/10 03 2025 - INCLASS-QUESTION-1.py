# Write a program to input a student admission number, marks for a module and displaay admission number with grade.
# The grade iss calculated as follows:
# Marks Grade
# >= 75 A
# 65-75 B
# 55-65 C
# 45-55 S
# <45   F

# Input of the admission number and the marks
Admission = int(input("Enter your Student Admission no. here: "))
ModuleMarks = int(input("Enter your module marks here: "))

# Checking for the grade based on the module marks
if (ModuleMarks >= 75):
    Grade = "A"
elif (ModuleMarks < 75 and ModuleMarks > 65):
    Grade = "B"
elif (ModuleMarks < 65 and ModuleMarks > 55):
    Grade = "C"
elif (ModuleMarks < 55 and ModuleMarks >45):
    Grade = "S"
else:
    Grade = "F"

# Printing the grade along with the student admission number
print(f"Student admission number: {Admission}")
print(f"Grade: {Grade}")
print(f"{Admission}'s grade is {Grade}")