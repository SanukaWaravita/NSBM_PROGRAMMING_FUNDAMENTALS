# Write a function that accepts 2 whole numbers as parameters and calculate and return the product.

def findProduct(a, b):
    
    return(a * b)

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter your 2nd number here: "))

product = findProduct(num1, num2)

print(f"The product of the two numbers is: {product}")