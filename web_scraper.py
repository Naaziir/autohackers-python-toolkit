import requests
from bs4 import BeautifulSoup

def scrape_bbc_headlines():
    url = "https://www.bbc.com/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = soup.find_all("h3")
    for h in headlines[:10]:
        print(h.text.strip())

if __name__ == "__main__":
    scrape_bbc_headlines()