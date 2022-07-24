# Funktionen: Bei ihrem Aufruf stehen Funktionen "für sich" und das, worauf sie sich beziehen steht ggf.
# als Argument in den Klammern hinter ihnen:

fingerspiel = ["schnick","schnack","schnuck"]
print(len(fingerspiel))     # Beispiel "len" funktion
# print()
# set()
# len()
# slice()
# input()
# split()
# sum()
# eval()
# format()
# Full documentation: https://docs.python.org/3/library/functions.html


# Methoden
# Daneben kennen wir aber auch schon Befehle, die mit einem Punkt an Objekte angehängt werden. Eine Liste ist ein
# solches Objekt. Jedes Objekt hat Methoden, auf die wir zurückgreifen können. Diese Methoden können wir aber nicht
# auf ein Objekt eines anderen Typs anwenden (meistens zumindest).
# Beispiel:
# .append - anhängen, doppelte sind zugelassen liste2.append(4)
# .pop  - letztes element entfernen liste3.pop(2)
# .join - anhängen, doppelte sind nicht zugelassen
# .insert - einsetzen via index liste4.insert(1, 4)
# .remove - entfernen via index liste5.remove(4)
# .reverse - umkehren einer Liste liste7.reverse()
# .index - print(liste6.index(3)) ???
# .count - print(liste.count(4)) ???