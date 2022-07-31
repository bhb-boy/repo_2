# Umgang mit Listen
metalbands = ["Metallica","AC/DC","Bolt Thrower","Meshugga", "Hirschi"]

last_band = metalbands.pop()        # Letztes Element entfernen .pop
print(last_band)                    # print des letzten Element aus "metalband" -> "Hirschi"
print(metalbands)                   # print der Liste ohne das letzte Element

# Mehrere Listen aneinander hängen mit "+" Operator
bands = ["Metallica","AC/DC","Bolt Thrower","Meshugga", "Hirschi"] + ["Mocheeba"]
print(bands)

# del , Wie Funktionsaufruf -> Entfernen einzelner Elemente
del bands[1]            # delete per index del Funktion
print(bands)

# remove Methode -> Praktisch weil man die index Position nicht braucht.
bands.remove("Metallica")       # Suche nach strg und removal
print(bands)





