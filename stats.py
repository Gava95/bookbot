def get_number_of_words(contents_file : str):
    # Delete the empty space of the string and evalute is length
    num_words = len(contents_file.split())

    return f"{num_words} words found in the document"


def get_number_character_occurence(contents_file : str):
    # Dictionnary with character and their number of occurence 
    character_occurrences = {}

    # put every character of the string in lower case
    characters = contents_file.lower()

    for character in characters:
        # If the character already exist in the dictionnary, incremment his count by 1.
        if (character in character_occurrences) == True:
            character_occurrences[character] += 1
        # If character doesn't exist in dictionnary, add it and initalise his count.
        else:
            character_occurrences[character] = 1
    
    return character_occurrences