# Write a program to allow the user to input 10 numbers and display the total number of odd, even numbers in the entered number series.

count = 0
odd_no_count = 0
even_no_count = 0

while count < 10: 
    number = float(input("Enter number " + str(count + 1) + ": "))
    if number % 2 == 0:
        even_no_count += 1
    else:
        odd_no_count += 1
    count += 1
    
print(f"No of Even numbers in the number series: {even_no_count}")
print(f"No of Odd numbers in the number series: {odd_no_count}")