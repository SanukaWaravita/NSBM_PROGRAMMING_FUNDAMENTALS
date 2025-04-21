# Example 2 (Question 1) - Create the following two functions:
# 1. A function to input name and display the name.
# 2. A function to input birth year and display the age.

# After creating the functions call the functions

# Function1
def inputname():
    name = input("Enter you name here: ")
    print(f"The name you entered is: {name}")

# Function2
def inputAge():
    y = int(input("Enter Birth Year: "))
    age = 2025 - y
    print(f"You are {age} years old")

# Call the functions
inputname()
inputAge()