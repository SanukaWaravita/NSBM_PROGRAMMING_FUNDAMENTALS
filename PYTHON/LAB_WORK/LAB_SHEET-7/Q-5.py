# Write a function to read 2 numbers and display the sum. Call this function from the main function several times.

def findSum():
    num1 = int(input("Enter your 1st number here: "))
    num2 = int(input("Enter your 2nd number here: "))

    sum = num1 + num2

    print(f"The sum of the 2 numbers you entered is: {sum}")

def main():
    print("First call: ")
    findSum()

    print("\nSecond call: ")
    findSum()

    print("\nThird call: ")
    findSum()

main()