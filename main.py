def main():
    word_count = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print(word_count)

def count_words(text):
    file_words = []
    final_count = None
    file_words = text.split()
    final_count = len(file_words)
    return final_count

main()