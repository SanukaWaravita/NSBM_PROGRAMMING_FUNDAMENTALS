# Write a Python program to calculate nth power of a given integer. The user input base and exponent. (Do NOT use inbuilt functions, instead use a loop) 

base = int(input("Type the base number here: "))
exponent = int(input("Type the exponent number here: "))

result = 1

for i in range (exponent):
    result *= base

print(f"{base} raised to the power of {exponent} is: {result}")