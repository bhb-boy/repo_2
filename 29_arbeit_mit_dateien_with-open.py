# Arbeit mit Dateien "with"
# Zuverlässiges schließen von Dateien
# Anstatt folgende Syntax zu verwenden: file = open("blablubb.txt") / file.close()
# Damit wird im Fehlerfall die göffnete Datei zuverlässig wieder geschlossen
with open("piraten.txt", "r") as file:      # Es geht nur "r", weder "w" noch "a" Funny!
    for line in file:
        print(line)

# Nur innerhalb des "with" Blocks kann die Datei weiter bearbeitet werden.
# Keine Ahnung wie das dann gescripted wird.