# Input Details
basic_salary = float(input("Type the basic salary here: "))
years_of_service = float(input("Type the number of years of service here: "))
city_of_work = (input("Type the city (type 'C' if it is colombo): "))
monthly_sales = float(input("Type your monthy sales here: "))

# Calculating additional allowance based on years of service
if years_of_service > 5:
    monthly_additional_allowance = 0.10 * basic_salary
else:
    monthly_additional_allowance = 0

# Calculating additional allowance based on city 
if city_of_work == 'C':
    city_additional_allowance = 2500
else:
    city_additional_allowance = 0

# Monthly bonus payment based monthly sales
if monthly_sales < 25000:
    monthly_bonus_payment = 0.10 * monthly_sales
elif monthly_sales < 50000:
    monthly_bonus_payment = 0.12 * monthly_sales
else:
    monthly_bonus_payment = 0.15 * monthly_sales

# Calculation of gross remuneration
gross_remuneration = basic_salary + monthly_additional_allowance + city_additional_allowance + monthly_bonus_payment

# Printing gross remuneration
print(f"The gross monthly remuneration of the saleman is: {gross_remuneration:}")