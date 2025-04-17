# Write a program to allow the user the input 10 numbers and display the total number of positives, negatives and zeroes in the entered number series. 

count = 0
no_of_positive = 0
no_of_negative = 0
no_of_zero = 0

while count < 10: 
    number = float(input("Enter number " + str(count + 1) + ": "))
    if number > 0:
        no_of_positive += 1
    elif number < 0:
        no_of_negative += 1
    else:
        no_of_zero += 1
    count += 1
    
print(f"No of Positive numbers in the number series: {no_of_positive}")
print(f"No of Negative numbers in the number series: {no_of_negative}")
print(f"No of Zeroes in the number series: {no_of_zero}")