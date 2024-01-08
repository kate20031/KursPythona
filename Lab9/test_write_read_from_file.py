import unittest
import pytest
import self
from Ulamki_3 import Ulamek
from unittest.mock import MagicMock



def test_zwykły_zapisu():
        u1 = Ulamek(1, -6)
        Ulamek.zapisz_do_pliku(u1, "plik_1")
        ul2 = Ulamek.odczytaj_z_pliku(self, "plik_1")
        print(ul2)

@pytest.mark.parametrize("u1, u2, oczekiwana_suma", [(Ulamek(1, 3), Ulamek(1, 2), Ulamek(5, 6)),
                                                     (Ulamek(-1, 3), Ulamek(-2, 3), Ulamek(-1, 1)) ])
def test_suma_parametr(u1, u2, oczekiwana_suma):
    suma = u1 + u2
    assert suma.licznik == oczekiwana_suma.licznik
    assert suma.mianownik == oczekiwana_suma.mianownik

@pytest.fixture
def zapisz_mocked(monkeypatch):
    mock_open = MagicMock()
    monkeypatch.setattr(Ulamek, 'zapisz_do_pliku', mock_open)
    return mock_open

@pytest.fixture
def odczytaj_mocked(monkeypatch):
    ulamek = Ulamek(-1, 7)
    with monkeypatch.context() as m:
        m.setattr(Ulamek, 'odczytaj_z_pliku', MagicMock(return_value=ulamek))
        yield m

def test_zapisz_i_odczytaj_mock(zapisz_mocked, odczytaj_mocked):
    ulamek = Ulamek(1, -7)
    ulamek.zapisz_do_pliku("plik1")
    zapisz_mocked.assert_called_once_with("plik1")

    odczytany_ulamek = Ulamek.odczytaj_z_pliku("plik1")

    assert ulamek.licznik == odczytany_ulamek.licznik
    assert ulamek.mianownik == odczytany_ulamek.mianownik

if __name__ == '__main__':
    unittest.main()
