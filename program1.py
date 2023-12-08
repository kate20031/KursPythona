import math
import sys

class Ulamek:
    def __init__(self, licznik, mianownik):
        assert mianownik != 0
        self.licznik = licznik
        self.mianownik = mianownik
        self.skrocenie()

    # Wersja2 __slots__ = ('licznik', 'mianownik')

    def skrocenie(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd

    def __add__(self, y):
        return Ulamek(self.licznik * y.mianownik + y.licznik * self.mianownik, self.mianownik * y.mianownik)

n = int(sys.argv[1])
k = int(sys.argv[2])
ulamki = [Ulamek(1, i + 1) for i in range(n)]
for i in range(k):
    ulamki[i % n] += ulamki[(i + 1) % n]