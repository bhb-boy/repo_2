# Vergeleichsoperatoren "and & or"
age = 35
if age >= 30:       # "if" Bedingung >= 30
    if age <= 39:   # "or" Bedingung <= 39
        print("Du bist in den 30er Lebensjahren")

# Verkettung mit "and" Operator, logisch "und"
if age >= 30 and age <= 39:     # Beide Bedingungen müssen erfüllt sein
    print("Du bist in den 30er Lebensjahren")

# Verkettung mit "or" Operator, logisch "oder"
age = 55
if age < 30 or age >= 40:       # Entweder die eine oder die andere Bedingung muss erfüllt sein
    print("Du bist nicht in den 30er Lebensjahren")

# Boolean True/False # Variable auf "1" gesetzt -> SyntaxError: cannot assign to literal. Funzt aber mit Variable in strg
a = False
print(a)
b = True
print(b)

age = 25
above_30 = age >= 30        # Speichere True/False Bedingung in einer Variable
print(above_30)

# Einfachste "if" Abfrage mit True/False
# Bedingung per default immer True?
if True:
    print("if Abfrage wurde ausgeführt")    # Condition "True", print wird ausgeführt
if False:
    print("if Abfrage wurde ausgeführt")    # Condition "False", print wird nicht ausgeführt

age = 55
above_50 = age >= 50    # Boolean return code
print(above_50)         # True

if above_50:            # if Abfrage = True -> print, if Bedingung nicht erfüllt = False -> no print at all
    print("if Abfrage wurde ausgeführt")

# Boolean Logik, concatenation with boolean
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Beispiel: Prüfung ob minderjährig oder nicht
land = "US"
alter = 20
if(land == "US" and alter >=21) or (land != "US" and alter >= 18):  # if
                                                                    # Erste Klammer: True and False = False
                                                                    # or
                                                                    # Zweite Klammer: False and True = False
    print("Du bist Volljährig")                                     # False or False = False - print wird NICHT ausgeführt
