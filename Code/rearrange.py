import random
import sys

def rearrange_words(words):
    random.shuffle(words)  # Shuffle the list in place
    return " ".join(words)  # Convert the list back to a string

if __name__ == "__main__":
    if len(sys.argv) > 1:
        words = sys.argv[1:]  # Get command-line arguments (excluding script name)
        print(rearrange_words(words))
    else:
        print("Usage: python3 rearrange.py <words to shuffle>")
