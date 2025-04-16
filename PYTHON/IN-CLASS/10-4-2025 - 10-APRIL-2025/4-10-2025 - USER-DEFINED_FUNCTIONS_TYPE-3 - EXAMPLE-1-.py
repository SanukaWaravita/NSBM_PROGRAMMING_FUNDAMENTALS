<<<<<<< HEAD
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

=======
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

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
# Functions with 'return' type must be called within "print()"