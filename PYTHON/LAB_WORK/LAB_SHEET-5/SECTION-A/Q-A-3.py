# Get input from user
num = int(input("Enter a number to calculate factorial: "))

# Initialize variables
factorial = 1
i = num

# Handle special case for 0
if num == 0:
    print("Factorial of 0 is: 1")
else:
    # Calculate factorial using while loop
    while i >= 1:
        factorial = factorial * i
        i -= 1
    print(f"Factorial of {num} is: {factorial}")