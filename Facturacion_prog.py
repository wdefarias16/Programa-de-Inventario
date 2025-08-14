import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from PIL import Image, ImageTk
import datetime

class FacturacionProg(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   width=1500,
                                   height=60,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.place(relx=0.5,rely=0,anchor='n')

        # LABEL
        '''title_label = ctk.CTkLabel(title_frame,
                                   text='Facturación',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.pack(fill='both', expand=False)'''
   