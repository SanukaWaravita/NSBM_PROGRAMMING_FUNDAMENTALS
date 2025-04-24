# 2D List
a = [[1, 3, 5, 7], [2, 4, 6, 8], [10, 20, 30, 40]]
print(a)

# Display the values in rows

for record in a: 
    print(record)

# access and display the values of each element
for r in range(len(a)): # no. of rows
    for c in range(len(a[r])): # no. of columns
        print(a[r][c], end=" ")
    print()