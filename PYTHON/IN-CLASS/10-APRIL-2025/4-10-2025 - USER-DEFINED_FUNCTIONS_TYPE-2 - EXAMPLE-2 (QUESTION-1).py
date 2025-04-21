# Example 2 (Question 1) - Create a function which accept 2 integers and display the highest number.

# function creation

def integermax(a, b):
    maximum = max(a,b)
    print(f"The maximum out of the 2 integers is: {maximum}")

# function calling
n1 = int(input("Enter first number here: "))
n2 = int(input("Enter second number here: "))
integermax(n1, n2)

# Create a function.
# Using max is not "creating a function" because max is ALREADY a function.