n = 1980
print(n < 1967)
# True


years = ["Year", "1980","1990"]
print(years)        # return ist eine Liste

for year in years:      # Konvertierung einer Liste in numbers
    if year == "Year":
        continue
    print(int(year))

# Erzeugung einer Liste mit Jahreszahlen, Ausgabe untereinander
for schleife in range(1950,2001):
    print(schleife)

# Ausgabe als Einzeiler
print(*range(1950,2000))
