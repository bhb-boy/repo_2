# list comprehension
# Umwandlung von mehreren Listen in ene einzelne Liste

# Beispiel Berechnung Numbers in Liste num² Bisher mit "for" Schleife"
xs = [1,2,3,4,5,6,7,8]
ys = []
for i in xs:
    ys.append(i * i)    # Quadrat von Listenelement an Liste "ys" anhängen
print(xs)
print(ys)

# List comprehension Schreibweise. Schreibweise die es kompakter macht.
xs = [1,2,3,4,5,6,7,8]

ys = [x * x for x in xs]  # Eckige Klammer -> erstelle eine leere Liste. x mal x für jedes x in der Liste "xs"

print(xs)
print(ys)

# Beispiel Anzahl der Zeichen in den strgs einer Liste
piraten = ["jan","hein","claas","pit"]

alle_piraten = []   # Leere Liste erstellen
for pirat in piraten:           # Das ist ein funny trick. Wieso weiß python das pirat ein einzelnes Element in der
                                # Liste piraten ist?
    alle_piraten.append(len(pirat)) # Hängt die Zeichenlänge der strgs an Liste "alle_piraten" an.

print(alle_piraten)

# Selbes Beispiel mit List comprehension anstatt "for" Schleife.
alle_piraten = [len(pirat) for pirat in piraten]  # Zeichenlänge jedes Elements in Liste "piraten" []

print(alle_piraten)

# List comprehension für Graphen, zuerst wieder als "for" Schleife
import matplotlib.pyplot as plt
xs = []         # Array mit xs Werten
for i in range(0,100):   # Zähle Zahlen von 0 bis 100 hoch, kann von range aber nicht parameter übergeben werden
                         # und muss daher in eine neue Variable übergeben werden
    xs.append(i / 10)    # Teile jeden Wert aus range durch 10
print(xs)

# List comprehension für Graphen, jetzt als list comprehension
xs = [i / 10 for i in range(0,100)] # Teile jedes Element aus Range durch 10. Hier wird die Auflösung des Graphen gesteuert
ys = [i * i for i in xs]            # Quadrat von jedem Element
print(xs)
print(ys)

plt.plot(xs,ys)
plt.show()
