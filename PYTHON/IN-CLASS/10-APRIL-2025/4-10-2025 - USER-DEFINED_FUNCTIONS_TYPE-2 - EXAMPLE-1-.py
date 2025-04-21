# No return type, with parameters

# Example 1 - Create a function which accepts 2 integers as parameters display the total.

# Function creation
def FindTotal(a, b):
    # "a" and "b" are called 'parameters'
    t = a + b
    print(f"The total is {t}")

# Function call
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
FindTotal (n1, n2)

#n1 goes to "a", n2 goes to "b"