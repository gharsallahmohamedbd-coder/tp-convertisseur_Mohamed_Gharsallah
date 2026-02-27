# tests/test_convertisseur.py
import sys
import os
import pytest

# Ajouter le dossier src au path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import convertisseur  # maintenant Python le trouve toujours

def test_zero_celsius():
    assert convertisseur.celsius_vers_fahrenheit(0) == 32.0

def test_100_celsius():
    assert convertisseur.celsius_vers_fahrenheit(100) == 212.0

def test_kelvin_to_celsius():
    assert convertisseur.kelvin_vers_celsius(273.15) == 0.0

def test_negative_celsius():
    assert convertisseur.celsius_vers_kelvin(-273.15) == 0.0

def test_kelvin_negatif():
    with pytest.raises(ValueError):
        convertisseur.kelvin_vers_celsius(-1)

def test_valeur_decimale():
    assert round(convertisseur.celsius_vers_fahrenheit(36.6), 1) == 97.9
