# Vergeleichsoperatoren und Listen
# "in" operator: "in" ist gleicher Operatortyp wie: "<", ">", "=", "+"
piraten = ["jan","hein","claas","pit"]
print("hein" in piraten)        # "in" Operator, testet ob Element in einer Liste ist. Output = "True"
print("Jette" in piraten)       # "in" Operator, testet ob Element in einer Liste ist. Output = "False"

# Vergleichsoperatoren mit "if" Abfrage
if "hein" in piraten:           # True
    print("Hein ist mit auf Kaperfahrt")
if "Jette" in piraten:          # False
    print("Jette ist mit auf Kaperfahrt")

# Vergleichsoperatoren mit "if/else" Abfrage
if "claas" in piraten:           # True
    print("Claas ist mit auf Kaperfahrt")
else:                            # "else" Zweig
    print("Claas hat keinen Bock mit zu fahren")

if "Jette" in piraten:          # False
    print("Jette ist mit auf Kaperfahrt")
else:                           # "else" Zweig
    print("Jette bleibt lieber beim MSC")

# Vergleichsoperatoren: Suche nach einem Zeichen in einer Liste strg's
zeichensuche = "Jette ist mit auf Kaperfahrt"
if "?" in zeichensuche:
    print("Der Satz hat ein Fragezeichen")     # False
else:
    print("Der Satz hat kein Fragezeichen")    # True

