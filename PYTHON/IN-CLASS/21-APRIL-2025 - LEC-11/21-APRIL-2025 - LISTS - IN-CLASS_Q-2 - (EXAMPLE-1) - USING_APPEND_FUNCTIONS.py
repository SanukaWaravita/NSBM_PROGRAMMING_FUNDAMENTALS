# Use the append function and write a program to input five integers into a list and display the values.

integerList = []

for i in range(5):
    integer = int(input(f"Enter your {i+1} number here: "))
    integerList.append(integer)

print(integerList)