# Write a function that accepts 2 whole numbers as parameters and calculate and return the product.

def findProduct(a, b):
    
    return(a * b)

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter your 2nd number here: "))

print(f"The product of the two numbers is: {findProduct(num1, num2)}")