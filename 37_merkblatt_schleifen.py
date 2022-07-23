# "for" Schleife
# Eine Schleifenvariable durchläuft nacheinander die Werte einer ebenfalls anzugebenden Sequenz
# Bei der Sequenz kann es sich z.B. um eine Liste handeln. Wir sehen, dass unsere
# Schleifenvariable i nacheinander und automatisch die Werte aus der Liste annimmt.
liste = [5, 8, 10, "Apfelkraut Salami", "Schokopudding"]
for i in liste:        # Schleife für jedes einzelne Element der Liste
    print(i)

# if/else Codeblock wird jeweils nur einmal ausgeführt. Im Gegensatz zur "while" schleife, die endlos läuft

# "while" Schleife, ohne Abbruchbedingung endlos laufend
# Bei Schleifen wie der while-Schleife wird ein Code-Block so lange mehrmals hintereinander ausge-
# führt, bis eine Abbruchbedingung erfüllt ist.
counter = 0     # reset counter

while counter < 5:  # Abbruchbedingung
    print(counter)  # print innerhalb der Schleife
    counter = counter + 1   # raise counter. Zustandsänderung damit die Schleifenbedingung nicht dauerhaft erfüllt ist

print("Drei Chinesen mit dem Kontrabass")   # print ausserhalb der Schleife

# Innerhalb einer Schleife muss sich unbedingt ein Zustand in jedem Schritt verändern, damit die
# Schleifenbedingung nicht dauerhaft erfüllt ist, und das Programm die Schleife auch wieder verlassen
# kann.
piraten = ("Jette","Jan","Hein","Claas","Pit")
i = 0       # Counter reset
while i < len(piraten):     # Anzahl der loops anhand der Länge Liste "piraten", funny!
    print(piraten[i])       # print jedes Element der Liste "piraten" als strg untereinander
    i = i +1                # raise counter. Zustandsänderung damit die Schleifenbedingung nicht dauerhaft erfüllt ist

# range Objekt
# Als Sequenz für eine for-Schleife braucht man nicht zwangsläufig eine Liste. Häufig greift man
# stattdessen auf ein range-Objekt zurück:
print(range(0,5))   # print als strg. Warum auch immer man das braucht.

# range als Schleife
for i in range(0, 5):
    print(i)

# Hier das summieren (Addition aller Werte) der Zahlen von 1 bis 10 mithilfe einer for-Schleife und eines range-Objekt
sum = 0     # Summe wird auf "0" gesetzt
for i in range(1,11):       # Schleife die 10 mal läuft
    sum += i                # Addition der Zahlen von 1 - 10
print(sum)                  # Ergebnis


