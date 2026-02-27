# Module de conversion de températures

def celsius_vers_fahrenheit(c):
    return float((c * 9/5) + 32)

def fahrenheit_vers_celsius(f):
    return float((f - 32) * 5/9)

def celsius_vers_kelvin(c):
    return float(c + 273.15)

def kelvin_vers_celsius(k):
    if k < 0:
        raise ValueError("Le Kelvin ne peut pas être négatif")
    return float(k - 273.15)