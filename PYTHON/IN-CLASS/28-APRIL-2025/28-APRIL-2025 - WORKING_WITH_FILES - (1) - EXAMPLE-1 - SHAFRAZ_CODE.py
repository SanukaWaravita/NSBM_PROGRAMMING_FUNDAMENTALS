# Working with files
# (1)
# Example - 1

# Writing data to a text file
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")

# Call the function
write_file("28-04-2025 - WORKING_WITH_FILES - Sample.text", "Batch 25.1 Group B")