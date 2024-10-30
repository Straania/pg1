def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    radek, sloupec = cilova_pozice
    typ_figury = figurka["typ"]
    pozice = figurka["pozice"]

    # Ověření, zda je cílová pozice na šachovnici
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False
    
    # Ověření, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False

    # Funkce pro ověření, zda je mezi dvěma pozicemi cesta volná
    def cesta_volna(start, cil):
        r1, s1 = start
        r2, s2 = cil
        if r1 == r2:  # Horizontální pohyb
            step = 1 if s2 > s1 else -1
            for s in range(s1 + step, s2, step):
                if (r1, s) in obsazene_pozice:
                    return False
        elif s1 == s2:  # Vertikální pohyb
            step = 1 if r2 > r1 else -1
            for r in range(r1 + step, r2, step):
                if (r, s1) in obsazene_pozice:
                    return False
        else:  # Diagonální pohyb
            step_r = 1 if r2 > r1 else -1
            step_s = 1 if s2 > s1 else -1
            r, s = r1 + step_r, s1 + step_s
            while (r, s) != (r2, s2):
                if (r, s) in obsazene_pozice:
                    return False
                r += step_r
                s += step_s
        return True

    # Ověření pohybu pro jednotlivé figury
    if typ_figury == "pěšec":
        if pozice[0] == 2:  # výchozí pozice
            if (radek == pozice[0] + 2 and sloupec == pozice[1]) and \
               (pozice[0] + 1, pozice[1]) not in obsazene_pozice:
                return True
        if radek == pozice[0] + 1 and sloupec == pozice[1]:
            return True

    elif typ_figury == "jezdec":
        if (abs(radek - pozice[0]), abs(sloupec - pozice[1])) in [(2, 1), (1, 2)]:
            return True

    elif typ_figury == "věž":
        if radek == pozice[0] or sloupec == pozice[1]:
            return cesta_volna(pozice, cilova_pozice)

    elif typ_figury == "střelec":
        if abs(radek - pozice[0]) == abs(sloupec - pozice[1]):
            return cesta_volna(pozice, cilova_pozice)

    elif typ_figury == "dáma":
        if (radek == pozice[0] or sloupec == pozice[1] or
            abs(radek - pozice[0]) == abs(sloupec - pozice[1])):
            return cesta_volna(pozice, cilova_pozice)

    elif typ_figury == "král":
        if max(abs(radek - pozice[0]), abs(sloupec - pozice[1])) == 1:
            return True

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
