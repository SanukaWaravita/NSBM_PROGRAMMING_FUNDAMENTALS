#Example 2: Write a program that allows the user to input a name, birth year and display name with age.
name = input("Type your name here:")
yob = input("Type your year of birth here:")
age = int(2025) - int(yob)

#print("Your name is", name, "and you are", age, "years old!")
print(f"Hey {name} you are {age} years old!")