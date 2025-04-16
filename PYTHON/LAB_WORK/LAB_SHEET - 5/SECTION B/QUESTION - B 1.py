<<<<<<< HEAD
# Input 10 numbers and output the number of positive, number of negative, number of zeros. 

positive = 0
negative = 0
zero = 0
count = 0

for i in range (1, 11):
    number = int(input(f"Enter {count+1} your number here: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    elif number == 0:
        zero += 1
    count = i

print(f"Number of positive numbers that was entered is: {positive}")
print(f"Number of negative numbers that was entered is: {negative}")
=======
# Input 10 numbers and output the number of positive, number of negative, number of zeros. 

positive = 0
negative = 0
zero = 0
count = 0

for i in range (1, 11):
    number = int(input(f"Enter {count+1} your number here: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    elif number == 0:
        zero += 1
    count = i

print(f"Number of positive numbers that was entered is: {positive}")
print(f"Number of negative numbers that was entered is: {negative}")
>>>>>>> 02db6b354abde10cbddf6f0eafab50bf70906f64
print(f"Number of p numbers that was entered is: {zero}")