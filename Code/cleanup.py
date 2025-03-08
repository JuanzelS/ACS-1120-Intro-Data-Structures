import re
import html

# Function to clean the text
def clean_text(text):
    # Step 1: Convert HTML character codes to their ASCII equivalents
    text = html.unescape(text)
    
    # Step 2: Normalize punctuation
    text = text.replace("‘", "'").replace("’", "'")  # Convert curly single quotes to straight quotes
    text = text.replace("“", '"').replace("”", '"')  # Convert curly double quotes to straight quotes
    
    # Step 3: Remove unwanted characters (like underscores, stars, etc.)
    text = re.sub(r'[_*]', '', text)  # Remove underscores and stars
    
    # Step 4: Optionally, remove other unwanted characters
    unwanted_chars = ['§', '©', '®']  # Add more characters to remove if necessary
    for char in unwanted_chars:
        text = text.replace(char, '')
    
    # Return cleaned-up text
    return text

# Example usage
if __name__ == '__main__':
    # Open the corpus file
    with open('corpus.txt', 'r') as file:
        corpus = file.read()

    # Clean the corpus
    cleaned_corpus = clean_text(corpus)

    # Save the cleaned corpus to a new file
    with open('cleaned_corpus.txt', 'w') as file:
        file.write(cleaned_corpus)
    
    print("Corpus cleaned and saved as cleaned_corpus.txt")
