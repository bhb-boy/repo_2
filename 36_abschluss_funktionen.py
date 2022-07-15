# a.) Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet
# Vervollständige die Funktion list_sum(), der als Parameter eine Liste mit den Preisen übergeben wird.
# Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.
#
#cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]
#sum_of_prices = 0

# BHB Lösung mit "for" loop, ohne function
        #for price in cart_prices:
        #    sum_of_prices = sum_of_prices + price
        #print(sum_of_prices)

"""cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):    #   Aufruf Funktionsname(Parameter):
    total = 0       # counter auf "0" setzen
    for i in l:     # Schleife "i" innerhalb der funktion
        total = total + i   # Addition er enthaltenen Artikel
    print(total)
    # alternativ einfach: print(sum(l)) # Hier mit "sum" Funktion

list_sum(cart_prices)   # Aufruf der Funktion! call the function
# Folgende Ausgabe wird erwartet: 63.95"""

# b.) Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt!
# Liste mit Preisen bis zehn Einheiten des Artikels enthalten
# So soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".

"""articel = "Wunderkeks"
price = "0,79"
max_articel = 10

#def prices_list(l):
count = 0
while count <= 10:
    print(count)
    count = count + 1

prices_list(count)"""
# Ein zarter Anfang der funktioniert
def my_function():
    print("Hello from my function")
my_function()

article = "Wunderkeks"
price = "0,79"
max_article = 10

"""def prices_list():          # function ohne argument()
    count = 0
    if count <= 10:
        print(articel, price)
        count = count + 1
        print("Hier geht mehr rein")
        print(count)
    else:
        print("Wir haben mehr als einen Artikel")"""


def tolle_funktion():
    price = 0.79
    count = 2
"""    while count <= 10:
        print(article,price)
        count = count + 1
        new_price = (float(price)) + (float(price))   # Hier soll der Preis addiert werden
#        print(new_price)
        next_price = (float(new_price)) + (float(price))    # Hier soll der "new_price" wieder um "price" addiert werden
        print(new_price )
        print(next_price)
        print(count)
tolle_funktion()"""

#prices_list()       # call der function

# Hier die Doofmannlösung
price = 0.79

def counting():
#if count <= 10:
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
#else:
#    print("Done")
counting()

# Ich brauche 2 Funktionen, 1 für die erste "price + price" und eine weitere "next_price"




