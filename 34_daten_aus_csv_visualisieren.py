# /home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv

"""# Gib die erste Zeile aus der .csv aus
with open ("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv", "r") as file:
    for line in file:
        print(line)
        break

# Öffne die ersten 5 Zeilen der .csv
with open ("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        print(line)
        if counter >= 4:
            break"""

# Output ist: Id der Liste : Vorname : Im Jahr : Geschlecht : Bundesstaat : Summe des vergebenen Namen
xs = []
ys = []
name = "Anna"   # Suchparameter "name"
gender = "F"    # Suchparameter "gender"
state = "CA"    # Suchparameter "state"
with open ("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv", "r") as file:
    counter = 0
    for line in file:
#        counter = counter + 1   # counter hoch zählen

        line_splitted = line.strip().split(",")         # Hier wird die Zerlegung angeschoben
        if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state:
            xs.append(int(line_splitted[2]))     # xs Liste Jahreszahl
            ys.append(int(line_splitted[5]))     # ys Liste Anzahl der Namen
            print(line_splitted)            # Ausgabe der if Schleife
#            break                           # break nach dem ersten Treffer

# Jetzt das Diagramm
# x-achse: Jahr
# y-achse: Anzahl der Namen pro Jahr
#print(xs)
#print(ys)

import matplotlib.pyplot as plt
plt.plot(xs, ys)

plt.title("Häufigkeit der Verwendung des Namen Anna in den USA")
plt.ylabel("Anzahl der Namen"), plt.xlabel("Zeitachse")
#plt.scatter(xs, ys)
plt.show()




