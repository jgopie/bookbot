from typing import Dict
def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    print_report(text, path_to_book)

def get_book_text(book_path):
    file = open(book_path, "r")
    return file.read()

def count_words(text):
    return len(text.split())

def count_characters(text: str) -> Dict[str, int]:
    cache = {}
    for i in range(0, len(text)):
        current_character = text[i].lower()
        if current_character.isalpha():
            if current_character in cache.keys():
                cache[current_character] += 1
            else:
                cache[current_character] = 1
    return cache

def print_report(text: str, path: str):
    print(f"--- Begin report of {path} ---")
    word_count = count_words(text)
    print(f"{word_count} words found in document\n\n")
    char_count = count_characters(text)
    for key, value in char_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End Report ---")

main()