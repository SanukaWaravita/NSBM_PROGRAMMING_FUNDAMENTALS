# Write a function which accepts an integer and a float value as parameters and return the product as a float value. Display the result from the main function.

def get_product(num1, num2):
    return float(num1 * num2)

def main():
    int_value = 5
    float_value = 3.2

    result = get_product(int_value, float_value)
    print("The product is:", result)

main()