import sys
from stats import get_num_words, char_sort, char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char=char_count(text)
    char_sorted = char_sort(num_char)
    print_report(book_path,num_words, char_sorted)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, char_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()
