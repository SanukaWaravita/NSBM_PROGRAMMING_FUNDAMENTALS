# Write a function that accepts 2 numbers as parameters and calculate and display sum and difference.

def displaySumAndDiff(a, b):
    
    print(f"The sum of the 2 numbers is: {a + b}")
    print(f"The difference of the 2 numbers is: {a - b}")

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter your 2nd number here: "))

displaySumAndDiff(num1, num2)