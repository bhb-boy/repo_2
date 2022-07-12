# Öffne .csv und selektiere Zeilen nach gewünschten Begriff (if Schleife)
print("Filtern nach Suchbegriff")
with open("datei.csv") as file:
    for schleife in file:
        bestimmtes_element = schleife.strip().split(";")
        if bestimmtes_element[2] == "MUC":      # Schleife für ein Suchbegriff
#        if bestimmtes_element[2] == "BER" or bestimmtes_element[2] == "BUD": # if Schleife für zwei Suchbegriffe
            print(bestimmtes_element[2])        # Achtung: weitere indentation!
            print(bestimmtes_element)

print("Error TypeError: '>=' not supported between instances of 'str' and 'int' ")

with open ("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
#        if data[1] >= 2000000:     # Ohne casting gehts hier nicht weiter, siehe nachfolgendem Fehler:
#            print(data)     # TypeError: '>=' not supported between instances of 'str' and 'int'
        if int(data[1]) >= 2000000:    # Mit casting int(data[1]) geht es dann weiter mit Bedingung ">="
            print(data)

# Schreibweise mit einem continue
print("Mit Bedingung 'kleiner als'")
with open ("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        if int(data[1]) < 2000000:      # Hier sollte eigentlich nur München heraus kommen, tut es aber nicht!
            continue
        print(data)

# Schreibweise mit mehreren continue
print("Mit mehreren 'continue")
with open ("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        if int(data[1]) < 2000000:
            continue            # Fahre fort wenn Bedingung erfüllt ist. Auch das funktioniert nicht wie angesagt!
        if data[2] == "BUD":
            continue            # Breche ab wenn Bedingung nicht erfüllt ist
        print(data)