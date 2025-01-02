# Příklad 2: Práce s externími knihovnami a soubory
# Zadání:
# Napište funkci `fetch_and_save_data`, která:
# 1. Načte data z URL (https://jsonplaceholder.typicode.com/posts).
# 2. Do staženého json souboru přidá klíč `userName` s hodnotou jména uživatele podle klíče `userId` z URL (např. 1 -> "Leanne Graham").
# 3. Data uloží do souboru `data.json` ve formátu JSON.
# Použijte knihovny `requests` a `json`.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    try:
        # 1. Odeslání GET požadavku na URL pro stažení dat
        response = requests.get(url)

        # Kontrola, zda byl požadavek úspěšný
        if not response.ok:
            print("Chyba při stahování dat.")  # Pokud selže, vypíšeme chybu
            return False  # Funkce vrátí False

        # 2. Načtení JSON dat z odpovědi
        data = response.json()

        # 3. Pro každý záznam v datech:
        for item in data:
            # a. Získání userId ze záznamu
            user_id = item.get("userId")
            
            # b. Přidání klíče `userName` podle `userId` z mapy `user_names`
            # Pokud není `userId` nalezen, použijeme výchozí hodnotu "Unknown"
            item["userName"] = user_names.get(user_id, "Unknown")

        # 4. Uložení obohacených dat do souboru `data.json`
        with open("data.json", "w", encoding="utf-8") as f:
            # a. Uložíme data jako JSON s čitelným formátováním
            json.dump(data, f, ensure_ascii=False, indent=4)

        # 5. Informace o úspěšném uložení
        print("Data úspěšně uložena do souboru data.json.")
        return True  # Funkce vrací True, což signalizuje úspěch

    except Exception as e:
        # Pokud dojde k chybě, vypíšeme její obsah
        print(f"Nastala chyba: {e}")
        return False  # Funkce vrátí False, pokud něco selže

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])
