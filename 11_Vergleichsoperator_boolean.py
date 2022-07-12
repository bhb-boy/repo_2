# Vergleichsoperatoren <,>,==

if 4 < 5:
    print("ja")

# Vergleichsoerator mit Boolean
print(6 < 5)       # False output Vergleichsoperator (Datentyp Boolean)
print(5 < 6)       # True output  Vergleichsoperator (Datentyp Boolean)

b = True           # Variable b auf True gesetzt
print(b)           # Boolean Wert der Variable

c = False          # Variable c auf False gesetzt
print(c)           # Boolean Wert der Variable

if 5 < 6:           # Einfaches if mit direkter Ausgabe
    print("5 ist kleiner als 6")

result = 5 < 6     # Variable "result" wird mit Boolean True/False belegt
if result:         # Variale "result" ist True
    print("5 ist kleiner als 6")

print(5 > 6)       # Boolean False
print(6 > 6)       # Boolean False
print(7 > 6)       # Boolean True

print(5 == 5)      # Boolean True
print(6 == 5)      # Boolean False

# Vergleichsoperator mit strg und ==
gruss = "Hallo"
print(gruss == "Hallo")     # strg der Variable gruss ist True
print(gruss == "Moin" )     # strg der Variable gruss ist False

# Vergleichsoperator mit strg und !=
gruss = "Hallo"
print(gruss != "Hallo")     # strg der Variable und != gruss ist False
print(gruss != "Moin" )     # strg der Variable und != gruss ist True

# Vergleich von Zahlen ( Mathematische Operatoren)
print(5 < 5)                # Vergleich False
print(5 <= 5)               # Vergleich True

