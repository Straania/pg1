# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  
# Podtřída Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # (Atribut pro šířku obdélníku, zadaný při inicializaci objektu.)
        self.height = height  # (Atribut pro výšku obdélníku, zadaný při inicializaci objektu.)

    def area(self):
        return self.width * self.height  # (Výpočet plochy obdélníku pomocí vzorce: šířka × výška. Tato metoda implementuje abstraktní metodu `area` z třídy Shape.)

# Podtřída Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # (Atribut pro poloměr kruhu, zadaný při inicializaci objektu.)

    def area(self):
        return math.pi * (self.radius ** 2)  # (Výpočet plochy kruhu pomocí vzorce: π × poloměr^2. Používáme konstantu π z modulu math.)

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)  # (Vytvoření instance obdélníku se šířkou 4 a výškou 5)
    assert rect.area() == 20, "Plocha obdélníku by měla být 20."  # (Kontrola výpočtu plochy obdélníku)

    circle = Circle(3)  # (Vytvoření instance kruhu s poloměrem 3)
    assert round(circle.area(), 1) == 28.3, "Plocha kruhu by měla být přibližně 28.3."  # (Kontrola výpočtu plochy kruhu)

    try:
        shape = Shape()  # (Pokus o vytvoření instance abstraktní třídy)
    except TypeError:
        print("Shape je abstraktní třída a nemůže být přímo instancována.")  # (Očekáváme chybu při pokusu o vytvoření abstraktní třídy)

    print("Všechny testy prošly!")  # (Pokud všechny kontroly proběhnou, testy jsou úspěšné)
test_shapes()