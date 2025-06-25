#get word count function
# accepts book text as input and returns total count of words.
def get_word_count(book):
    words_list = book.split()
    return len(words_list)

#count characters function
# accepts a string as input and returns a dictionary of each character and it's count'
def count_characters(book):
    character_count = {}
    for character in book.lower():
        if character.isalpha():
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1
    return character_count

#function to get key for sort function
def sort_on(character):
    return character["num"]

#get report function
# takes a dictionary and sorts by the key and returns sorted list of dictionaries
# function needs remade to return a list of dictionaries
def sort_characters(character_dict):
    characters_list = []
    for character in character_dict:
        characters_list.append({"char":character, "num": character_dict[character]})
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list
