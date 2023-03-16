# 1. Erstelle eine Liste “Kleiderschrank” mit den Elementen: Hose, T-Shirt, Kleid
kleiderschrank = ["Hose", "T-Shirt", "Kleid"]

# 2. Erstelle eine Liste "Kommode" mit den Elementen: Schuhe, Socken, Muetzen
kommode = ["Schuhe", "Socken", "Muetzen"]

# 3. Lass dir jedes Element deines “Kleiderschranks” einzeln ausgeben
for element in kleiderschrank:
    print(element)

# 4. Lass dir alle Elemente  deines “Kleiderschranks” über eine For-Schleife ausgeben
# (Bereits in Schritt 3 erledigt)

# 5. Es ist kalt im Winter. Füge deinem Kleiderschrank einen Pullover hinzu.
kleiderschrank.append ("Pullover")

# 6. Du verkaufst die Kommode. Füge den Inhalt der Komode dem Kleiderschrank hinzu
kleiderschrank.extend(kommode)

# Ausgabe des aktualisierten Kleiderschranks
print("Aktualisierter Kleiderschrank:", kleiderschrank)

#print(type(kleiderschrank))
