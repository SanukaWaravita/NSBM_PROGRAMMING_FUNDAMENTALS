def smallest(a, b, c):
    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b
    else:
        smallest = c
    
    print(f"The smallest number is: {smallest}")

floatno1 = float(input("Enter a float number here: "))
floatno2 = float(input("Enter a float number here: "))
floatno3 = float(input("Enter a float number here: "))

smallest(floatno1, floatno2, floatno3)