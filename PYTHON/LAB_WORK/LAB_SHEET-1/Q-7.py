#  Input two numbers, swap the values and display the output. (Before swap and after swap)

# Inputing two numbers
x = int(input("Enter first number: "))
y = int(input("Enter 2nd number: "))

# Printing the values before swapping
print("before Swap X:- ",x)
print("before Swap Y:- ",y)

# Swapping the values
temp = x
x = y
y = temp

# Printing the values after swapping
print("after swap X:-",x)
print("after swap Y:-",y)