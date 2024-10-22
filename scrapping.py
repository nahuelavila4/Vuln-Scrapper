import requests, re
from bs4 import BeautifulSoup

url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&search_type=all&isCpeNameSearch=false"

def scrapp1():
    r = requests.get(url)
    if r.status_code == 200:
        print("Security Vulnerabilities")
        soup = BeautifulSoup(r.text, "html.parser")
        
        vulns = soup.find("tbody")
        with open("output233.txt", "w") as file:
            for item in vulns:

                plain_text = item.get_text()
                file.write(plain_text)
        print("El archivo de salida se ha guardado correctamente")
    else:
        print(f"Error: {r.status_code}")

if __name__ == "__main__":
    scrapp1()