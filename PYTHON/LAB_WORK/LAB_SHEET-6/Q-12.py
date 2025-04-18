# Write a Python program that prompts the user to enter a password and checks its strength based on its length under the below criteria. 
# •	If the password has 8 or more than 8 characters, it is considered strong.
# •	If the password has less than 8 characters, it is considered weak.
# If the password is weak, prompt the user to re-enter another password. If the password is strong, display 'New Password accepted'. The program should continue prompting the user until the entered password is accepted. 

while True:

    new_password = input("Enter your new password here: ")

    password_length = len(new_password)

    if password_length >= 8:
        break
    else:
        print(f"Your password is weak. Please re-enter new Password")

print("New Password accepted!")