import customtkinter as ctk
import tkinter as tk
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class LineasGrupos(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        lineas_frame = ctk.CTkFrame(self)
        lineas_frame.pack(expand=True,fill='both')

        grupos_frame = ctk.CTkFrame(self)
        grupos_frame.pack(expand=True,fill='both')