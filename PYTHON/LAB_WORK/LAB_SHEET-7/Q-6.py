# Write a function which accepts 2 integers as parameters and display the sum, difference and product using a single print statement.

def SumDiffProd(a, b):
    sum = a + b
    difference = a - b
    product = a * b

    print(f"The sum of the two numbers is: {sum}\nThe difference of the two numbers is: {difference}\nThe product  of the two numbers is: {product}")

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter you 2nd number here: "))

SumDiffProd(num1, num2)