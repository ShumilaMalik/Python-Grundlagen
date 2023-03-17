# Initialisiere die Variable gesamtpreis mit 0
gesamtpreis = 0

# Setze die Variable weitere_person auf True, um die Hauptschleife zu starten
weitere_person = True

# Wiederhole die Schleife, bis der Benutzer keine weiteren Personen hinzufügen möchte
while weitere_person:
    # Fordere den Benutzer auf, das Alter der Person einzugeben
    alter = int(input("Bitte geben Sie das Alter ein: "))

    # Überprüfe das Alter und weise den entsprechenden Preis zu
    if 0 <= alter <= 3:
        preis = 0
    elif 4 <= alter <= 11:
        preis = 20
    elif 12 <= alter <= 17:
        preis = 25
    elif alter >= 18:
        preis = 30
    else:
        raise ValueError("Das Alter muss eine positive Zahl sein.")

    # Gebe den Eintrittspreis für das eingegebene Alter aus
    print(f"Der Eintrittspreis für das Alter {alter} beträgt {preis} €.")
    
    # Aktualisiere den Gesamtpreis, indem der Preis der aktuellen Person hinzugefügt wird
    gesamtpreis += preis

    # Frage den Benutzer, ob er eine weitere Person hinzufügen möchte
    antwort = input("Möchten Sie eine weitere Person hinzufügen? (ja/nein): ").lower()

    # Überprüfe die Antwort des Benutzers und beende die Schleife, wenn die Antwort "nein" ist
    if antwort == 'nein':
        weitere_person = False

# Gebe den Gesamtpreis für alle Personen aus
print(f"Der Gesamtpreis für alle Personen beträgt {gesamtpreis} €.")
