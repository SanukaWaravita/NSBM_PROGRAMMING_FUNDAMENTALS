<<<<<<< HEAD
# Write a Python program to calculate nth power of a given integer. The user input base and exponent. (Do NOT use inbuilt functions, instead use a loop) 

base = int(input("Type the base number here: "))
exponent = int(input("Type the exponent number here: "))

result = 1

for i in range (exponent):
    result *= base

=======
# Write a Python program to calculate nth power of a given integer. The user input base and exponent. (Do NOT use inbuilt functions, instead use a loop) 

base = int(input("Type the base number here: "))
exponent = int(input("Type the exponent number here: "))

result = 1

for i in range (exponent):
    result *= base

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print(f"{base} raised to the power of {exponent} is: {result}")