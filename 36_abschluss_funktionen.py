# a.) Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet
# Vervollständige die Funktion list_sum(), der als Parameter eine Liste mit den Preisen übergeben wird.
# Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.
#

"""cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):            #   Aufruf Funktionsname(Parameter):
    total = 0               # counter auf "0" setzen
    for i in l:             # Schleife "i" innerhalb der funktion. Hier wird der function name (l) aufgerufen
        total = total + i   # Addition er enthaltenen Artikel
    print(total)
    # alternativ einfach: print(sum(l)) # Hier mit "sum" Funktion

list_sum(cart_prices)   # Aufruf der Funktion! Hier wird die Varaible ausserhalb der Funktion übergeben (cart_prices)
# Folgende Ausgabe wird erwartet: 63.95"""

# b.) Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann.
# Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten
# des Artikels stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

# Hier die Doofmannlösung
"""price = 0.79

def counting():
    count = 0
    count = count + 1
    print(price, "1 Artikel")
    new_price = (float(price)) + (float(price))   # Hier soll der Preis addiert werden
    count = count + 1
    print(new_price,"2 Artikel")
    next_price = (float(new_price)) + (float(price))    # Hier soll der "new_price" wieder um "price" addiert werden
    print(next_price,"3 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"4 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"5 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"6 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"7 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"8 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"9 Artikel")
    next_price = (float(next_price)) + (float(price))
    print(next_price,"10 Artikel")

counting()"""

# Hier die lbr Lösung
"""article = "Wunderkeks"  # Artikel wird ausserhalb der Funktion übergeben
price = 0.79              # Preis wird auch ausserhalb übergeben

def prices_list():
    liste = []
    count = 0
    while count <= 9:
        count = count + 1                               # Counter funzt
        price_sum = count * float(price)                # Aufsteigender Preis anhand von count * price
        liste.append(f"{count},{article},{price_sum}")  # Jetzt als Listenausgabe mit f (format) und String Formattierung
    return liste

liste = prices_list()                                   # Hier wird die function an eine Variable übergeben
                                                        # um an eine Ausgabe zu kommen
print(liste)

# Ausgabe in eine Liste, append hängt doppelte hintereinader, join schmeisst doppelte raus"""

# b.) Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann.
# Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten
# des Artikels stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

# Hier das final
"""name = "Wunderkeks"
price = 0.79

def prices_list(name, price):   # Parameter Übergabe aus einer Variable in ()
    count = 0
    if count <= 10:
        count = count + 1
    return count
    count = zaehler
    print(zaehler)"""


# Tests auf der zweiten Runde des Tutorial. Das Lesen der Arbeitsblätter ist wichtig, die Videos sind zu wenig.
#def funktionsname(Argument):

def nardo_funct(wirduntenübergeben):    # Funktionsname nardo_funct mit Argument "wirdübegeben"
    print(wirduntenübergeben)
nardo_funct("Deine Mudder")     # Hier findet die Parameter/Argument Übergabe der Variable statt
                                # die in der Function verwendet werden soll
# Ausgabe:
#Deine Mudder

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

# return statement = Functions send Python values/Objects back to the caller.
#                    These values/objects are known as the function's return value"""
"""
def multiply(number1, number2):
    return number1 * number2
x = multiply(6,8)       # set variable to print the return code
print(x)"""