import customtkinter as ctk
import tkinter as tk

fonts = [('Roboto light',25),('Roboto light',15)]
app_colors = ['#eaeaea','#1d1d1d','#1c9bac','#166c78','#5d5d5d']

class Inicio(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)