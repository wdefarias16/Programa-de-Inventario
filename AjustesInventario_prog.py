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


