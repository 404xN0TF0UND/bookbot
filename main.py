import sys
from stats import get_num_words, char_count, generate_char_report

def main():
    # Check if book path is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path from the command line
    file_path = sys.argv[1]

    try:
        # Read file and analyze
        word_count, file_contents = get_num_words(file_path)
        character_counts = char_count(file_contents)
        generate_char_report(character_counts, word_count, file_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


    # import sys
# from stats import get_num_words, char_count, generate_char_report

# def main():
#     with open("books/frankenstein.txt") as f:
#         file_contents = f.read()
#         words = file_contents.split()
#         # print (words)


# main()
# get_num_words
# char_count
# generate_char_report