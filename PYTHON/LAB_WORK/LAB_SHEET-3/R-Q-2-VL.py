num1=int(input("Enter number 01: "))
num2=int(input("Enter number 02: "))
num3=int(input("Enter number 03: "))

largest=num1
smallest=num1

if (num2>largest):
    largest=num2

elif (largest<num3):
    largest=num3

if (num2<smallest):
    smallest=num2

elif (num2<smallest):
    smallest=num3

print("Smallest number is", smallest)
print("Largest number is ", largest)