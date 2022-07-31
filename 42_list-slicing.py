# list slicing Operatoren. Zugriff auf Elemente in strgs und Listen
program = ["bind","exim","dhcp","hast"]

# greife auf das letzte Element zu
# via Index
print(program[2])       # Funktioniert nur lange wie sich Variable "program" nicht ändert

# via negative als index Position
print(program[-1])      # Funktioniert auch wenn sich die Liste verändert
print(program[-3])

# Jetzt das list slicing
print(program[:]) # Standart Fall ist das erstellen einer Kopie der Varaiable "program"
print(program[0:2]) # print einer Teilliste via index Position. Print ist exklusive der letzten index Position

print(program[1:-1])    # Funzt auch mit negativem Index, wieder exklusive letztem Element

print(program[:-1])     # Selbe Geschichte
print(program[1:])

# strg slicing. Zugriff auf Teilstrings. Der Doppelpunkt defininiert den slicing Wunsch.
print("jan, hein, claas, pit"[0:3])     # character removal via index
print("jan, hein, claas, pit"[-3:])

