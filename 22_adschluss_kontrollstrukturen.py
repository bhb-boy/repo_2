# Abschluss Übung Kontrollstrukturen
# 1a.) Gib nacheinander alle Kontinente aus der Liste continents aus.

continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for i in continents:            # Alle Listenelemente untereinander, je strg eine Zeile
    print(i)

# 1b.) Gib aus der Liste continents nur die bewohnten Kontinente aus. Also Antarktis raus
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]
# BHB Lösung
#continents.remove(continents[1])
#for  i in continents:
#    print(i)
# Musterlösung
for continent in continents:
    if continent == "Antarktis":
        continue
    print(continents)

# 1c.) Gib aus der Liste stuff nur die Kontinente aus. Vergleiche mit der Liste continents
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]
stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]

# Ausdruck beider Listen
print("Liste continets:",continents)
print("Liste stuff:",stuff)

# compairing continents and stuff
# Finding the intersection of 2 lists means finding all the elements that are present in both lists.
# BHB Lösung
#doppelte = set(continents) & set(stuff)
#print(list(doppelte))

# Udemy Lösung: Suche die Elemente die in beiden Listen vorhanden sind:
for element in stuff:
    if element in continents:
        print(element)

# 1d.) Wie viele Kontinente sind in der Liste doppelte enthalten?
print(len(doppelte))

