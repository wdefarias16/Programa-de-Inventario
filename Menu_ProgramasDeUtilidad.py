import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from tkinter import ttk
from style import*


class ProgramasDeUtilidadMenu(ctk.CTkFrame):
    def __init__(self,parent,
                 GoBack_CB,
                 MaestroDeTablas):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.MaestroDeTablas = MaestroDeTablas

    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
        # CONFIGURACION DE ESTILO DEL MENU
        font_menu = tkFont.Font(family="Roboto", size=15)
        self.option_add("*Menu*Font", font_menu)

        # DECLARACION DEL MENU
        menu_bar = tk.Menu(self)
        # LINEAS Y GRUPOS
        maestro_de_tablas_menu = tk.Menu(menu_bar,tearoff=0)
        maestro_de_tablas_menu.add_command(label='Maestro De Tablas',
                                    command = self.MaestroDeTablas)
        
        # AGREGAR A MENU PRINCIPAL
        menu_bar.add_cascade(label='Tablas', menu=maestro_de_tablas_menu)

        parent.configure(menu=menu_bar)