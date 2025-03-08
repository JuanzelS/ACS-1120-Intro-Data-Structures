import random

class MarkovChain:
    def __init__(self):
        # Dictionary to hold the transitions from each word
        self.transitions = {}

    def learn(self, corpus):
        """Learn the Markov chain from the given corpus."""
        # We need to iterate over the corpus, and for each word, find its next word
        for i in range(len(corpus) - 1):
            word = corpus[i]
            next_word = corpus[i + 1]

            # If the word doesn't exist in the dictionary, add it with an empty dictionary
            if word not in self.transitions:
                self.transitions[word] = {}

            # Add or update the frequency of the next word
            if next_word not in self.transitions[word]:
                self.transitions[word][next_word] = 0
            self.transitions[word][next_word] += 1

    def get_next_word(self, word):
        """Return a word that can follow the given word based on the learned chain."""
        if word not in self.transitions:
            return None  # No transitions for this word
        
        # Get the possible next words and their frequencies
        next_words = self.transitions[word]
        total_count = sum(next_words.values())
        
        # Choose the next word based on the probabilities (randomly, weighted by frequency)
        rand_choice = random.randint(1, total_count)
        cumulative_count = 0

        for next_word, count in next_words.items():
            cumulative_count += count
            if rand_choice <= cumulative_count:
                return next_word
        return None

def generate_sentence(markov_chain, start_word, max_length=50):
    """Generate a random sentence using the learned Markov Chain."""
    sentence = [start_word]
    current_word = start_word

    while len(sentence) < max_length:
        next_word = markov_chain.get_next_word(current_word)
        if next_word is None:
            break  # End if we reach a word with no outgoing transition
        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence)

# Example usage:
if __name__ == "__main__":
    # Example corpus
    corpus = [
        'A', 'man', ',', 'a', 'plan', ',', 'a', 'canal:', 'Panama!',
        'A', 'dog', ',', 'a', 'panic', 'in', 'a', 'pagoda!'
    ]

    # Learn the Markov chain
    markov_chain = MarkovChain()
    markov_chain.learn(corpus)

    # Generate a sentence starting from the word 'A'
    generated_sentence = generate_sentence(markov_chain, 'A')
    print("Generated sentence:", generated_sentence)
