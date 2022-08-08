# Dictionaries und Schleifen
dictionary = {"Berlin": "BER", "Helsinki": "HEL","Saigon":"SGN"} # Zuordnung KEY:VALUE.

for key in dictionary:
    value = dictionary[key]     # Zugriff auf den Value des Dict. per "for" Schleife und der variable "value"
    print(key)      # Zugriff auf den Key Print des Key als Strg untereinander
    print(value)    #

# .items Funktion
print(dictionary.items())   # Rückabewert ähnlich einer Liste von Tuples

# Entpacken der variable "dictinary" in untereinander stehenden Key/Value Paaren
for key, value in dictionary.items():   # Ausgabe der key/value Paare als strgs untereinander
    print(key + ": " + value)           # Key af der linken Seite, value auf der rechten Seite


