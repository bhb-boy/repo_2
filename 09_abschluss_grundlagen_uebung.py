# Aufgabe 1
# Ein automatisierter Trick
# 1.a
number = 6
calc = ((number * 2) + 10) / 2
print(calc)     # number as float

# 1.b
z = int(calc)   # number as integer via casting "int"
print(z)

# 1.c
print("Du hast " + str(number) + " ausgewählt. Das Ergebnis ist: " + str(z) + "!")

# Aufgabe 2
# a. Zersägte E-Mail-Adressen
mail = "bernhard_beetz@gmx.de"      # Alles nach dem "@" abschneiden
thesaw  = mail.split("@")
thesaw.pop()
print(thesaw)

print(mail.split("@")[0])           # Alles in einer Zeile

# b.) Ziehe einen Namen aus einer Domain/TLD
mail = "admin@schlaukraut.net"      # nur schlaukraut heraus extrahieren
frontsaw = mail.split("@")          # Teile bei "@"
cutoff = (frontsaw[1])              # Nur index1 übegeben
s = cutoff                          # Neue Varaible eröffnen. Der ist geklaut
parts = s.split(".")                # domain und tld am Punkt trennen
parts.pop()                         # tld weg schneiden
a = str(parts)                      # str Darstellung
print(a)

print(mail.split("@")[1].split(".")[0])     # Oder alles in einer Zeile, wie in der Lösung

# c.) Wie viele Kunden gibt es im Online-Shop
mail1 = "zarah.zauber@zauberberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_unhold@dunkelnetz.de"

clients = [mail1 , mail2 , mail3]
print(clients)
number_of_elements = len(clients)       # Länge der Liste in eine neue variable
print(number_of_elements)               # print Anzahl der elemente

# Andere Lösung für 2.c mit .append
clients = []
clients.append(mail1)
clients.append(mail2)
clients.append(mail3)
print(clients)
print(len(clients))

# d.) Mailadresse aus Strings zusammenbauen
zauberer = ["Buehnenzauberer", "magic.com", "noch ein furz"]
mailadresse =( zauberer[0] +"@" + zauberer[1])
print(mailadresse)

# Andere Lösung mit .join alle Elemente der Liste mit "@" aneinander hängen
print("@".join(zauberer))
