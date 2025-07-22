import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, APP_COLORS, ICONS

class MaestroDeTablas_prog(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)

        self.GoBack_CB = GoBack_CB

        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLORS[3],
                                   corner_radius=0,
                                   height=50)
        title_frame.pack(fill='x')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Maestro de tablas',
                                   bg_color='transparent',
                                   text_color=APP_COLORS[0],
                                   font=FONT['title_light'])
        title_label.pack(pady=10)
        # PROG FRAME
        self.prog_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.prog_frame.pack(expand=True,fill='both',side='left')
        self.prog_frame.bind("<Return>",lambda event:self.ProductsHelp())

        # GRID SETUP
        ROWS, COLUMNS = 20, 12
        for rows in range(ROWS):
            self.prog_frame.rowconfigure(rows,weight=1,uniform='a')
        for columns in range(COLUMNS):
            self.prog_frame.columnconfigure(columns,weight=1,uniform='a')

    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
        