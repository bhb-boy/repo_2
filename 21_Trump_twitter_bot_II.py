       # Trump Twitter Bot
import random
part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

# Listen von Listen erstellen. Alle strg's aus allen Listen
best_words = [part1, part2, part3, part4]

# for Schleife über "best_words" print Länge (len) und die einzelnen strg's

sentence = []                           # Variable "sentence" um aus der random Liste einen Satz zu bauen
for part in best_words:                 # Schleifenbegriff "part" für Liste aller strg's in "best_words"
    r = random.randint(0, len(part) - 1)   # Zufallsgenerator zwischen erstem strg [0] und letztem strg [-1]
                                        # Achtung: part dient als Platzhalter für part1-4, funny trick!
                                        # Mit [-1] werden elegant die unterschiedlich langen Listen abgefangen.
    sentence.append(part[r])            # Fülle Liste "sentence". Hänge die random Begriffe aus "r" aneinander
print(" ".join(sentence))               # Ausgabe ist eine Liste. Mit " " als Leerzeichen und ".join" wird ein kompletter
                                        # Satz gebaut.

teil1 = ["Die Chefetage", "Der Vertrieb", "Die nutzlosen IT'ler", "Der Kunde", "Die vom Betriebsrat" ]
teil2 = ["asap", "at the end of the day", "muss back to the Drawing Board","Da müssen wir proaktiv ran"]
teil3 = ["Kickoff-Meeting","Jour Fixe", "Project-Recap", "compliance-konform"]
teil4 = ["Low-Hanging-Fruits","No-Brainer","Showstopper","Learnings"]
teil5 = ["Da bin ich fine mit", "unsere PS auf die Straße bringen", "Wir müssen richtig Gas geben","Wir alle, ein Team!"]
teil6 = []

# Änderung vom Lenovo Notebook