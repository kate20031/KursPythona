# Zrób dwie wersje programu:

# Wersja 1:
# - klasa Ułamek (z poprzednich zajęć)
# - dwie wartość - n i k wczytane z args
# - stworzenie dużej liczby (co najmniej n > milion) ułamków 
# - zrobienie k operacji na nich; dowolną metodą np.
# ---- możemy trzymać Ułamki w tablicy
# ---- traktować ją jako cykliczną dla poniższych działań
# ---- a[i] += a[i+1]

# Wersja 2:
# j.w., ale dodajemy do klasy Ułamek __slots__ = ('licznik', 'mianownik') 

# Badamy zajętość pamięci i czas. Porównujemy wyniki dla różnych liczb ułamków i wykonanych operacji. 


# Badanie można wykonać taką komendą:
# /usr/bin/time -v python program.py 2>&1 1>/dev/null | grep  -E "wall|Max"

# Komenda /usr/bin/time, dla odróżnienia od wbudowanego time, bada dużo różnych rzeczy na temat uruchomionego procesu. Fragment z dużą liczbą znaków > powoduje skierowanie stdout do /dev/null (ewentualne wyjście programu w pythonie), stderr do stdout (wydruk komendy time) - w tej kolejności - a następnie przekierowanie stdout do polecenia grep, które wybierze interesujące nas dwie linijki.

# Miło by było, żeby Wersja 1 zamieniana była w Wersję 2 jakoś automatycznie, np. z użyciem
# perl -p -e "s/# Wersja2 //" wersja1.py > wersja2.py
# Powyższa linijka usunie z każdej linijki maksymalnie jedno wystąpienie ciągu '# Wersja2 ' czyli w szczególności zamieni takie coś:
# # Wersja2 __slots__ = (blu,bla)
# na takie coś:
# __slots__ = (blu,bla)
# Pozostałych linijek nie zmienia. 

# BTW: nie zaszkodzi zapamiętać sobie tą instrukcję perl-a. Jest jeszcze wersja perl -pi -e "s/co/naco/" plik która zmienia plik w miejscu (opcje -pi -e łatwo zapamiętają zwłaszcza łakomczuchy ;)


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
