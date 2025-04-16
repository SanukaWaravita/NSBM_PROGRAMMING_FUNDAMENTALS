<<<<<<< HEAD
# Example 3
# Use the for loop and write a program to allow the user to input a number andd display the multiplication table of that number.

# User input
number = int(input("Type your preferred number here: "))

# Table generation

print(f"\nThe multiplication table for {number} is: ")
print()
for i in range (1, 13):
    result = number * i 
=======
# Example 3
# Use the for loop and write a program to allow the user to input a number andd display the multiplication table of that number.

# User input
number = int(input("Type your preferred number here: "))

# Table generation

print(f"\nThe multiplication table for {number} is: ")
print()
for i in range (1, 13):
    result = number * i 
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print(f"{number} × {i} = {result}")