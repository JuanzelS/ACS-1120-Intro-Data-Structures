import re
import sys
from collections import Counter

def read_file(filename):
    """Reads the text file and returns its contents as a string."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().lower()  # Convert to lowercase for uniformity

def clean_text(text):
    """Removes punctuation and splits text into words."""
    return re.findall(r'\b[a-zA-Z]+\b', text)  # Extract only words

def histogram(words):
    """Creates a histogram (word frequency dictionary) from a list of words."""
    return Counter(words)  # Uses Counter for efficiency

def unique_words(hist):
    """Returns the count of unique words in the histogram."""
    return len(hist)

def frequency(word, hist):
    """Returns the frequency of a specific word."""
    return hist.get(word, 0)

def most_frequent_words(hist, n=5):
    """Returns the n most frequent words."""
    return hist.most_common(n)

def least_frequent_words(hist, n=5):
    """Returns the n least frequent words."""
    return sorted(hist.items(), key=lambda item: item[1])[:n]

def average_word_frequency(hist):
    """Returns the mean, median, and mode of word frequency."""
    frequencies = list(hist.values())
    mean = sum(frequencies) / len(frequencies)

    frequencies.sort()
    mid = len(frequencies) // 2
    median = (frequencies[mid] if len(frequencies) % 2 != 0 
              else (frequencies[mid - 1] + frequencies[mid]) / 2)

    mode = Counter(frequencies).most_common(1)[0][0]

    return mean, median, mode

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 word_frequency.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    text = read_file(filename)
    words = clean_text(text)
    hist = histogram(words)

    print(f"Total unique words: {unique_words(hist)}")
    print(f"Most frequent words: {most_frequent_words(hist)}")
    print(f"Least frequent words: {least_frequent_words(hist)}")

    mean, median, mode = average_word_frequency(hist)
    print(f"Mean frequency: {mean:.2f}, Median frequency: {median}, Mode frequency: {mode}")

    test_word = "the"
    print(f"Frequency of '{test_word}': {frequency(test_word, hist)}")
