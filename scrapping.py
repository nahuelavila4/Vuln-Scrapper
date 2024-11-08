import requests, re, savesql
from savesql import insert_vuln
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&search_type=all&isCpeNameSearch=false"

def scrapp1():
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")      
        vulns = soup.find_all("tr", attrs={"data-testid": True})

        with open("output.txt", "w") as file:
            #file.write("National Vulnerability Database")
            for item in vulns:
                # Find and remove version
                versions = item.find_all("td", attrs={"nowrap": "nowrap"})
                for v in versions:    
                    v.extract()

                # Obtein ID, descrip y fecha
                id_vuln = item.find("a").get_text().strip()
                descrip_vuln = item.find("p").get_text().strip()
                date_vuln = item.find("span").get_text().strip()
                
                plain_text = item.get_text()
                file.write(plain_text)

                # Delete AM/PM
                date_vuln = date_vuln[:-6]
                date_time_obj = datetime.strptime(date_vuln, "%B %d, %Y; %I:%M:%S %p")
                formated_date = date_time_obj.strftime("%m/%d/%Y %H:%M:%S")

                conn = sqlite3.connect("scraper.db")
                insert_vuln(id_vuln, descrip_vuln, formated_date)
                conn.close()
        print("El archivo de salida se ha guardado correctamente")
    else:
        print(f"Error al extraer: {r.status_code}")

if __name__ == "__main__":
    scrapp1()