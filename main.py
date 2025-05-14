from stats import get_number_of_words
from stats import get_number_character_occurence

def get_book_text(filepath : str):
    # Open file
    with open(filepath) as file:
        # Retrieve the contents of thew file
        file_contents = file.read()
    return file_contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(get_number_of_words(book_contents))
    print(get_number_character_occurence(book_contents))
main()