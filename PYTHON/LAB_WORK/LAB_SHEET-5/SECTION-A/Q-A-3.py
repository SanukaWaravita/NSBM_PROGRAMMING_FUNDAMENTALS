<<<<<<< HEAD
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
=======
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
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print(f"Factorial of {num} is: {factorial}")