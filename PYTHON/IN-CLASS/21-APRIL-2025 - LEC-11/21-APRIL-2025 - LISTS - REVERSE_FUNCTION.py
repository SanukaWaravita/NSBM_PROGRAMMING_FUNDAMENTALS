# reverse function for lists

list1 = [85, 78, 96, 46, 72]
list1.reverse()

print(f"{list1}")

m = 0
for i in range(5):
    if (list1[i] > m):
        m = list1[i]
print("The highest is ", m)