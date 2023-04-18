import tkinter as tk
from tkinter import messagebox
from ia import Ia

X_PLAYER = "X"
O_PLAYER = "O"
BUTTON_WIDTH = 3
BUTTON_HEIGHT = 1


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = X_PLAYER
        self.game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text="", font=("Arial", 30),
                                   width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                                   command=lambda row=row, col=col: self.handle_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
            self.is_vs_computer = True #ajoute un drapeau pour indiquer si on joue contre l'ordi

    def handle_click(self, row, col):
        if self.check_winner() or self.check_tie():
            return
        if self.game_board[row][col] == "":
            self.game_board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player, state="disabled")
        if self.check_winner():
            self.show_winner()
        elif self.check_tie():
            self.show_tie()
        else:
            self.switch_player()
            if self.current_player == O_PLAYER:  # Si c'est le tour de l'IA
                position = Ia(self.game_board, O_PLAYER)  # Appeler la fonction ia pour déterminer où l'IA veut jouer
                if position is False:  # Si la fonction ia retourne False, il y a eu une erreur
                    messagebox.showerror("Erreur", "L'IA a rencontré une erreur.")
                    return
                row, col = position // 3, position % 3  # Convertir la position en une ligne et une colonne
                self.game_board[row][col] = O_PLAYER  # Mettre à jour le plateau de jeu avec le choix de l'IA
                self.buttons[row][col].configure(text=O_PLAYER, state="disabled")
                if self.check_winner():
                    self.show_winner()
                elif self.check_tie():
                    self.show_tie()
                else:
                    self.switch_player()

    def switch_player(self):
        if self.current_player == X_PLAYER:
            self.current_player = O_PLAYER
        else:
            self.current_player = X_PLAYER

    def check_winner(self):
        for i in range(3):
            if (self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != "" or
                    self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != ""):
                return True
        if (self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != "" or
                self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != ""):
            return True
        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] == "":
                    return False
        return True

    def show_winner(self):
        winner = self.current_player
        tk.messagebox.showinfo("Winner", f"{winner} has won the game!")
        self.reset_game()

    def show_tie(self):
        tk.messagebox.showinfo("Tie", "The game is a tie!")
        self.reset_game()

    def reset_game(self):
        self.current_player = X_PLAYER
        self.game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()