import re
import sys

def tokenize(text):
    # Step 1: Remove unwanted punctuation
    no_punc_text = remove_punctuation(text)
    
    # Step 2: Split the cleaned text by whitespace
    tokens = split_on_whitespace(no_punc_text)
    
    return tokens

def remove_punctuation(text):
    # Remove common punctuation marks
    no_punc_text = re.sub('[,.()!"?;:]', '', text)
    
    # Replace double dashes with a single space (for cases like 'twentieth--March')
    no_punc_text = re.sub('--', ' ', no_punc_text)
    
    return no_punc_text

def split_on_whitespace(text):
    # Split the text by any sequence of whitespace characters
    return re.split(r'\s+', text)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Read the file provided as the command line argument
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            source = file.read()
        
        # Tokenize the text from the file
        tokens = tokenize(source)
        
        # Print the tokens
        print(tokens)
    else:
        print('No source text filename given as argument')
