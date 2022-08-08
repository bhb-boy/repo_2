# tuples packen und entpacken
# rückgabewerte einer funktion zu übernehnmen? nuschel nuschel
# zweites Beispiel wie ein tuple entpackt wird

# entpacken
tuple = ("Bernardo Beetzo", 55, "Pythonschüler")

# Das hier kann man vereinfachen, komprimieren. Weise den Strings aus einem tuple variablen zu. -> Zeile 14
#name = tuple[0]
#age = tuple[1]
#actual = tuple[2]

# Hier das entpacken des tuple als Einzeiler.
# Entpackt in untereinander stehende strgs
name, age, actual = tuple   # Erster Wert in die variable "name", zweiter Wert ind die Variable "age", dritter Wert
                            # in die Variable "actual"

print(name)
print(age)
print(actual)

# Mit 4 Einträgen klappt das nicht. Die Anzahl der Elemente muss eingehalten werden, siehe die Fehlermeldung -> Zeile 23
"""tuple2 = ("Bernardo Beetzo", 55, "Pythonschüler", "Widder")
name, age, actual = tuple2      # ValueError: too many values to unpack (expected 3)"""

# Funktion um tuple zu entpacken in eine Liste! Funny
def get_tuple():
    return ("Bernardo Beetzo", 55, "Pythonschüler")

# Aufruf der 3 Parameter aus dem "retun" in Zeile 28
#Hier als strgs untereinander
print(name)
print(age)
print(actual)

print(get_tuple())      # Funktionsaufruf get_tuple(). Ausgabe in tuple Liste

# Liste von tuples, aussen eckige Klammer, also Liste, innen tuple
piraten = [
    ("Jan", 34 ),
    ("Hein", 31)
]

# entpacken in einer "for" Schleife. Warum findet die Ausgabe 2x statt???
for pirat in piraten:
    print(piraten)  # Ausgabe von tuples als Listenelemente

for pirat in piraten:   # Hier wird "pirat" als "Hilsfvaraible" verwendet
    name, age = pirat   # tuple was entpackt wird. Ausgabe als strgs untereinander
    print(name)
    print(age)

for name, age in piraten: # iteration über die Liste, entpacken der tuples direkt
    print(name)
    print(age)

