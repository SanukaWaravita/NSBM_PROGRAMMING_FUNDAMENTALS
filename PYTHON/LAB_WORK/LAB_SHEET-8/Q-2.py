# Write a program that inputs a series of integers and passes them one at a time to function even, which uses the remainder operator to determine if an integer is even. 
# The function should take an integer argument and return 1 if the integer is even and 0 otherwise. 

def even(num):
    if num % 2 == 0:
        return (1)
    else:
        return (0)

intcount = int(input("How many integers are you going to add: "))

for i in range (intcount):
    num = int(input(f"Enter your {i+1} number here: "))
    if even(num) == 1:
        print(f"The returned value is {even(num)}, therefore the integer you entered is even.")
    else:
        print(f"The returned value is {even(num)}, therefore the integer you entered is odd.")