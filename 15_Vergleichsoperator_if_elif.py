# Währungsrechner mit "else" Verzweigung
currency = "sad"
if currency == "$":
    print("US-Dollar")
else:
    if currency == "¥":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "฿":
                print("Thai Bath")
            else:
                print("Unknown currency")
# Währungsrechner mit "elif" Verzweigung.Gleiche Wirkung, code ist sauberer durch weniger indentation
currency = "asd"
if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Baht")
else:
    print("Unbekannte Währung")
