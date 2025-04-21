# Decalre the integer list and asign five numbers access the elements of the array and display the following. 
#   1. reverse order
#   2. The maximum value

# declare an integer array to store 5 values
list1 = [85, 78, 96, 46, 72]

# display the values in reverse order
for i in range(4, -1, -1):
    print(list1[i])

# find and display the highest
m = 0
for i in range(5):
    if(list1[i]>m):
        m = list[i]
print("The highest is ", m)