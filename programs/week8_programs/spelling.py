import sys
def load_dictionary():
    return set([
        "fundamental", "computer", "programming", "task", "week", 
        "this", "is", "a", "simple", "spell", "checker", "test",
        "it", "can", "find", "misspelled", "words"
    ])
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()  
            return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def find_misspelled_words(words, dictionary):
    misspelled = []
    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word)).lower()  
        if cleaned_word and cleaned_word not in dictionary:
            misspelled.append(cleaned_word)
    return misspelled

def print_misspelled_words(misspelled_words):
    for word in misspelled_words:
        print(word)

def main():
    if len(sys.argv) != 2:
        print("Usage: python spell.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    dictionary = load_dictionary()
    words = read_file(filename)
    misspelled_words = find_misspelled_words(words, dictionary)
    print_misspelled_words(misspelled_words)

if __name__ == "__main__":
    main()
