# 2. Aufgabe: Rabattaktion
# a.) Gib für die Variable price den neuen, rabattierten Preis aus.
# 0 und 20 (einschließlich) Taler kosten, werden um 20 % reduziert.
# zwischen 20 (nicht einschließlich) und 50 Taler (einschließlich) kosten, werden um 40 % reduziert.
# Alle anderen Artikel, die mehr als 50 Taler kosten, werden um 60 % reduziert.
# 1a.) Gib für die Variable price den neuen, rabattierten Preis aus.
price = 50

if price <=20:
       print("Es gibt 20% Rabbat")
elif price <= 50:
       print("Es gibt 40& Rabbat")
else:                           # Else hat keine Bedingung!
       print("Es gibt 60% Rabbat")

# b.) Berechne nun für jeden der alten Preise aus der Liste prices die
# passenden reduzierten Preise und speichere sie in der neuen Liste
# new_prices. Gib diese Liste schließlich aus."""

prices = [2, 50, 70, 30]
new_prices =[]
print("Hier die rabbatierten Preise je nach Kaufpreishöhe")
for price in prices:
    if price <= 20:     # Bedingung
        lowrabbat = (price / 100 * 80)
        new_prices.append(lowrabbat)
    elif price <= 50:   # Bedingung
        midrabbat = (price / 100 * 60)
        new_prices.append(midrabbat)
    else:               # Else hat keine Bedingung!
        highrabbat = (price / 100 * 40)
        new_prices.append(highrabbat)
print(new_prices)

# 2c.) Zusatzaufgabe
# Gehe die Elemente in der Liste chaos durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem
# String und hängst ihn der Liste order an.
# Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst diesen Wert an die Liste order.
# Schließlich gibst du die vollständige Liste order aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).
# Mit Hilfe des in - Operators kannst du prüfen, ob old oder new in einem Listenelement vorkommt ("old" in "old price: 123"),

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []
newprice = []
oldprice = []
list_to_process = []

# Sortierung der Liste "chaos" in "old price" und "new price" Listen
for match in chaos:                      # Filtert aus der Liste "chaos" bestimmte Elemente (old/new) und verteilt sie auf separate Listen
    if "new price" in match:             # Search for strg "new price" in Liste "chaos
        newprice.append(match)           # Append search strg "new price" to list "newprice"
    else:
        oldprice.append(match)           # Append every other strg to list "oldprice"

print("Artikelpreise mit reduziertem Preis werden direkt an die Liste order angehängt")
for each_value in newprice:                 # Schleife über newprice
    newprice_list = each_value              # Ergebnis der Schleife an "newprice_list" übergeben
    newprice_value = newprice_list[11:14]   # Aus "newprice_list" nur den Zahlenwert an "newprice_value" übergeben [11:14]
    print(newprice_value)                   # Zeilenweise Darstellung der Zahlen in "newprice_value"
    order.append(newprice_value)            # Artikel mit reduziertem Preis als strg anhängen an die Liste "order"

print("Artikelpreise mit nicht reduziertem Preis müssen erst neu berechnet un dann an die Liste order angehängt werden")
for each_value in oldprice:                 # Schleife über oldprice
    oldprice_list = each_value              # Ergebnis der Schleife an "oldprice_list" übergeben
    oldprice_value = oldprice_list[11:13]   # Aus "oldprice_list" nur den Zahlenwert an "oldprice_value" übergeben [11:13]
    print(oldprice_value)                   # Zeilenweise Darstellung der Zahlen in "oldprice_value"
    list_to_process.append(oldprice_value)  # Übergabe der zu bearbeitenden Werte aus der Liste "old_price_value" an "list_to_process"
print("Hier die Liste der neu zu berechnenden Werte als strg's")
print(list(list_to_process))
print("Hier die rabbatierten Preise je nach Kaufpreishöhe")
for price in (list_to_process):
    if int(price) <= 20:     # Bedingung
        lowrabbat = (int(price) / 100 * 80)
        print(lowrabbat)
        order.append(lowrabbat)
    elif int(price) <= 50:   # Bedingung
        midrabbat = (int(price) / 100 * 60)
        print(midrabbat)
        order.append(midrabbat)
    else:               # Else hat keine Bedingung!
        highrabbat = (int(price) / 100 * 40)
        print(highrabbat)
        order.append(highrabbat)
print("Hier die fertige order Liste order")
print(order)

print("beep!")

# Udemy lösung für die schwierige Aufgabe  ------------------------------------------------------------------------
# Mit PyCharm will diese Lösung nicht. Man beachte "price *= 0.8". Dort hängt sich PyCharm auf
chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for i in chaos:     # Zu Beginn eine "for" Schleife. Hier wird der Delimitter ": " verwendet
    print(i.split(": "))

    price = int((i.split(": ")[1]))    # Zerlegung des Listenelements in einzelne String Elemente

    if "old" in i:          # Preisanpassung nur bei Artikeln die "old" enthalten
        if price <= 20:
            price *= 0.8
        elif price <= 50:
            price *= 0.6
        else:
            price *= 0.4

    order.append(price)
print(order)
