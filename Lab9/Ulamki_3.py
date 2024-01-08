import math

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
        if (self.licznik < 0 and self.mianownik < 0):
            self.licznik = abs(self.licznik)
            self.mianownik = abs(self.mianownik)

        if (self.licznik > 0 and self.mianownik < 0):
            self.licznik *= -1
            self.mianownik = abs(self.mianownik)

    def __str__(self):
        if self.licznik == 0 or self.mianownik == 1:
            return f"Ulamek: {self.licznik}"

        return f"Ulamek: {self.licznik}/{self.mianownik}"

    def __add__(self, y):
        return Ulamek(self.licznik * y.mianownik + y.licznik * self.mianownik, self.mianownik * y.mianownik)

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'w') as plik:
            plik.write(f"{self.licznik} / {self.mianownik}")

    def odczytaj_z_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            ulamek_str = plik.read().strip().split('/')

        return Ulamek(licznik=int(ulamek_str[0]), mianownik=int(ulamek_str[1]))
