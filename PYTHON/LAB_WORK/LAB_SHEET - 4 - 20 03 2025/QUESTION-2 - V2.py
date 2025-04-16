<<<<<<< HEAD
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("A for Addition")
print("S for Substraction")
print("M for Multiplication")
print("D for Division")

opr = input("Enter Operation: ")

if opr == "A":
    ans = num1 + num2
elif opr == "S":
    ans = num1 - num2
elif opr == "M":
    ans = num1 * num2
elif opr == "D":
    ans = num1 / num2

=======
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("A for Addition")
print("S for Substraction")
print("M for Multiplication")
print("D for Division")

opr = input("Enter Operation: ")

if opr == "A":
    ans = num1 + num2
elif opr == "S":
    ans = num1 - num2
elif opr == "M":
    ans = num1 * num2
elif opr == "D":
    ans = num1 / num2

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print("The answer is: ", ans)