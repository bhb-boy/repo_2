with open ("datei.csv") as file:
    for line in file:
        print(line)         # print mit newline zwischen jeder Zeile

with open ("datei.csv") as file:
    for line in file:
        print(line.strip()) # print ohne newline

with open ("datei.csv") as file:
    for line in file:
        print(line.split(";"))         # Zerlegt die .csv in eine zeilenweise Liste bei ";" Delimitter mit \n am Ende
                                        # .split definiert den Delimitter
        print(line.strip().split(";"))  # line.strip entfernt die Leerzeichen und Zeilenumbruchzeichen \n

# Selektion bestimmter Listenwerte
with open("datei.csv") as file:
    for apfel in file:
        bestimmtes_element = apfel.strip().split(";")
        print(bestimmtes_element)       # csv zeilenweise ohne zeilenumbruch Zeichen (.strip)
        print(bestimmtes_element[0] + ":" + bestimmtes_element[1])  # bestimmte Elemente via Index [0]
                                                                    # ohne zeilenumbruch Zeichen (.strip)

