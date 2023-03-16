import random

Witze = ["Hast du ein Bad genommen?“ – Warum, fehlt eins?", "Egal, wie gut du schläfst: Albert schläft wie Einstein", 
         "Wissenschaftler haben herausgefunden – und sind wieder reingegangen.",
         "Wie heißt der Schutzpatron der Vergesslichen? – Dings", "Egal wie voll du bist, Rudi war Völler."]

while True:
    witz = random.choice(Witze)
    print(witz)

    antwort = input("Na, noch einen? (ja/nein)")
    if antwort == "nein":
        break