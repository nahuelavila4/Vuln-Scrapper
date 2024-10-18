import requests, re
from bs4 import BeautifulSoup

url = "https://owasp.org/www-project-top-ten/"

r = requests.get(url)

def scrapp1():
    if r.status_code == 200:
        print("Vulnerabilities Titles")
        soup = BeautifulSoup(r.text, "html.parser")
        titles = soup.find_all("a", href=True)
        filtered_titles = [link for link in titles if "https://owasp.org/Top10/A" in link['href']]

        for t in filtered_titles:
            print(t.text)
    else:
        print(f"Error: {r.status_code}")

if __name__ == "__main__":
    scrapp1()