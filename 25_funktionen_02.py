# Functions 02

def multi_print(name, count):   # Funktion mit 2 Parameter
    for i in range(0, count):   # Schleife auf null gesetzt und Zähler angeschmissen
        print(name)

# input:
multi_print("Hausfrauenknoten", 4)  # $name und $count werden übergeben. Gezählt wird: 0,1,2,3
"""Hausfrauenknoten
Hausfrauenknoten
Hausfrauenknoten
Hausfrauenknoten"""

# Verschachtelung von Funktionen
def weitere_funktion():
    multi_print("Hallo Claas",3)    # Aufruf vorher erstellter Funktion
    multi_print("Hallo Pit",3)      # Aufruf vorher erstellter Funktion

weitere_funktion()              # Aufruf der verschachtelten Funktion mit () am Ende

# Function gibt etwas zurück
def maximum(a, b):
    if a < b:           # Wenn A kleiner B:
        return b        # Im Funktionsaufbau erscheint das was in diesem "return" steht. In diesem Fall: B ist größer als A
    else:               # Oder, wenn nicht, dann:
        return a        # Wenn B kleiner A, return A
result = maximum(4,5)   # Varaiable result wird befüllt mit einer Funktion und Parameter
print(result)           # B ist größer als A. Es wird der Inhalt von B zurück gegeben

