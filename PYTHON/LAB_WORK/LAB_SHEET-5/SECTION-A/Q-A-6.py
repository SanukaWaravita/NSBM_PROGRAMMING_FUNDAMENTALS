<<<<<<< HEAD
# Write a Python program to print first 10 numbers of “Fibonacci Sequence”.
# Initialize first two numbers of Fibonacci sequence
first = 0
second = 1

print("The first 10 numbers of the Fibonacci sequence is: ")
print(first, end = "")
print(second, end = "")

for i in range (8):
    next_num = first + second
    print(next_num, end = "")
    first = second
    second = next_num

=======
# Write a Python program to print first 10 numbers of “Fibonacci Sequence”.
# Initialize first two numbers of Fibonacci sequence
first = 0
second = 1

print("The first 10 numbers of the Fibonacci sequence is: ")
print(first, end = "")
print(second, end = "")

for i in range (8):
    next_num = first + second
    print(next_num, end = "")
    first = second
    second = next_num

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print()