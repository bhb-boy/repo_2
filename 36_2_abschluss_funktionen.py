# Schreibe eine Funktion, die die Listen mit den Artikeln auffüllt!
# Von nun an soll auch eine Funktion die Waren in die virtuellen Regale einräumen, d. h. an die erste, noch
# leere Position in der Liste shelf packen. Als Parameter soll der Funktion add_shelf() der einzusortierende
# Artikel übergeben werden. Die Funktion aktualisiert dann die Liste shelf, und der neue Artikel wurde in das
# erste leere Regalfach eingeräumt.

shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickkarten", "leer"]

def add_shelf(article):
    for i in range(0, len(shelf)):
        print(i)                # Anzahl der Durchgänge, abhängig von der Anzahl der Elemente in "i"
        print(shelf[i])         # Funny! print der Liste "shelf" als strgs untereinander, nicht in einer Zeile []

    for i in range(0, len(shelf)):
        if shelf[i] == "leer":  # Hier wird der Begriff "leer" in der Liste gesucht ("==")
            shelf[i] = article  # Zuweisung. Hier wird der Begriff "leer" ersetzt durch den Funktionsinhalt
                                # aus "add_shelf" ("=")
            break               # Das "break" sorgt für den Abbruch nach dem ersten Treffer

add_shelf("Rubik's Cube")       # Hier wird "Rubik's Cube" an die Funktion "add_shelf" übergeben
print(shelf)