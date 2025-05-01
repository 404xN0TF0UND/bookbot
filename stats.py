def get_num_words(file_path: str) -> tuple:
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    return num_words, file_contents

def char_count(file_contents: str) -> dict:
    char_count_dict = {}
    for char in file_contents.lower():
        if char.isalpha():  # Only count letters
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict

def generate_char_report(char_counts: dict, word_count: int, file_path: str):
    # Sort character counts from greatest to least
    sorted_chars = sorted(
        [{'character': k, 'count': v} for k, v in char_counts.items()],
        key=lambda x: x['count'],
        reverse=True
    )

    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['character']}: {entry['count']}")
    print("============= END ===============")

# === Run the full program ===
file_path = "books/frankenstein.txt"
word_count, contents = get_num_words(file_path)
char_counts = char_count(contents)
generate_char_report(char_counts, word_count, file_path)


# def get_num_words():
#     with open("books/frankenstein.txt") as f:
#         file_contents = f.read()
#         words = file_contents.split()
#         num_words = len(words)
#         print (f"{num_words} words found in the document")
#         return file_contents

# def char_count(file_contents: str) -> dict:
#     char_count_dict = {}
#     for char in file_contents.lower():
#         if char in char_count_dict:
#             char_count_dict[char] += 1
#         else:
#             char_count_dict[char] = 1
#     return char_count_dict
    
# def gen_char_report(char_counts: dict) ->list:
#     # Covert to a list of dict
#     char_list = [{'character': char, 'count': count} for char, count in char_counts.items()]
#     # sort list
#     sorted_list = sorted(char_list, key=lambda x: x['count'], reverse =True)

#     print("Character Frequency Report:")
#     for entry in sorted_list:
#         print(f"{entry['character']!r}: {entry['count']}")
#     return sorted_list

# contents = get_num_words()
# char_count = char_count(contents)
# print(char_count)



# get_num_words()
