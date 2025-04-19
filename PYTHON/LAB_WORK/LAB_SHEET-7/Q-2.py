# Write a function that accepts 2 numbers as parameters and calculate and display sum and difference.

def findSumAndDifference(a, b):
    sum = a + b
    difference = a - b
    
    print(f"The sum of the 2 numbers is: {sum}")
    print(f"The difference of the 2 numbers is: {difference}")

num1 = int(input("Enter your 1st number here: "))
num2 = int(input("Enter your 2nd number here: "))

findSumAndDifference(num1, num2)