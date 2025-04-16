print("Type Employee Number and Hours Worked(Type Employee Number = -999 to STOP)")

count_over_4000 = 0
employee_count = 0
employees = []

while True:
    emp_no = int(input("Enter Employee Number:"))

    if emp_no == -999:
        break

    work_hours = int(input("Enter Hours Worked:"))

    if work_hours <= 40:
        OTP = 150 * work_hours
    else:
        OTP = 150*40 + (work_hours - 40)*200

    employees.append((emp_no,OTP))
    
    employee_count+=1

    if OTP > 4000:
        count_over_4000+=1

for emp in employees:
    print(f"Employee Number : {emp[0]} , Over Time Pay : Rs.{emp[1]:.2f}")

if employee_count > 0:
    if count_over_4000 > 0:
        over_4000_percentage = (count_over_4000 / employee_count) * 100
        print(f"The percentage of employees with OPT over Rs.4000 : {over_4000_percentage:.2f}%")
    else:
        print("NO employees with OPT over Rs.4000")
else:
    print("No employee details were entered.")
