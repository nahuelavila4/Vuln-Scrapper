import requests, re, savesql
#from savesql import * 
from bs4 import BeautifulSoup

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
                id_vuln = item.find("a", attrs={"data-testid": True})

                # Obtener descripcion


                # Obtener fecha



                #file.write(plain_text)
                plain_text = item.get_text()
                print(plain_text)
        print("El archivo de salida se ha guardado correctamente")
    else:
        print(f"Error al extraer: {r.status_code}")

if __name__ == "__main__":
    #save_sql()
    scrapp1()