import requests
from bs4 import BeautifulSoup
import re

url = 'https://transcripts.foreverdreaming.org/viewtopic.php?t=88727&sid=adaf0e19cfcf4223206ee057b0ab7dba'

# Send a GET request to the URL
response = requests.get(url)

vocab_words = []

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <div> element containing the script
    div_element = soup.find('div', class_='content')

    # Check if the div element is found
    if div_element:
        # Extract the text of the div element
        script_text = div_element.get_text(separator='\n').strip()
        print(script_text)

        # Use regular expression to match words that are in quotations and add to a vocab list
        words = re.findall(r'"([^"]+)"', script_text)
        vocab_words.extend(words)

        # Use regular expression to find words that come after "a" or "an" and before "is"
        words = re.findall(r'(?:\ba\b|\ban\b) (\w+) is', script_text, re.IGNORECASE)
        vocab_words.extend(words)

    else:
        print("Div element not found on the page.")
else:
    print("Failed to retrieve the webpage.")
