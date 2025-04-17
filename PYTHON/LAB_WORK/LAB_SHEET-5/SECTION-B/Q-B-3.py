# Input price of 10 items and display the average value of an Item, number of items which the price is greater than 200.

prices = []
count = 0

print("Enter the price of 10 items:")
for i in range (1, 10):
    itemprice = float(input(f"Enter item {count + 1}: "))
    prices.append(itemprice)
    count = i

total = 0
items_above_200 = 0

for itemprice in prices:
    total += itemprice
    if itemprice > 200:
        items_above_200 += 1

average = total / 10

print(f"The average price of the items: {average}")
print(f"The number of items above 200 is: {items_above_200}")