# Write a Python program that asks the user to enter a sentence and a search term. Find the index position of the first occurrence of the search term within the sentence. If the search term is found, display its index position. If the search term is not found, display 'Search term not found in the sentence’. 

sentence = input("Enter a sentence here: ")
search_term = input("Enter a search term here: ")

index = sentence.find(search_term)

if index != -1:
    print(f"The index position of your search term is: {index}")
else:
    print("Search term not found in the sentence")