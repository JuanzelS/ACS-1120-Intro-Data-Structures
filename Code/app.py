import cleanup
import tokens
import word_count
import sample
import sentence

from flask import Flask

app = Flask(__name__)

# Initialize word histogram (or Markov chain) here
words_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
histogram = word_count.build_histogram(words_list)  # Example: Build histogram from sample words

@app.route("/")
def home():
    """Route that returns a randomly generated word based on frequency weighting."""
    random_word = sample.weighted_random_word(histogram)  # Get a weighted random word
    return f"<p>Random Word: {random_word}</p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal."""
    app.run(debug=True)
