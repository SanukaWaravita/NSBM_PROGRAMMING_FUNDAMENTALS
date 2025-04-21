# Declare the integer list and asign five numbers access the elements of the array and display the following. 
#   1. reverse order
#   2. The maximum value

# declare an integer array to store 5 values
integerList = []
reverseIntegerList = []

for i in range(5):
    integer = int(input(f"Enter your {i+1} number here: "))
    integerList.append(integer)

# display the values in reverse order
for x in range(-1, -(len(integerList))-1, -1):
    num = integerList[x]
    reverseIntegerList.append(num)

print(f"The reverse order of the list: {reverseIntegerList}")

# find and display the highest
maximum = 0

for i in range(len(integerList)):
    if (integerList[i] > maximum):
        maximum = integerList[i]

print(f"The maximum of the list is: {maximum}")