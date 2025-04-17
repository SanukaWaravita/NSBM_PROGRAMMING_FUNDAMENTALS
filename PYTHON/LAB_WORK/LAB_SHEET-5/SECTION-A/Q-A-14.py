# Re-Write the above code to count all the even numbers in above integer array and display the count.

# Initialize an empty list to store the integers
integer_array = []

# Loop to get 10 integers from the user
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    integer_array.append(num)

# Count even numbers
even_count = 0
for num in integer_array:
    if num % 2 == 0:
        even_count += 1

# Print the array and even count
print("The entered array is:", integer_array)
print("Number of even integers in the array:", even_count)