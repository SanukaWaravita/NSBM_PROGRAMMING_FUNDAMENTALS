# Appending to a text file

# Write a program to add new text to an existing file.

# Writing data to a text file
def write_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content written to {file_path}")

# Call the function
write_file("28-04-2025 - WORKING_WITH_FILES - Sample.text", " is good")