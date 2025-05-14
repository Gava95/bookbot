def get_book_text(filepath : str):
    # Open file
    with open(filepath) as file:
        # Retrieve the contents of thew file
        file_contents = file.read()
    return file_contents

def number_of_words(contents : str):
    # Delete the empty space of the string and evalute is length
    num_words = len(contents.split())
    return f"{num_words} words found in the document"


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    print(number_of_words(book_contents))

main()