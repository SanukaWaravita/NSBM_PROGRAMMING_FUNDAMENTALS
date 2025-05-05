# Working with files
# (2)
# Example - 1

# Reading data to a text file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The {file_path} does not exist")

# Calling the function
read_file("28-04-2025 - WORKING_WITH_FILES - Sample.text")