# Example 3
# Use the for loop and write a program to allow the user to input a number andd display the multiplication table of that number.

# User input
number = int(input("Type your preferred number here: "))

# Table generation

print(f"\nThe multiplication table for {number} is: ")
print()
for i in range (1, 13):
    result = number * i 
    print(f"{number} × {i} = {result}")