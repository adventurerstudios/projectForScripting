from bs4 import BeautifulSoup
import requests

def scraper(website):
    HEADERS = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",  # < 0.5 instead?
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_57_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    response = requests.get(website, headers=HEADERS)
    setup = BeautifulSoup(response.text, "html.parser")

    # check response statement
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.text)
    else:
        print(f"Failed to retrieve {website}. Status code: {response.status_code}")