import sys
from stats import word_count, text_filter, dict_to_sorted_list
def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text
    
def main(): # This is good! No parameters for main.
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else: # <--- Problem 1: This line needs to be indented AND store the result!
            path = sys.argv[1]
            stored = get_book_text(path)
         
        total = word_count(stored)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {total} total words")
        print("--------- Character Count -------")

        char_counts = text_filter(stored)
        sorted_chars = dict_to_sorted_list(char_counts)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")


main()