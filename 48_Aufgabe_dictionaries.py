# Aufgabe Dictionarys
# Lies zuerst die Daten in ein Dictionary ein und zähle, wie oft jeder Vorname insgesamt vorgekommen ist.
# Analysiere dann erst das Dictionary und finde den häufigsten Vornamen heraus.
# Achte drauf, wenn du 2 Zahlen addieren möchtest, musst du ggf. einen String zuerst in eine Zahl umwandeln.
# Schreibe den gesamten Code, der die Datei öffnet und durchgeht, in einer Zelle, wenn Du Jupyter Notebook verwendest.

# so sieht der input aus
#Id,Name,Year,Gender,State,Count
#1,Mary,1910,F,AK,14
#2,Annie,1910,F,AK,12
#3,Anna,1910,F,AK,10

import csv

with open("/home/nardo/PycharmProjects/python-projects/udemy_python_course/names_small.csv") as f:
    csv_reader = csv.reader(f)      # .reader read object "f"
    next(csv_reader)                # next - skippt die erste Zeile
    process_list = []               # Hier eine leere Liste für die Ausgabe
    for line in csv_reader:         # Schleife über die Ausgabe [18 ,'Mary', '1910', 'F', 'AK', '14']
        filtered_list = (line[1:])  # remove of index [0] Output: ['Mary', '1910', 'F', 'AK', '14']
        del filtered_list[1:4]      # delete index [1] - index [4] übrig bleibt: ['Mary', '14']
#        print(filtered_list)        # Tadaaa! Es bleiben Namen und Anzahl übrig. Je nach Indentation den letzten
                                    # Eintrag oder alle Listen. Jede Zeile ist eine neue Liste. Das geht jetzt
                                    # in ein neue Liste, welche ausserhalb der Schleife weiter zur Verarbeitung geht.
        process_list.append(filtered_list)  # Hänge alle Listen in eine neue Liste
print(process_list)                 # Hier kommt die ganze Suppe als eine Zeile von Listen heraus und kann ausserhalb
                                    # des for loop weiter verarbeitet werden
#print(type(process_list))           # Wir haben immer noch eine Liste, kein Dictionary

# Dictionary can not store multiple duplicate values
# Als Zwischenschritt erst einmal nur die Namen zählen. Darum die Anzahl der Namen erst einmal droppen

process_dictionary = {}         # Jetzt ein leeres Dictionary

#for element in process_list:    # for Schleife über die process_list
#    if element in process_list:
#        process_dictionary[element] = process_dictionary[element] + 1
#    else:
#        process_dictionary[element] = 1
#print(process_dictionary)









# Etwas Spielzeit mit der Vorbereitung für die Dictionary Aufgabe
#liste = ["Hallo","Hallo","Welt","Hallo","Mars"]

#d = {}  # Leeres Dictionary als "d"
#for element in liste:
#    if element in d:     # Gibt es das Element schon als Schlüssel. Is key in dictionary?
#        d[element] = d[element] + 1        # Wenn es das Element in dem Dictionary gibt, zähle den Wert von element hoch
#    else:
#        d[element] = 1  # Wenn es das Element noch nicht als key gibt, setzte den Zähler auf 1"""
#print(d)







# Das hier ist die große Datei
# for i in open("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv"):
# https://www.pythontutorial.net/python-basics/python-read-csv-file/