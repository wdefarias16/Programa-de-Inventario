import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from style import*


class ProgramasDeUtilidadMenu(ctk.CTkFrame):
    def __init__(self,parent,
                 GoBack_CB,
                 CargaDolar,
                 GestionUsuarios):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.CargaDolar = CargaDolar
        self.GestionUsuarios = GestionUsuarios

    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
        # CONFIGURACION DE ESTILO DEL MENU
        font_menu = tkFont.Font(family="Roboto", size=15)
        self.option_add("*Menu*Font", font_menu)

        # DECLARACION DEL MENU
        menu_bar = tk.Menu(self)

        # CARGA DOLAR
        carga_dolar_menu = tk.Menu(menu_bar,tearoff=0)
        carga_dolar_menu.add_command(label='Carga del dólar',
                                    command = self.CargaDolar)
        # GESTION DE USUARIOS
        gestion_usuarios_menu = tk.Menu(menu_bar,tearoff=0)
        gestion_usuarios_menu.add_command(label='Gestión de usuarios',
                                    command = self.GestionUsuarios)
        
        # AGREGAR A MENU PRINCIPAL
        menu_bar.add_cascade(label='Dólar', menu=carga_dolar_menu)
        menu_bar.add_cascade(label='Usuarios', menu=gestion_usuarios_menu)

        parent.configure(menu=menu_bar)