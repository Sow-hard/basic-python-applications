import tkinter as tk
from tkinter import messagebox
import sys

class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.buttons = {}
        for i in range(3):
            for j in range(3):
                b = tk.Button(self.window, text="", font=("Helvetica", 60), width=3, height=2, 
                              command=lambda x=i, y=j: self.click(x,y))
                b.grid(row=i, column=j)
                self.buttons[(i,j)] = b
        
        self.player = "X"
        
        tk.Label(text="Player: " + self.player, font=("Helvetica", 30)).grid(row=3, column=0, columnspan=3)
        
        self.window.mainloop()

    def click(self, i, j):
        if self.buttons[(i,j)]["text"] == "":
           self.buttons[(i,j)]["text"] = self.player
           
           if self.check_win():
               self.show_game_over(self.player)
           else:
               if self.player == "X":
                   self.player = "O"
               else:
                   self.player = "X"
               tk.Label(text="Player: " + self.player, font=("Helvetica", 30)).grid(row=3, column=0, columnspan=3)

    def check_win(self):
        # Check for winner
        for i in range(3):
            if self.buttons[(i,0)]["text"] == self.buttons[(i,1)]["text"] == self.buttons[(i,2)]["text"] != "":
                return True
        
        for j in range(3):
            if self.buttons[(0,j)]["text"] == self.buttons[(1,j)]["text"] == self.buttons[(2,j)]["text"] != "":
                return True

        if self.buttons[(0,0)]["text"] == self.buttons[(1,1)]["text"] == self.buttons[(2,2)]["text"] != "":
            return True
        if self.buttons[(0,2)]["text"] == self.buttons[(1,1)]["text"] == self.buttons[(2,0)]["text"] != "":
            return True
        
        return False

    def show_game_over(self, winner):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Game Over", winner + " won!")
        sys.exit()
        
game = TicTacToe()