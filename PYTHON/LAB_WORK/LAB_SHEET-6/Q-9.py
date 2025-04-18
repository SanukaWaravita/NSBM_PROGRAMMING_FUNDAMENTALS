# Write a Python program that prompts the user to enter an email address and validates the email by checking whether it contains both '@' and '.' characters. Finally display whether the entered email address is valid or not. 

user_email = input("Enter your email address here: ")

at_validity = user_email.find("@")
dot_validity = user_email.find(".")

if at_validity != -1 and dot_validity != -1:
    print("The email address you entered is valid")
else:
    print("The email address you entered is invalid")