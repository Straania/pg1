def bin_to_dec(binarni_cislo):
    # Pokud je vstup typu int, převedeme ho na řetězec
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    
    # Funkce int() převede binární řetězec na desítkové číslo
    return int(binarni_cislo, 2)

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157  # test pro "10011101" na 157
    assert bin_to_dec(10011101) == 157  # test pro 10011101 jako int na 157

test_funkce()
