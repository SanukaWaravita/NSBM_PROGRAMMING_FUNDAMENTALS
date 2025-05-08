# Write a program that asks the user to input ten numbers and checks whether they are positive, negative, or zero, outputting the COUNT of positives, negatives, and zeros.

positive_count = 0
negative_count = 0
zero_count = 0
count = 0

for i in range(1, 11):
    no = int(input(f"Write you {count + 1} number here: "))
    if no > 0:
        positive_count += 1
    elif no < 0:
        negative_count += 1
    else:
        zero_count += 1
    
    count += 1

print(f"Positive no. count = {positive_count}")
print(f"Negative no. count = {negative_count}")
print(f"Zero no. count = {zero_count}")