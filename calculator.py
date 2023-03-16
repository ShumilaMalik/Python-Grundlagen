import tkinter as tk

class Calculator:
    def __init__(self):
        # Hauptfenster erstellen
        self.window = tk.Tk()
        self.window.title("Taschenrechner")

        # Eingabefeld für die Rechnung erstellen
        self.expression = ""
        self.entry = tk.Entry(self.window, width=40)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons erstellen und ins Grid einfügen
        self.create_buttons()

        # Hauptfenster starten
        self.window.mainloop()

    def create_buttons(self):
        # Zahlen- und Funktionsbuttons erstellen
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        # Buttons zum Hauptfenster hinzufügen
        for (text, row, column) in buttons:
            button = tk.Button(
                self.window,
                text=text,
                width=10,
                height=3,
                command=lambda text=text: self.on_button_click(text)
            )
            button.grid(row=row, column=column)

        # Clear-Button hinzufügen
        clear_button = tk.Button(
            self.window,
            text="C",
            width=10,
            height=3,
            command=self.clear_expression
        )
        clear_button.grid(row=5, column=0)

    def on_button_click(self, text):
        # Auf Klicks der Buttons reagieren
        if text == "=":
            self.calculate_expression()
        else:
            self.expression += text
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear_expression(self):
        # Ausdruck löschen
        self.expression = ""
        self.entry.delete(0, tk.END)

    def calculate_expression(self):
        # Ausdruck berechnen und Ergebnis anzeigen
        try:
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = ""
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Fehler")

# Taschenrechner starten
if __name__ == "__main__":
    Calculator()
