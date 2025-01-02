# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # Vytvoříme prázdný seznam pro uložení výsledných čísel
    result = []
    
    # Iterujeme přes všechna čísla v seznamu
    for num in numbers:
        # Pokud narazíme na číslo 10, ukončíme zpracování seznamu
        if num == 10:
            break
        
        # Pokud je číslo větší než 5, zpracujeme ho
        if num > 5:
            # Vynásobíme číslo 2 a přidáme ho do výsledného seznamu
            result.append(num * 2)
    
    # Vrátíme výsledný seznam čísel
    return result

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]  

