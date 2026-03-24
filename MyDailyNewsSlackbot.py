import requests
from bs4 import BeautifulSoup

# 1. Your Slack Webhook from the Inventory Script
SLACK_WEBHOOK_URL = "XYZ"

# 2. Setup the Scrape
url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all('h2')

# 3. Define your "Professional Interest" Keywords
# Added 'Amazon' and 'Retail' for your specific role
keywords = ["Amazon", "Retail", "Tech", "AI", "Supply Chain", "Inventory", "Manchester United", "BMW", "Tesla", "Meta", "Google", "NVIDIA", "Netflix", "Autonomous", "Space", "Artemis", "Moon", "Stars", "Apple", "Health", "Car", "Digital"]

# ... (Keep your imports and Webhook URL) ...

# 1. Target the "Articles" instead of just headlines
# BBC often uses <a> tags with specific classes for their links
articles = soup.find_all('a', href=True)

# 2. Refined Loop
for article in articles:
    # Get the headline text
    headline_text = article.get_text().strip()
    
    # Get the link
    link = article['href']
    
    # BBC links are often "relative" (e.g., /news/world-123)
    # We need to turn them into "absolute" links (https://bbc.com/news/world-123)
    if link.startswith('/'):
        full_url = f"https://www.bbc.com{link}"
    else:
        full_url = link

    # 3. Use your "Smarter Filter" from before
    words_in_text = headline_text.lower().split()
    
    for key in keywords:
        if key.lower() in words_in_text:
            # Send to Slack with the link included!
            message = f"📰 *DAILY INTEL ALERT* 📰\n> *{headline_text}*\n🔗 <{full_url}|Read Full Story>"
            
            payload = {"text": message}
            requests.post(SLACK_WEBHOOK_URL, json=payload)
            print(f"🚀 Link Sent: {headline_text}")
            break