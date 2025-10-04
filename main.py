from stats import count_words, count_chars, sort_dicts
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    contents = get_book_text(path)
    num_of_words = count_words(contents)
    char_dict = count_chars(contents)
    sorted_dicts = sort_dicts(char_dict)
    print_report(path, num_of_words, sorted_dicts)

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in chars_sorted_list:
        if not i["char"].isalpha():
            continue
        print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")

main()

