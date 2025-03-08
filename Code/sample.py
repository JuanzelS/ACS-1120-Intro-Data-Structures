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

def weighted_random_word(histogram):
    """Returns a weighted random word based on frequency in histogram."""
    total_weight = sum(histogram.values())
    random_choice = random.randint(1, total_weight)
    
    cumulative_weight = 0
    for word, weight in histogram.items():
        cumulative_weight += weight
        if cumulative_weight >= random_choice:
            return word

if __name__ == "__main__":
    # Check if a filename or words were provided in the command line
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        words = get_words_from_file(filename)
    else:
        words = input("Enter words: ").split()
    
    print(random_word(words))
