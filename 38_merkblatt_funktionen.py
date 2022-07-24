# Merkblatt Funktionen, Methoden, len build in function

# 1. Definition und Aufruf einer Funktion ohne Argument
def fischbrötchen():
    print("Hallo Hamburg")  # strg "Hamburg" wird an Funktion "fischbrötchen" zurück gegeben
    print("Hallo Welt")     # stg "Welt" wird an die Funktion "fischbrötchen" zurück gegeben

fischbrötchen()             # Aufruf der Funktion "fischbrötchen"

# 2. Definition und Aufruf einer Funktion mit einem Argument
# Du kannst dir einen solchen Parameter als eine zu einer Funktion gehörige Variable vorstellen. Vermeide es,
# einen Funktionsparameter wie eine bereits bestehende Variable zu benennen - Verwirrungsgefahr!
name = "Marin"

def verwirrung(name):
    print(name)             # print innerhalb der Funktion
verwirrung("Mein schönes")  # Argument Übergabe an die Funktion "verwirrung"
verwirrung("Marin MTB")     # Argument Übergabe an die Funktion "verwirrung"

print(name)                 # print außerhalb der Funktion

# 3. Definition und Aufruf einer Funktion mit zwei Argumenten
def segelsport(artikel, count):
    for i in range(0, count):   # Schleife innerhalb einer "range". Counter auf "0" setzen.
        print(artikel)

segelsport("Black Pearl", 3)    # Übergabe des strg "BLack Pearl" an die Variable "Artikel" in der Funktion "Segelsport"

# 4. Verschachtelte Funktionen
def schachtel():
    segelsport("Die Erna", 3)
    segelsport("ist ein schnelles Schiff", 3)

schachtel()

# 4. "return" Values
# Funktionen können auch mittels des Befehls "return" Werte zurückgeben:
def rückgabe_element(gruss):    # funktion "rückgabe_element" mit Argument "gruss"
    return gruss

print(rückgabe_element("Moin mein Bester"))     # Vewendung der Funktion "rückgabe_element" mit strg "Moin mein Bester"

# noch eine Funktion mit "return" und if/else Konstrukt
def rückgabe_mit_ausrufezeichen(titel):     # Funktion "rückgabe_mt_ausrufezeichen" mit Argument "titel"
    return titel + "!"                      # Ergänzt Argument "titel" mit dem strg "!"

if rückgabe_mit_ausrufezeichen("Guten Morgen") == "Guten Morgen!":  # Wenn das Argument "titel" den strg "Guten Morgen"
                                                                    # enthält, dann ergänze den strg mit einem "!"
    print("Richtig!")                       # Das Argument "titel" enthält "Guten Morgen". Das if/else ist "true"
else:
    print("Falsch")                         # Das Argument "titel" enthält nicht "Guten Morgen", Das if/else ist "false"

# "len" Build in function
print(len("Hallo"))             # Anzahl der Elemente in einem strg
print(len(["Hallo", "Welt"]))   # Anzahl der Elemente in einer Liste

# 2 Aufrufe der gleichen Function "nardo_funct" mit verschiedenen Parameter
nardo_funct("Eine Varaible")
nardo_funct("Eine andere Variable")
# Ausgabe
#Eine Varaible
#Eine andere Variable

# Funktion mit zwei Argumenten
def argument_funct(name, count):
    for i in range(0, count):       # counter wird auf "0" gesetzt
        print(name)                 # Was der hier soll weiß ich nicht
argument_funct("Mehr!", 4)          # Funktionsaufruf mit Argument "Mehr!" und count = 4
# Ausgabe:
#Mehr!
#Mehr!
#Mehr!
#Mehr!

# Veschachtelung von Funktionen
def schachtel():
    nardo_funct("Nardo seine erste Funktion")
    argument_funct("wiederholt sich immer wieder", 3)
schachtel()
# Ausgabe:
#Nardo seine erste Funktion
#wiederholt sich immer wieder
#wiederholt sich immer wieder
#wiederholt sich immer wieder

# len Function
var1 = len("Vier Bier")  # Zählt die Anzahl der Elemente eines einzelnen String
var2 = len(["Vier Bier", "und", "eine", "Suppe"])  # Zählt die Anzahl der Listenelemente
print(var1)
print(var2)



