# Imagine you are a teacher and you want to sort the student names in the register. Write a python program that asks the user to enter the names of five students and display the names of the students who appear first and last once the register is sorted in the ascending order of the alphabet. 

student_list = []

for i in range(1, 6):
    student_name = input(f"Enter the {i} student's name: ")
    student_list.append(student_name)

student_list.sort()

print(f"The name of the first student in the register is: {student_list[0]}")
print(f"The name of the last student in the register is: {student_list[-1]}")