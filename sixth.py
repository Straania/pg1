import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne URL předanou v parametru url pomocí requests.get(),
    zkontroluje návratový kód response.status_code, který musí být 200.
    Pokud je odpověď úspěšná, najde ve staženém obsahu stránky všechny výskyty
    <a href="url">odkaz</a> a z nich načte URL, které vrátí jako seznam.
    """
    hrefs = []
    
    try:
        # Stáhneme obsah stránky
        response = requests.get(url)
        
        # Zkontrolujeme, zda odpověď je OK (status code 200)
        if response.status_code == 200:
            # HTML obsah stránky
            html_content = response.text
            
            # Regulární výraz pro nalezení všech href atributů v <a> tagu
            pattern = r'href=["\'](https?://[^\s\'"]+)["\']'
            
            # Použijeme re.findall k nalezení všech URL
            hrefs = re.findall(pattern, html_content)
            
            # Pokud by byl relativní odkaz, doplníme základní URL
            # Například: "/about" -> "https://www.jcu.cz/about"
            for i in range(len(hrefs)):
                if hrefs[i].startswith('/'):
                    hrefs[i] = url.rstrip('/') + hrefs[i]
                    
        else:
            print(f"Chyba při stahování stránky. Status kód: {response.status_code}")
    
    except Exception as e:
        print(f"Došlo k chybě při načítání stránky: {e}")
    
    return hrefs

if __name__ == "__main__":
    try:
        # Získáme URL z argumentů příkazového řádku
        url = sys.argv[1]
        
        # Zavoláme funkci pro získání všech odkazů
        hrefs = download_url_and_get_all_hrefs(url)
        
        # Vypíšeme získané odkazy
        for href in hrefs:
            print(href)
    
    except IndexError:
        print("Nebyla zadána žádná URL adresa.")
    except Exception as e:
        print(f"Program skončil chybou: {e}")

