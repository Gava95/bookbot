from stats import get_number_of_words
from stats import get_number_character_occurence
from stats import sorted_list
import sys


def get_book_text(filepath : str):
    # Open file
    with open(filepath) as file:
        # Retrieve the contents of thew file
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {file_path}...")
    
    print("----------- Word Count ----------")
    
    # Content of the book
    book_contents = get_book_text(file_path)
    # Number of words in the book
    print(get_number_of_words(book_contents))
    
    print("--------- Character Count -------")
    
    # Character in the book and their occurence number
    dict_character_ocurrences = get_number_character_occurence(book_contents)

    # Sort character by their decrease number of occurence
    result_sorted_list = sorted_list(dict_character_ocurrences)
    
    # Checking if the character is alphanumeric
    for i in range(len(result_sorted_list)):
        if result_sorted_list[i]['char'].isalpha() == True:
            # print the character and occurence in the format : "character:occurence"
            print(f"{result_sorted_list[i]['char']}: {result_sorted_list[i]['num']}")
    
    print("============= END ===============")

main()