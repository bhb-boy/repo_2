# 01_listspy
# http://localhost:8888/notebooks/Listen%20in%20Python.ipynb
metalbands = ["Metallica","AC/DC","Bolt Thrower","Meshugga"]
noten = [3,4,5,2,2,1]

print(metalbands)
print(metalbands[2])

print(metalbands[1] + " & " + metalbands[-1])

metalbands.append("Hirschi")
print(metalbands[4])

metalbands.pop()
print(metalbands)

# Notendurchschnitt aus einer integer liste
print((noten[0] + noten[1] + noten[2] + noten[3] + noten[4] + noten[5]) / 6)

# Anzahl von Elementen in einer Liste
print(len(metalbands))
