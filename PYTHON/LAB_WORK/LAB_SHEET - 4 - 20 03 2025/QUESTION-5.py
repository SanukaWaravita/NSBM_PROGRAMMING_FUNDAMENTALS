<<<<<<< HEAD
# Write a Python program to enter month number and print total number of days in the month. First assume that the given month belongs to a non-leap year.

mninput = int(input("Enter the number of a month (1-12): "))

if mninput == 1 or mninput == 3 or mninput == 5 or mninput == 7 or mninput == 9 or mninput == 11:
    days = 31
elif mninput == 2:
    days = 28
else:
    days = 30

=======
# Write a Python program to enter month number and print total number of days in the month. First assume that the given month belongs to a non-leap year.

mninput = int(input("Enter the number of a month (1-12): "))

if mninput == 1 or mninput == 3 or mninput == 5 or mninput == 7 or mninput == 9 or mninput == 11:
    days = 31
elif mninput == 2:
    days = 28
else:
    days = 30

>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print(f"Month {mninput} has {days} days.")