# Input employee name and basic salary
employee_name = input("Enter the employee name: ")
basic_salary = float(input("Enter the basic salary: "))

# Calculate the increment based on the basic salary
if basic_salary < 5000:
    increment = basic_salary * 0.05
elif 5000 <= basic_salary < 10000:
    increment = basic_salary * 0.10
else:
    increment = basic_salary * 0.15

# Calculate the new salary
new_salary = basic_salary + increment

# Display the results
print(f"Employee Name: {employee_name}")
print(f"New Salary: {new_salary:.2f}")