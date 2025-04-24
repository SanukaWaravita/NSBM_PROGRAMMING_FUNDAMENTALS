# Use 2 for loops and display the following pattern:
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 

a = [0, 1, 2, 3, 4]

for r in range(len(a)):
    for value in a: 
        print(value, end=" ")
    print()