# Arbeit mit Dateien, lesen und schreiben!
# csv = comma seperated value

file = open("lesen.txt", "r")
for line in file:
    print(line)

# Ausgabe mit Leerzeile zwischen den Zeilen!
# Zeilenumbruch Steuerzeichen "\n"
print("Hal\nlo")
print("welt")
# -----------------------------------------
print("File open mit Steuerzeichen")
file = open("lesen.txt", "r")
for line in file:
    # line = "Hallo Welt 123!!!\n"
#    print(line)     # Eingelesen wird die variable Line ist als letztes Zeichen das unsichtbare \n unter gebracht.
#   jeder print Aufruf sorgt für einen Zeilenumbruch
    print(line[-1] == "\n") # Gib das letzte Zeichen der Zeile aus [-1]

# Zum löschen von Leer- oder Sonderzeichen kann .strip verwendet werden
    print(line.strip())

