# Write a function that will read 2 numbers and calculate and display sum and difference.

def findSumAndDifference():
    num1 = int(input("Enter your 1st number here: "))
    num2 = int(input("Enter your 2nd number here: "))
    
    sum = num1 + num2
    difference = num1 - num2
    
    print(f"The sum of the 2 numbers is: {sum}")
    print(f"The difference of the 2 numbers is: {difference}")

findSumAndDifference()