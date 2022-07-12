students = ["jan","hein","claas","pit"]
print("#".join(students)) # .join -> Liste hintereinander hängen mit "#" als delimitter

print(", ".join(students)) # .join -> Liste hintereinander hängen mit "," als delimitter

studends_as_string = ", ".join(students)
print(studends_as_string + " fahren auf Kaperfahrt mit")    # Verarbeitung einer Liste als strg

# strg to list convert
i = "jan, hein, claas, pit"
print(i.split(", "))    # split: Zerlege die Liste mit überall wo ", " vorkommt
                        # Der print kommt in [], also als Liste in ie Ausgabe

#sabbel = "Ich erzähl den ganzen Tag nur dummes Zeug"
#h = sabbel.split(" ")   # strg in liste umgewandelt
#print(len(h.count(" ")))

sabbel = "Ich erzähl den ganzen Tag nur dummes Zeug"
print(len(sabbel.split(" ")))       # len function -> Zähle die Anzahl der Wörter

