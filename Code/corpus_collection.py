import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = 'your_diffbot_dev_token'  # Replace this with your actual Diffbot API token

def get_article(article_url):
    # Set request params for the API request
    params = {
        'token': DIFFBOT_DEV_TOKEN,
        'url': article_url,
        'discussion': 'false'
    }

    # Hit the Diffbot API
    try:
        res = requests.get(DIFFBOT_API_URL, params=params)  # Corrected way of passing params
        res.raise_for_status()  # Raises an HTTPError if the status code is 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article: {e}")
        return None
    
    try:
        # Parse the response object
        res_obj = res.json()
        
        # Debugging: print the entire response to see its structure
        print("Response from Diffbot:", res_obj)

        # Check if 'objects' exists in the response
        if 'objects' in res_obj:
            return res_obj['objects'][0]['text']  # Pull out the text
        else:
            print("No 'objects' field in the response.")
            return None
    except Exception as e:
        print(f"Error parsing response: {e}")
        print(res.text)  # Print the response for debugging
        return None

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Marvel_Rivals'  # Your target URL
    article = get_article(url)

    if article:
        # Save the article text to a file
        with open('marvel_rivals_corpus.txt', 'w') as output_file:
            output_file.write(article)
        print('Corpus saved to marvel_rivals_corpus.txt')
    else:
        print("Failed to fetch article.")