# Write a Python program that prompts the user to enter 10 numbers as input and then finds and displays the maximum and minimum numbers among those entered. 

# Prompt the user to enter the first number to initialize max and min
number = float(input("Enter number 1: "))  # Convert input to float
max_number = number  # Set initial max to the first entered number
min_number = number  # Set initial min to the first entered number

# Prompt the user to enter the remaining 9 numbers
for i in range(1, 10):
    number = float(input(f"Enter number {i+1}: "))  # Convert input to float
    
    # Update max and min numbers based on the current input
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

# Display the results
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")