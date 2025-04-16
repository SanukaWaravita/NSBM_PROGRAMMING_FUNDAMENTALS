<<<<<<< HEAD
# Input Employee Number and Hours worked by employees to display the following:

#   Employee Number, Over Time Payment, and the percentage of employees whose Over Time Payment exceed Rs. 4000/-. 
#   The user should input –999 as Employee Number to end the program, and the normal Over Time Rate is Rs.150 per hour and Rs. 200 per hour for hours in excess of 40.

print("Type the employee no. and hours worked by the employees (type -999 to stop)")

count_over_4000 = 0
employee_count = 0

while True:
    employee_no = int(input("Enter employee no. here: "))

    if employee_no == -999:
        break

    employee_work_hours = int(input("Enter the number of hours worked: "))

    if employee_work_hours <= 40:
        over_time_payment = 150 * employee_work_hours
    else:
        over_time_payment = (40 * 150) + ((employee_work_hours - 40) * 200)

    employee_count += 1

    if over_time_payment > 4000:
        count_over_4000 += 1

    print(f"Over time payment for employee {employee_no} is: {over_time_payment}")

if employee_count > 0:
    if count_over_4000 > 0:
        over_4000_percentage = (count_over_4000 / employee_count) * 100
        print(f"The percentage of employees with an over time payment > 4000 is: {over_4000_percentage:.2f}%")
    else:
        print("There is no employee with an over time payment > 4000.")
else:
=======
# Input Employee Number and Hours worked by employees to display the following:

#   Employee Number, Over Time Payment, and the percentage of employees whose Over Time Payment exceed Rs. 4000/-. 
#   The user should input –999 as Employee Number to end the program, and the normal Over Time Rate is Rs.150 per hour and Rs. 200 per hour for hours in excess of 40.

print("Type the employee no. and hours worked by the employees (type -999 to stop)")

count_over_4000 = 0
employee_count = 0

while True:
    employee_no = int(input("Enter employee no. here: "))

    if employee_no == -999:
        break

    employee_work_hours = int(input("Enter the number of hours worked: "))

    if employee_work_hours <= 40:
        over_time_payment = 150 * employee_work_hours
    else:
        over_time_payment = (40 * 150) + ((employee_work_hours - 40) * 200)

    employee_count += 1

    if over_time_payment > 4000:
        count_over_4000 += 1

    print(f"Over time payment for employee {employee_no} is: {over_time_payment}")

if employee_count > 0:
    if count_over_4000 > 0:
        over_4000_percentage = (count_over_4000 / employee_count) * 100
        print(f"The percentage of employees with an over time payment > 4000 is: {over_4000_percentage:.2f}%")
    else:
        print("There is no employee with an over time payment > 4000.")
else:
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print("No employees were entered.")