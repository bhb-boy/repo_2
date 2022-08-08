# Aufgabe Dictionarys
# Lies zuerst die Daten in ein Dictionary ein und zähle, wie oft jeder Vorname insgesamt vorgekommen ist.
# Analysiere dann erst das Dictionary und finde den häufigsten Vornamen heraus.
# Achte drauf, wenn du 2 Zahlen addieren möchtest, musst du ggf. einen String zuerst in eine Zahl umwandeln.
# Schreibe den gesamten Code, der die Datei öffnet und durchgeht, in einer Zelle.

# so sieht der input aus
#Id,Name,Year,Gender,State,Count
#1,Mary,1910,F,AK,14
#2,Annie,1910,F,AK,12
#3,Anna,1910,F,AK,10

import csv

with open("/home/nardo/PycharmProjects/python-projects/udemy_python_course/names_small.csv") as f:
    csv_reader = csv.reader(f)      # .reader read object "f"
    next(csv_reader)                # next - skippt die erste Zeile
    for line in csv_reader:         # Schleife über die Ausgabe [18 ,'Mary', '1910', 'F', 'AK', '14']
        filtered_list = (line[1:])  # remove of index [0] Output: ['Mary', '1910', 'F', 'AK', '14']
        del filtered_list[1:4]      # delete index [1] - index [4]
        print(filtered_list)        # Tadaaa! Es bleiben Namen und Anzahl übrig.









# Das hier ist die große Datei
# for i in open("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv"):
# https://www.pythontutorial.net/python-basics/python-read-csv-file/