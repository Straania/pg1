def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    nepravidelne = ["", "jeden", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]

    if 0 <= cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"][cislo - 10]
    elif 20 <= cislo < 100:
        desitky_index = cislo // 10
        jednotky_index = cislo % 10
        if jednotky_index == 0:
            return desítky[desitky_index]
        else:
            return desítky[desitky_index] + " " + jednotky[jednotky_index]
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah"  # Pro rozšíření o větší čísla

# Příklady použití
print(cislo_text(0))    # "nula"
print(cislo_text(1))    # "jedna"
print(cislo_text(15))   # "patnáct"
print(cislo_text(25))   # "dvacet pět"
print(cislo_text(100))  # "sto"

