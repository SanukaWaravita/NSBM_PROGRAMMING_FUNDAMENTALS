# Input values to list 1 and list 2

# Add the related elements and store them in list 3

# Display the values of the list 3

list1 = []
list2 = []
list3 = []


for i in range(5):
    num1 = int(input(f"Enter number {1+i}: "))
    list1.append(num1)

for i in range(5):
    num2 = int(input(f"Enter number {1+i}: "))
    list2.append(num2)

for i in range(5):
    list3.append(list1[i] + list2[i])

print(list1)
print(list2)
print(f"The resulting list (list 3) is: {list3}")