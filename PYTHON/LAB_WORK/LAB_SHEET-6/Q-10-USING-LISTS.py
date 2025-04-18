# Write a Python program that prompts the user to enter 10 numbers as input and then finds and displays the maximum and minimum numbers among those entered. 

number_list = []

for i in range(1, 11):
    number = int(input(f"Enter your {i} number here: "))
    number_list.append(number)

max_number = max(number_list)
min_number = min(number_list)

print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")