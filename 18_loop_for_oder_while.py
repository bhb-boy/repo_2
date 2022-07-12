# Wann wird eine "while" Schleife verwendet und wann eine "for" Schleife?
# while Schleife kann endlos laufen wenn keine Begrenzung eingebaut wird
# for Schleife, wenn klar ist wie viele Werte behandelt werden sollen, z.B. durch range Funktion
# Wenn beide Schleifentypen funktionieren würden, nimm die "for" Schleife

zähler = 0
while zähler < 10:          # Funktion solange eine Bedingung erfüllt ist
    print(zähler)
    zähler = zähler + 1

zähler = 0
for zähler in range(1, 10): # Festgelegter Zahlenbereich
    print(zähler)