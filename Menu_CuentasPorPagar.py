import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from tkinter import ttk
from style import*


class CuentasPorPagarMenu(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB,Proveedores_Prog):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.Proveedores_Prog = Proveedores_Prog

    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
        # CONFIGURACION DE ESTILO DEL MENU
        font_menu = tkFont.Font(family="Roboto", size=15)
        self.option_add("*Menu*Font", font_menu)

        # DECLARACION DEL MENU
        menu_bar = tk.Menu(self)
        # CARGA DEL MAESTRO
        carga_del_maestro_menu = tk.Menu(menu_bar,tearoff=0)
        carga_del_maestro_menu.add_command(label='Carga del maestro',
                                    command = self.Proveedores_Prog)

        # AGREGAR A MENU PRINCIPAL
        menu_bar.add_cascade(label='Carga del maestro', menu=carga_del_maestro_menu)

        # AGREGAR EL MENU A LA PANTALLA
        parent.configure(menu=menu_bar)