# Write a function that accepts 2 whole numbers as parameters and calculate and return the quotient.

def findQuotient(a, b):
    
    quotient = a // b
    return(quotient)

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter your 2nd number here: "))

print(f"The product of the two numbers is: {findQuotient(num1, num2)}")