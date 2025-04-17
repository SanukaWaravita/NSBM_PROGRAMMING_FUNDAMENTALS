# Write a program to add all user inputs until user input '-1'. And then display the sum.

total = 0

while True: 

    num = int(input("Enter a number here (-1 to stop): "))

    if num == -1: 
        break

    total += num

print(f"The total sum is {total}")