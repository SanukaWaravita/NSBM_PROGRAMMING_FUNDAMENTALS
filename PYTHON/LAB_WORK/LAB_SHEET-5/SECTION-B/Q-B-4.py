<<<<<<< HEAD
# Input the Employee No and the Basic Salary of the Employees in an organisation, ending with the dummy value -999 for Employee No and count the number Employees whose Basic Salary > = 5000.

print("Type the employee no. and the basic salary of the employee (type -999 to stop)")

count = 0

while True:

    employeeno = int(input("Enter employee no. here: "))

    if employeeno == -999:
        break

    employee_salary = float(input("Enter basic salary here: "))

    if employee_salary >= 5000:
        count += 1

=======
# Input the Employee No and the Basic Salary of the Employees in an organisation, ending with the dummy value -999 for Employee No and count the number Employees whose Basic Salary > = 5000.

print("Type the employee no. and the basic salary of the employee (type -999 to stop)")

count = 0

while True:

    employeeno = int(input("Enter employee no. here: "))

    if employeeno == -999:
        break

    employee_salary = float(input("Enter basic salary here: "))

    if employee_salary >= 5000:
        count += 1

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print(f"The number of employees with a basic salary >= 5000 is: {count}")