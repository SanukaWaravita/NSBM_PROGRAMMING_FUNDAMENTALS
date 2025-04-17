# With return type, no parameters

# Example 1 - Create a function which inputs two numbers and *returns* the average.
# Means the input must occur within the function.

# Function creation
def FindAverage ():
    n1 = int(input("Enter First number: "))
    n2 = int(input("Enter Second number: "))
    avg = (n1 + n2)/2
    return avg

# Function calling
print(f"The average is {FindAverage()}")

# Functions with 'return' type must be called within "print()"