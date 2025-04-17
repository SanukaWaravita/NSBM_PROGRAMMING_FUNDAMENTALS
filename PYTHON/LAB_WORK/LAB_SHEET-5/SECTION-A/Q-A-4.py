# Write a Python program to calculate the sum of all digits of a user given number. If user input 123 your program should output 6. (calculated as 1+2+3) 

total = 0
count = 0

while count < 3:
    unum = int(input("Type your number here: "))
    total += unum
    count += 1

print(f"The sum of all three digits is: {total}")