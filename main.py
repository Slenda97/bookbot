def main():
    word_count = None
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letters = alphabet()
    char_dict = {}
    for letter in letters:
        char_dict[letter] = character_count(letter, file_contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document \n")
    for letter in char_dict:
        print(f"The '{letter}' character was found {char_dict[letter]} times")
    print("--- End report ---")

def count_words(text):
    file_words = []
    file_words = text.split()
    final_count = len(file_words)
    return final_count

def character_count(character,text):
    
    lower_file_chars = text.lower()
    count = 0
    for char in lower_file_chars:
        if char == character:
            count += 1
    return count

def alphabet():
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_list = list(letters)
    return letters_list


main()