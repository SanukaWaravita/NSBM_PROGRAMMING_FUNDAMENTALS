# Write a program using the nested for loop to display the following output:
# 12345
# 12345
# 12345
# 12345
# 12345

# Variant 1
for x in range(1, 6):
    for y in range (1, 6):
        print(y, end = "")
    print() 

# Variant 2 (Print statement keyword to add new line)
for x in range(1, 6):
    for y in range (1, 6):
        print(y, end = "")
    print("\n") 

# Variant 3 (Printing * instead of number)
for x in range(1, 6):
    for y in range (1, 6):
        print("*", end = "")
    print("\n") 