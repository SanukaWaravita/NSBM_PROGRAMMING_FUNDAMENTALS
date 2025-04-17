#Example 3: Write a program to input an item number, description, price, quantitiy and display item number, description with total price.
itemno = int(input("Type the item number here:"))
itemdes = input("Type the item description here:")
itemprice = float(input("Type the item price here:"))
itemquantity = int(input("Type the item quantity here:"))

totalprice = itemprice * itemquantity

#print("The total price is:", totalprice)
print(f"The total price is: {totalprice}")