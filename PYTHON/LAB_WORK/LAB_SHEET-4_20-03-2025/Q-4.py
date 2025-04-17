# Write a Python program to read a character from the user and determine whether the given letter is vowel or not.

char = input("Type a character here: ")

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or \
    char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
    print("The character you entered is a vowel.")
else: 
    print("The character you entered is not a vowel.")