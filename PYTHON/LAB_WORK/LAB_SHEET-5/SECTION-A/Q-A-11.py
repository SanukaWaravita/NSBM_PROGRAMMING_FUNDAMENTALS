# Write a program to print all factors of a given integer. 

integer = int(input("Type a number here: "))

print(f"Factors of {integer} are: ")

for i in range(1, integer+1):
    if integer % i == 0:
        print(i)