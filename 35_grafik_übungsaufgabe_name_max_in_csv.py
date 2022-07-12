# Übungsaufgabe: Name Max in CA zwischen 1950 und 2000 jeweils einschlieslich
# ['587639', 'Max', '1950', 'M', 'CA', '57']
name = "Max"   # Suchparameter "name"
gender = "M"    # Suchparameter "gender"
state = "CA"    # Suchparameter "state"
start_date = 1950
end_date = 2000
occurences = 0

with open ("/home/nardo/share/udemy_python_bootcamp_resources/Kursmaterialien/data/names.csv", "r") as file:
    for line in file:
        splitted = line.strip().split(",")      # Hier wird zerlegt, spaces entfernt und die Zeilenumbruch Zeichen
                                                # Zeile für Zeile wie folgt: ['5647276', 'Landon', '2014', 'M', 'WY', '17']
#        print(splitted)
        if splitted[2] == "Year":               # Hier wird die erste Zeile mit den Überschriften abgefangen
            continue

        year = int(splitted[2])                 # Hier wird die Jahreszahl abgefischt und in die Variable "year" gekippt

        if splitted[1] == "Max" and year >= start_date and year <= end_date and splitted[3] == "M" and splitted[4] == "CA":
            occurences = occurences + int(splitted[5])  # Hier werden die Treffer aus "int(splitted[5])" auf occurences auf addiert

print(occurences)
