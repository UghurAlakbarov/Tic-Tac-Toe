import tkinter as tk
from tkinter import ttk


class Cell(ttk.Frame):
    

    def __init__(self, master, row, column):
        super().__init__(master)

        self.master = master

        # stores the coordinates of the cell to check for win in future
        self.row = row
        self.column = column

        self.state_of_cell = 'empty'

        # stores the images in a dict so that they don't get GC'd
        self.images = {}
        
        # creates three buttons representing three states of the cell
        self.states = {}
        for cell_state in ['x', 'o', 'empty']:
            photo=tk.PhotoImage(file=f'assets/{cell_state}.png')
            self.states[cell_state] = ttk.Button(
                self,
                image=photo,
                command=lambda state_of_cell=cell_state : self.cell_clicked(state_of_cell)
            )
            self.images[cell_state] = photo
        
        self.states['empty'].pack()


    def change_button_to(self, cell_state):
        # replaces the empty cell with X/O 
        self.states['empty'].pack_forget()
        self.states[cell_state].pack()
        self.master.cell_states[self.row][self.column] = cell_state
  
        
    def cell_clicked(self, state_of_cell):
        # places X/O if the cell is empty
        if state_of_cell == 'empty':
            if self.master.first_players_turn:
                self.change_button_to('x')
            else:
                self.change_button_to('o')
        
        # checks for a possible W and initializes the appropriate win screen
        if self.master.check_if_win():
            if self.master.first_players_turn:
                self.master.win(1)
            else:
                self.master.win(2)
        
        # switches the player
        self.master.first_players_turn = not self.master.first_players_turn

