# Write a function which accepts an integer and a float value as parameters and return the product as a float value. Display the result from the main function.

def FindProduct(a, b):
    product = a * b
    return(product)

def main():
    integer_value = 5
    float_value = 6.7

    print("Calling function to print the product of two numbers")
    print(f"The product of the two numbers is: {float(FindProduct(integer_value, float_value))}")

main()