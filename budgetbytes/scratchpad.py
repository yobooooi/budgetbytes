import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.budgetbytes.com/creamy-cucumber-salad/"

# Send a GET request to the webpage
headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links with 'category' in the URL
category_links = soup.find_all('a', {'rel' : 'tag'})

# Extract the href attribute values from the links
# links = [link['href'] for link in category_links]
links = [link.get_text(strip=True) for link in category_links]
# Print the results
for link in links:
    print(link)
