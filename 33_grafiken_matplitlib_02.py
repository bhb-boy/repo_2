import matplotlib.pyplot as plt

# In die Liste xs packen wir die ganzzahligen Werte von -10 bis 10
xs = []
for x in range(-10, 11):
    xs.append(x)

# In die Liste ys packen wir die Quadratzahlen zu jedem Wert aus der Liste xs
ys = []
for x in xs:
    ys.append(x * x)

# In die Liste ys packen wir die Kubikzahlen zu jedem Wert aus der Liste xs
ys2 = []
for x in xs:
    ys2.append(x * x * x)


# Wir geben die Listen xs, ys, ys2 nacheinander aus
print(xs)
print(ys)
print(ys2)

# Wir plotten ys und ys2 jeweils gegen xs
plt.plot(xs, ys)
plt.plot(xs, ys2)
plt.show()