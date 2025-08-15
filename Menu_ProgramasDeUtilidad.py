import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from tkinter import ttk
from style import*


class ProgramasDeUtilidadMenu(ctk.CTkFrame):
    def __init__(self,parent,
                 GoBack_CB,
                 MaestroDeTablas,
                 CargaDolar):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.MaestroDeTablas = MaestroDeTablas
        self.CargaDolar = CargaDolar

    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
        # CONFIGURACION DE ESTILO DEL MENU
        font_menu = tkFont.Font(family="Roboto", size=15)
        self.option_add("*Menu*Font", font_menu)

        # DECLARACION DEL MENU
        menu_bar = tk.Menu(self)
        # MAESTRO DE TABLAS
        maestro_de_tablas_menu = tk.Menu(menu_bar,tearoff=0)
        maestro_de_tablas_menu.add_command(label='Maestro De Tablas',
                                    command = self.MaestroDeTablas)
        # CARGA DOLAR
        carga_dolar_menu = tk.Menu(menu_bar,tearoff=0)
        carga_dolar_menu.add_command(label='Carga del dólar',
                                    command = self.CargaDolar)
        
        # AGREGAR A MENU PRINCIPAL
        menu_bar.add_cascade(label='Tablas', menu=maestro_de_tablas_menu)
        menu_bar.add_cascade(label='Dólar', menu=carga_dolar_menu)

        parent.configure(menu=menu_bar)