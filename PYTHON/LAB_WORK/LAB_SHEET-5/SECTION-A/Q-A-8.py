# Write a Python program to print all the ASCII values for letters A to Z. 

for letter in range(ord('A'), ord('Z') + 1):
    print(f"Letter: {chr(letter)}  ASCII: {letter}")