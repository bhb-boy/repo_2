# Arbeit mit Dateien schreiben "w"
file = open("schreiben.txt" , "w")      # schreiben.txt wird von PyCharm angelegt (touch)
file.write("Vier Bier und eine Suppe ")  # Append strg
file.write("Vier Bier und eine Suppe")  # Append another strg in the same line
file.write("\nVier Bier und eine Suppe")  # Append strg with newline
file.close()                            # Speichern und schließe des File's

# The string.join() function can also be used to add a newline

# Schreiben einer Liste in Datei
file = open("piraten.txt", "w")     # "w" Überschreibt vorhandene Daten. Falls nicht vorhanden, wird die Datei getouched
piraten = ["jan","hein","claas","pit","und deine Mudder"]
for pirat in piraten:
    file.write(pirat + "\n")        # newline \n muss in Anführungszeichen
file.close()

# Verschiedene Dateiöffnungsmodi
# "r"   read
# "w"   write
# "a"   append
file = open("piraten.txt", "a")   # variable "neuer_satz" wird an "piraten.txt" angehängt. "a" append modus
neuer_satz = "sind coole Piraten, die fahren mit!"
file.write(neuer_satz)
file.close()

# Mit einer Schleife kann man keinen neuen Satz anhängen?
# for neuer_satz in piraten:
#    file.write(neuer_satz + "\n")
