from bs4 import BeautifulSoup
import requests

def scraper(website): #scraper function
    HEADERS = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",  # < 0.5 instead?
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_57_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    while True:
        if website is None:
            website = input("Please enter the website URL: ").strip()

        if not website.startswith("http://") and not website.startswith("https://"):
            website = "https://" + website

        try:
            response = requests.get(website, headers=HEADERS, timeout=10)

        # check response statement
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                print("\n=== Web Page Text Start ===\n")
                print(soup.text)
                print("\n=== Web Page Text End ===\n")
                break
            else:
                print(f"Failed to retrieve {website}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error retrieving {website}: {e}")

        retry = input("Try another URL? (y/n): ").lower()
        if retry != "y":
            break
        website = None
