# Example 2 (Question 1) (Variant 2) - Create a function which accept 2 integers and display the highest number.

#function
def FindMax(a,b):
    if (a > b):
        m = a
    else:
        m = b
    print(f"The highest number is: {m}")

# call the function

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
FindMax (n1, n2)