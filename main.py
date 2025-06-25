from stats import get_word_count, count_characters, sort_characters
import sys

#main function
def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_word_count(book)
    characters_list = count_characters(book)
    sorted_characters = sort_characters(characters_list)
    print_report(book_path, num_words, sorted_characters)

# get book text function
# accepts file path as input and returns file contents as string
def get_book_text(path):
    with open(path) as book:
        return book.read()

#print report function, accepts a file path, integer, and then list of dictionaries
def print_report(book_path, num_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for character in sorted_characters:
        print(f"{character["char"]}: {character["num"]}")

    print("============= END ===============")

#call main function
main()
