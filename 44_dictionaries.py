# Dictionries

dictionary = {"Berlin": "BER", "Helsinki": "HEL","Saigon":"SGN"} # Zuordnung KEY:VALUE

print(dictionary["Berlin"])    # Abfrage, Key auf key/value pair

# append. Hinzufügen von key/value pairs. Sortierung geht möglicherweise verloren.
dictionary["Budapest"] = "BUD"

print(dictionary)

# remove eines key
del dictionary["Budapest"]

print(dictionary)

# Abfrage per "if" Schleife nach key in dictionary
if "Budapest" in dictionary:            # "in" Operator. Sucht nach key, nicht nach value!
    print("Budapest ist im dictionary")
if "Saigon" in dictionary:
    print("Saigon ist im dictionary")

# Zugriff auf ELemente mit .get
# Die .get Funktion Schreibweise in () droppt keinen Fehler beim Zugriff. Zugriff mit [] stürzt ab.
print(dictionary.get("Saigon"))    # ausgabe des value von key "Saigon"

# Best practice ist das Program zum Absturz zu bringen. Ansonsten ist Fehlersuche irgendwann unübersichtlich.



