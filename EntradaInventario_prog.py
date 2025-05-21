import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from DatabaseManager import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import FONTS, APP_COLORS, APPEARANCE_MODE

# PROGRAMA DE CARGA DE PRODUCTOS
class EntradasInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.goback_CB = GoBack_CB

        self.configure(fg_color=APP_COLORS[0])
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')

        title = ctk.CTkLabel(title_frame,
                             text='Entradas a inventario',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=10)
    # PROG FRAME
        prog_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        prog_frame.pack(expand=True,fill='both',side='left')
    # GRID SETUP
        for rows in range(18):
            prog_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(8):
            prog_frame.columnconfigure(columns,weight=1,uniform='column')