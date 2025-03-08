import sys
import random

def get_words_from_file(filename):
    """Reads a file and returns a list of words."""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.split()  # Splits the text into a list of words

def random_word(words):
    """Returns a randomly selected word from the list."""
    return random.choice(words)

if __name__ == "__main__":
    # Check if a filename or words were provided in the command line
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        words = get_words_from_file(filename)
    else:
        words = input("Enter words: ").split()
    
    print(random_word(words))
