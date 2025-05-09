import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from tkinter import ttk
from style import*


class InventarioMenu(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB,CargaPro_Prog,Lineas_Prog,EntradasInv_prog):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.CargaPro_Prog = CargaPro_Prog
        self.Lineas_Prog = Lineas_Prog
        self.EntradasInv_prog = EntradasInv_prog


        
    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
        # CONFIGURACION DE ESTILO DEL MENU
        font_menu = tkFont.Font(family="Roboto", size=15)
        self.option_add("*Menu*Font", font_menu)

        # DECLARACION DEL MENU
        menu_bar = tk.Menu(self)
        # LINEAS Y GRUPOS
        lineasgrupos_menu = tk.Menu(menu_bar,tearoff=0)
        lineasgrupos_menu.add_command(label='Carga de líneas y grupos',
                                    command = self.Lineas_Prog)
        # MAESTRO DE INVENTARIO
        inventario_menu = tk.Menu(menu_bar,tearoff=0)
        inventario_menu.add_command(label='Carga de productos',
                                    command = self.CargaPro_Prog)
        # LISTADOS
        listados_menu = tk.Menu(menu_bar,tearoff=0)
        listados_menu.add_command(label='Listados')
        # CONSULTAS
        consultas_menu = tk.Menu(menu_bar,tearoff=0)
        consultas_menu.add_command(label='Consultas')
        # AJUSTES
        ajustes_menu = tk.Menu(menu_bar,tearoff=0)
        ajustes_menu.add_command(label='Ajustes')
        # ENTRADAS DE INVENTARIO
        entradas_menu = tk.Menu(menu_bar,tearoff=0)
        entradas_menu.add_command(label='Entradas de inventario',
                                  command=self.EntradasInv_prog)
        # AGREGAR A MENU PRINCIPAL
        menu_bar.add_cascade(label='Líneas y grupos', menu=lineasgrupos_menu)
        menu_bar.add_cascade(label='Maestro de inventario', menu=inventario_menu)
        menu_bar.add_cascade(label='Listados', menu=listados_menu)
        menu_bar.add_cascade(label='Consultas', menu=consultas_menu)
        menu_bar.add_cascade(label='Ajustes', menu=ajustes_menu)
        menu_bar.add_cascade(label='Entradas de Inventario', menu=entradas_menu)

        


        parent.configure(menu=menu_bar)