<<<<<<< HEAD
# Write a program to print all factors of a given integer. 

integer = int(input("Type a number here: "))

print(f"Factors of {integer} are: ")

for i in range(1, integer+1):
    if integer % i == 0:
=======
# Write a program to print all factors of a given integer. 

integer = int(input("Type a number here: "))

print(f"Factors of {integer} are: ")

for i in range(1, integer+1):
    if integer % i == 0:
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
        print(i)