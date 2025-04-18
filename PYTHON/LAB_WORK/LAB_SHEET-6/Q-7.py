# You have intercepted a coded password that has been secretly encoded using ASCII values. Your task is to decode the password by converting each character separately to its corresponding ASCII value and appending those values together to find the correct password. 
# The encoded password is: 'K8$%j' 
# Write a Python program to decode the password by determining the ASCII value of each character in the encoded password and then appending them together to display the correct password. 
# (Hint: For example, if the encoded password is 'AB', and the ASCII values of 'A' and 'B' are 65 and 66 respectively, the correct password would be '6566'). 

encoded = "K8$%j"
decoded = ""

for char in encoded:
    decoded += str(ord(char))

print(f"The decoded password is: {decoded}")