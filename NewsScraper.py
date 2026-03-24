import requests
from bs4 import BeautifulSoup

# 1. The Target URL
url = "https://www.bbc.com/news"

# 2. The Request (Just like our API!)
response = requests.get(url)

# 3. The "Soup" (This turns the HTML into a searchable object)
soup = BeautifulSoup(response.text, "html.parser")

# 4. Finding the Headlines
# Most news sites use <h2> or <h3> tags for headlines
headlines = soup.find_all('h2')

print(f"🔥 TOP HEADLINES FROM {url}:\n")

for i, headline in enumerate(headlines[:10], 1):
    # .get_text() strips away the HTML tags and gives us just the words
    print(f"{i}. {headline.get_text().strip()}")