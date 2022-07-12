# Schleifen mit Schlüsselwörter "break" and "continue"

for i in range(0, 10):
    if i == 3:
        continue        # Setzte die Schleife fort, wenn i == 3 ist
    print(i)

for i in range(0, 10):
    if i == 3:
        break           # Unterbreche die Schleife, wenn i == 3 ist
    print(i)

# Beispiel: Prüfung ob die Summe in einer Liste > 10 ist.
liste = [4, 6, 7, 2, 4, 6, 7]   # Ermittlung der Summe einer Liste ohne break
summe = 0
for element in liste:
    summe = summe + element
print(summe)

liste = [4, 6, 7, 2, 4, 6, 7]   # Ermittlung der Summe einer Liste mit break
summe = 0
for element in liste:
    summe = summe + element
    if summe > 10:  # Hier die Abbruchbedingung
        break
print(summe)