# Appending to a text file

# Write a program to add new text to an existing file.

# Writing data to a text file

def append_file(file_path, new_content):
    try:
        with open(file_path, 'a') as file:
            file.write(new_content)
            print(f"The content is appended to the {file_path}")
    except FileNotFoundError:
        print(f"The {file_path} does not exist")

# call the function
append_file("28-04-2025 - WORKING_WITH_FILES - Sample.text", "\n Python File Handling")