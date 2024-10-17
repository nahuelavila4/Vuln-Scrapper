import requests
from bs4 import BeautifulSoup

url = "https://owasp.org/www-project-top-ten/"

r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html.parser")
    machines = soup.findAll("li", stronger = True)
    for machine in machines:
        print(machine)


