import random
import sys

def load_words(file_path="/usr/share/dict/words"):
    """Read the words file and return a list of words."""
    try:
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: Words file not found.")
        sys.exit(1)

def generate_sentence(word_count, words):
    """Generate a sentence with the given number of random words."""
    sentence = " ".join(random.choices(words, k=word_count))
    return sentence + "."

def main():
    """Main function to parse input and generate a random sentence."""
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
        word_count = int(sys.argv[1])
        if word_count <= 0:
            raise ValueError
    except ValueError:
        print("Error: Please provide a positive integer for the number of words.")
        sys.exit(1)
    
    words = load_words()
    sentence = generate_sentence(word_count, words)
    print(sentence)

if __name__ == "__main__":
    main()
