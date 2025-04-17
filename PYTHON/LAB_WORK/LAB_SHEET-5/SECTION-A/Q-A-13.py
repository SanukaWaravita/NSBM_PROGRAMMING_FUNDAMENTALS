# Write a program to read user inputs for an integer array (size = 10) and print the array. 

# Initialize an empty list to store the integers
integer_array = []

# Loop to get 10 integers from the user
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    integer_array.append(num)

# Print the array
print("The entered array is:", integer_array)