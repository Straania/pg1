import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah zadané stránky, zkontroluje status kód a získá všechny odkazy
    ve formátu <a href="url"> na stránce.
    """
    hrefs = []

    try:
        # Stáhneme obsah stránky pomocí requests.get
        response = requests.get(url)

        # Pokud status kód není 200, vyhodíme výjimku
        if response.status_code != 200:
            raise Exception(f"Chyba při stahování stránky, status kód: {response.status_code}")

        # Vytvoříme BeautifulSoup objekt pro analýzu HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Projdeme všechny <a> tagy a extrahujeme href atributy
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            hrefs.append(href)

    except Exception as e:
        print(f"Program skončil chybou: {e}")

    return hrefs

if __name__ == "__main__":
    # Zkontrolujeme, jestli byl zadán URL argument
    if len(sys.argv) < 2:
        print("Chyba: Musíte zadat URL jako argument.")
        sys.exit(1)  # Ukončíme program s chybovým kódem

    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)  # Výstup všech odkazů
    except Exception as e:
        print(f"Program skončil chybou: {e}")



