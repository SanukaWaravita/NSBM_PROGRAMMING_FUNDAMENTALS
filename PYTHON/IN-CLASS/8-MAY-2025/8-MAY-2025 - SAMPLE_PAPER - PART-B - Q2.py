# Create a function that accepts three nummbers as parameters and returns the highest number.
# After creating the function, input three numbers and call the function.

def highnum(num1, num2, num3):
    
    highestnum = num1

    if num2 > highestnum:
        highestnum = num2
    if num3 > highestnum:
        highestnum = num3
    
    return(highestnum)


no1 = int(input("Enter your first number here: "))
no2 = int(input("Enter your second number here: "))
no3 = int(input("Enter your third number here: "))



print(f"The highest number of the three is: {highnum(no1, no2, no3)}")