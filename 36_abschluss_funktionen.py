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

list_sum(cart_prices)"""   # Aufruf der Funktion! Hier wird die Varaible ausserhalb der Funktion übergeben (cart_prices)
# Folgende Ausgabe wird erwartet: 63.95

# b.) Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann.
# Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten
# des Artikels stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

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
print(liste)"""

# b.) Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann.
# Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten
# des Artikels stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

# Hier das final
# Es werden keine Variablen ausserhalb der function übegeben
def prices_list(name,price):
    output = []                     # Leere Liste
    for i in range(1, 11):              # for schliefe mit Abbruchbedingung, "i" ist die Anzahl der Durchgänge
        # Hier muss der Zählmagic rein
        new_price = i * price                 # Multipliziere die Anzahl der Durchgänge mit "price"
        output.append((i,name,new_price))     # Anzahl "i" x name price Innere Klammer ist expression die ein tuple baut.
                                               # Die äußere Klammer ist ein Statement. Die Ausgabe ist in tuple formatiert.

    return output                   # return aufruf beendet die Funktion

print(prices_list("Wunderkeks", 0.79))

# return statement = Functions send Python values/Objects back to the caller.
#                    These values/objects are known as the function's return value

# Folgende Ausgabe wird erwartet:
# ['1 x Wunderkeks: 0.79', '2 x Wunderkeks: 1.58', '3 x Wunderkeks: 2.37', \n
# '4 x Wunderkeks: 3.16', '5 x Wunderkeks: 3.95', '6 x Wunderkeks: 4.74',  \n
# '7 x Wunderkeks: 5.53', '8 x Wunderkeks: 6.32', '9 x Wunderkeks: 7.11',  \n
# '10 x Wunderkeks: 7.9']

# f-string gebastel


