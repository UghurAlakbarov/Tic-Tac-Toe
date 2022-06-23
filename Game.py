import tkinter as tk
from Cell import Cell



class Game(tk.Tk):

    first_players_turn = True


    def __init__(self):
        super().__init__()

        self.resizable(False, False)

        self.init_grid()

    
    def init_grid(self):

        self.configure(background='black')

        # creates 9 cells and puts them on a grid
        self.cells = [[Cell(self, i, j) for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.cells[i][j].grid(
                    row=i,
                    column=j,
                    padx=1,
                    pady=1
                    )
        
        # stores the states of the cells to check for win in the future
        self.cell_states = [['empty' for _ in range(3)] for _ in range(3)]
    

    def check_if_win(self):

        if self.cell_states[0][0] == self.cell_states[1][1] == self.cell_states[2][2] != 'empty': # \
            return True
        if self.cell_states[0][2] == self.cell_states[1][1] == self.cell_states[2][0] != 'empty': # /
            return True
        for i in range(3):
            if self.cell_states[0][i] == self.cell_states[1][i] == self.cell_states[2][i] != 'empty': # |
                return True
            if self.cell_states[i][0] == self.cell_states[i][1] == self.cell_states[i][2] != 'empty': # --
                return True
        return False


    def win(self, who_won):
        self.message = tk.Label(self, text=f'Player {who_won} won!')
        self.message.configure(background='green')
        self.message.grid(row=3, rowspan=1, column=0, columnspan=3)
        for i in range(3):
            for j in range(3):
                self.cells[i][j].states['empty']['state'] = 'disabled'

if __name__ == "__main__":
    ttt = Game()
    ttt.mainloop()
