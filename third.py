def je_prvocislo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    return [n for n in range(2, maximum + 1) if je_prvocislo(n)]

# Příklad použití
print(je_prvocislo(1))   # False
print(je_prvocislo(2))   # True
print(je_prvocislo(3))   # True
print(je_prvocislo(100)) # False
print(je_prvocislo(101)) # True

print(vrat_prvocisla(1))  # []
print(vrat_prvocisla(2))  # [2]
print(vrat_prvocisla(3))  # [2, 3]
print(vrat_prvocisla(10)) # [2, 3, 5, 7]

