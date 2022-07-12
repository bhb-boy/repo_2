# Vergleichsoperator "not". "if not" ist eine ausführlichere Schreibweise als "<"
alter = 40
if alter >= 50:             # True
    print("Alter ist >= 50")

if not alter >= 50:          # False
    print("if not alter >= 50")

# Ausdruck verhält sich gleich wie in Zeile 6
if alter < 50:
    print("Alter < 50 - Selbe Funktion wie voherige Zeile")

# "not" Operator. Prüfung ob Name in einer Liste ist
piraten = ["jan","hein","claas","pit"]
if "Jette" not in piraten:      # False - Bessere Schreibweise als Zeile 17. Direkte Abfrage an die Liste
    print("Jette ist nicht bei den Piraten")
if not "Jette" in piraten:      # True
    print("Jette ist nicht bei den Piraten")

# Nardo bastelt Beispiele mit strg's und "in" Operator
speisekarte = ["Nudels", "Burger", "Pizza", "Steak"]
if "Fischstäbchen" in speisekarte:      # False
    print("Juhu, es gibt Fischstäbchen")
else:                                   # False
    print("Schade, es gib keine Fischstäbchen")
if not "Fischstäbchen" in speisekarte:  # False
    print("Schade, es gib keine Fischstäbchen")

# Quizaufgabe
# Callcenter Anruf um 2h Nachts. Programm soll prüfen ob innerhalb der Geschäftszeit angerufen wird.
# Der Programmierer hat "and" und "or" verwechselt.

# Beispiel Anruf um 2h Nachts
# hour >= 9 and hour < 16    # False AND True = False | AND Operator is True if Left AND Right are True
# hour >= 9 or hour < 16     # False OR True = True   | OR Operator is True if Left Operator OR Right Operator are True
# Ergebnis des "OR" Fehler: Anruf um 2h wird als innerhalb der Geschäftszeit gewertet

# Beispiel Anruf um 10h
# hour >= 9 and hour < 16    # True AND True = True
# hour >= 9 or hour < 16     # True OR True = True
# Ergebnis des "OR" Fehler: Anruf um 10h wird als innerhalb der Geschäftszeit gewertet, Kein Unterschied von "AND" and "OR"

# Beispiel Anruf um 22h
# hour >= 9 and hour < 16    # True AND False = False
# hour >= 9 or hour < 16    # True OR False = True
# Ergebnis des "OR" Fehler: Anruf um 22h wird als innerhalb der Geschäftszeit gewertet

# Schaff dir einen neuen Programmierer an.