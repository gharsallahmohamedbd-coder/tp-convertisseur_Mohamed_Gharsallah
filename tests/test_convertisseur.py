import pytest
from src.convertisseur import *

def test_zero_celsius():
    assert celsius_vers_fahrenheit(0) == 32.0

def test_100_celsius():
    assert celsius_vers_fahrenheit(100) == 212.0

def test_kelvin_to_celsius():
    assert kelvin_vers_celsius(273.15) == 0.0

def test_negative_celsius():
    assert celsius_vers_kelvin(-273.15) == 0.0

def test_kelvin_negatif():
    with pytest.raises(ValueError):
        kelvin_vers_celsius(-1)

def test_valeur_decimale():
    assert round(celsius_vers_fahrenheit(36.6), 1) == 97.9