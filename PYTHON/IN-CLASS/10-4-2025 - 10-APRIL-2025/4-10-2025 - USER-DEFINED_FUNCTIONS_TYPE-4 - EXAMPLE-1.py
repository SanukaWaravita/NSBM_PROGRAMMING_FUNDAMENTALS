# With return type, with parameters

# Example 1 - Create a function which accepts 3 integers as *parameters* and *return* the average value.

# function
def findAvg (p, q, r):
    avg = (p + q + r) / 3
    return avg

# call the function

n1 = int(input("Enter your first number here: "))
n2 = int(input("Enter your second number here: "))
n3 = int(input("Enter your third number here: "))
print("The average is ", findAvg (n1, n2, n3))