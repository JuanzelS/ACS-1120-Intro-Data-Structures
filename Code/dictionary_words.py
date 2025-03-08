import random
import sys

def load_words(filepath="/usr/share/dict/words"):
    """Reads the words file and returns a list of words."""
    try:
        with open(filepath, "r") as file:
            words = [line.strip() for line in file.readlines()]
        return words
    except FileNotFoundError:
        print("Error: Words file not found.")
        sys.exit(1)

def generate_sentence(word_count, words):
    """Generates a random sentence with the given number of words."""
    selected_words = random.sample(words, word_count)
    return " ".join(selected_words) + "."

def main():
    """Main function to handle user input and generate a sentence."""
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
        word_count = int(sys.argv[1])
        if word_count <= 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        sys.exit(1)
    
    words = load_words()
    sentence = generate_sentence(word_count, words)
    print(sentence)

if __name__ == "__main__":
    main()