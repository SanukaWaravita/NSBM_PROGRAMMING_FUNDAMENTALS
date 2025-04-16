<<<<<<< HEAD
# Write a program to check whether a given number is prime or not. 

# Get input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
=======
# Write a program to check whether a given number is prime or not. 

# Get input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
    print(num, "is not a prime number")