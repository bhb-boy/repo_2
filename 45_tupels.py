# tuples, () Runde Klammern imutable!
# Mit tuples kann man funktionen bauen die mehrere Rückgabewerte gleichzeitig haben

tuple = (1,2,3)

print(tuple)       # Standart Zugriff
print(tuple[0])     # Zugriff per index

# Daten hinzufügen wie bei einer Liste funzt nicht
liste = [1,2,3]     # Schreib das hier in runden Klammern und Du siehst den Fehler
liste.append(4)     # "AttributeError: 'tuple' object has no attribute 'append'"
print(liste)
# Liste -> mutable / Veränderliche Datenstruktur
# Tuple -> immutable / Unveränderliche Datenstruktur

# Selbes Beispiel in einer Funktion, Liste ist veränderbar, tuple nicht.
# Funktion in einer Liste
person = ["Bernhard Beetz, 55"]     # person als Liste übergeben. Schreib das hier in runden Klammern
                                    # und Du siehst den Fehler "TypeError: 'str' object does not support item assignment"

def do_something(p):                # Funktion "do_something"
    p[0] = "Halli Galli"

do_something(person)    # Funktionsaufruf: Ändere den Inhalt von "person".
print(person)



