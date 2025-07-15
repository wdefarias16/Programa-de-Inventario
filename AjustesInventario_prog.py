import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from style import*



class AjustesInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0],corner_radius=0)
        # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # GRID SETUP
        for rows in range(30):
            self.rowconfigure(rows,weight=1,uniform='rows')
        for columns in range(12):
            self.columnconfigure(columns,weight=1,uniform='columns')  
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE
        # TITLE FRAME
        title_frame = ctk.CTkFrame(self,fg_color=APP_COLORS[3],corner_radius=0)
        title_frame.grid(row=0,column=0,rowspan=2,columnspan=12,sticky='nswe')
        # TITLE LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Ajustes de Inventario',
                                   text_color=APP_COLORS[0],
                                   bg_color='transparent',
                                   font=FONTS[0])
        title_label.pack(expand=True,fill='both',padx=5)
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # NUMERO DE DOCUMENTO
        self.num_fact_entry = ctk.CTkEntry(self,
                                           )
        self.num_fact_entry.grid(row=4,column=1,columnspan=2,sticky='ew')
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
        # NUMERO DE DOCUMENTO
        num_fact_label = ctk.CTkLabel(self,text='Documento',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        num_fact_label.grid(row=3,column=1,columnspan=2,sticky='w')

