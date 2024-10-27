import requests, re, savesql
from savesql import save_sql
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&search_type=all&isCpeNameSearch=false"

def scrapp1():
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")      
        vulns = soup.find_all("tr", attrs={"data-testid": True})

        with open("output2B.txt", "w") as file:
            #file.write("National Vulnerability Database")
            for item in vulns:
                versions = item.find_all("td", attrs={"nowrap": "nowrap"})
                for v in versions:    
                    v.extract()

                # Obtener ID
                id_vuln = item.find("a").get_text().strip()
                descrip_vuln = item.find("p").get_text().strip()
                # Obtener fecha - convertir luego con datetime
                date_vuln = item.find("span").get_text().strip()
                plain_text = item.get_text()
                #save_sql(id_vuln, descrip_vuln, date_vuln)
                #file.write(plain_text)

                # Formato fecha date_vuln October 26, 2024; 6:15:10 AM -0400
                date_vuln = date_vuln[:-6]
                date_time_obj = datetime.strptime(date_vuln, "%B %d, %Y; %I:%M:%S %p")
                formated_date = date_time_obj.strftime("%m/%d/%Y %H:%M:%S")
                print(type(formated_date))
                print(formated_date)
        print("El archivo de salida se ha guardado correctamente")
    else:
        print(f"Error al extraer: {r.status_code}")

if __name__ == "__main__":
    #save_sql()
    scrapp1()