def dec_to_bin(cislo):
    """
    Funkce převede číslo na binární reprezentaci.
    Číslo může být předáno jako int nebo str.
    Výstupem je binární reprezentace jako řetězec.
    """
    # Převést cislo na int, pokud je zadané jako str
    if isinstance(cislo, str):
        cislo = int(cislo)
    
    # Vrátit binární reprezentaci čísla (bez prefixu '0b')
    return bin(cislo)[2:]


# Testovací funkce
def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
