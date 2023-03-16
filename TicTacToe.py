import tkinter as tk

class TicTacToe:
    def __init__(self):
        # Hauptfenster erstellen
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Spielbrett als Liste von 9 Leerzeichen
        self.board = [" " for _ in range(9)]

        # Aktuellen Spieler auf "X" setzen
        self.current_player = "X"

        # Buttons erstellen und ins Grid einfügen
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text=" ",
                    width=10,
                    height=3,
                    command=lambda i=i, j=j: self.on_button_click(i, j)
                )
                button.grid(row=i, column=j)

        # Hauptfenster starten
        self.window.mainloop()

    def on_button_click(self, i, j):
        # Button-Index berechnen und auf Klick reagieren
        index = i * 3 + j
        if self.board[index] == " ":
            # Button aktualisieren und Spielbrett aktualisieren
            self.board[index] = self.current_player
            button = self.window.grid_slaves(row=i, column=j)[0]
            button.config(text=self.current_player)

            # Überprüfen, ob der aktuelle Spieler gewonnen hat
            if self.check_winner():
                self.game_over("Spieler " + self.current_player + " gewinnt!")
            # Überprüfen, ob das Spiel unentschieden ist
            elif all(cell != " " for cell in self.board):
                self.game_over("Unentschieden!")
            else:
                # Spieler wechseln
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Möglichkeiten, um zu gewinnen
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontale Linien
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertikale Linien
            (0, 4, 8), (2, 4, 6)             # diagonale Linien
        ]

        # Überprüfen, ob der aktuelle Spieler gewonnen hat
        for a, b, c in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] == self.current_player:
                return True
        return False

    def game_over(self, message):
        # Informationsfenster anzeigen und Spiel beenden
        tk.messagebox.showinfo("Spiel beendet", message)
        self.window.quit()

# Spiel starten
if __name__ == "__main__":
    TicTacToe()
