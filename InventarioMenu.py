import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from style import*
from Main import App

class InventarioMenu(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB,CargaPro_Prog,Lineas_Prog):
        super().__init__(parent)
    # CALLBACKS
        self.GoBack_CB =  GoBack_CB
        self.CargaPro_Prog = CargaPro_Prog
        self.Lineas_Prog = Lineas_Prog

        
    # MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - MENU OPCIONES - 
    # MENU FRAME
        frame_menu = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        frame_menu.pack(side='top',fill='x')
    # OPCIONES - OPCIONES - OPCIONES - 
    # LISTADOS
        self.listados_menu = ctk.CTkOptionMenu(frame_menu,
                                               corner_radius=0,
                                               button_color=APP_COLORS[0],
                                               button_hover_color=APP_COLORS[6],
                                               fg_color=APP_COLORS[0],
                                               text_color=APP_COLORS[4],
                                               font=FONTS[1],
                                               values=['Listados'])
        self.listados_menu.pack(side='left',padx=2)
    # CONSULTAS
        self.consultas_menu = ctk.CTkOptionMenu(frame_menu,
                                                corner_radius=0,
                                                button_color=APP_COLORS[0],
                                                button_hover_color=APP_COLORS[6],
                                                fg_color=APP_COLORS[0],
                                                text_color=APP_COLORS[4],
                                                font=FONTS[1],
                                                values=['Consultas'])
        self.consultas_menu.pack(side='left',padx=2)
    # AJUSTES
        self.ajustes_menu = ctk.CTkOptionMenu(frame_menu,
                                              corner_radius=0,
                                              button_color=APP_COLORS[0],
                                              button_hover_color=APP_COLORS[6],
                                              fg_color=APP_COLORS[0],
                                              text_color=APP_COLORS[4],
                                              font=FONTS[1],
                                              values=['Ajustes'])
        self.ajustes_menu.pack(side='left',padx=2)
    # ENTRADAS DE INVENTARIO
        self.entradas_menu = ctk.CTkOptionMenu(frame_menu,
                                               command=self.Entradas,
                                               corner_radius=0,
                                               button_color=APP_COLORS[0],
                                               button_hover_color=APP_COLORS[6],
                                               fg_color=APP_COLORS[0],
                                               text_color=APP_COLORS[4],
                                               font=FONTS[1],
                                               values=['Entradas de inventario',
                                                       'Carga de líneas y grupos'])
        self.entradas_menu.pack(side='left',padx=2)
    # BOTON IR ATRAS
        go_back_btn = ctk.CTkButton(frame_menu,
                                    command=lambda: self.GoBack_CB(),
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3],
                                    text_color=APP_COLORS[0],
                                    corner_radius=0,
                                    text='Ir atras')
        go_back_btn.pack(side='right')
    # DASHBOARD INVENTARIO - DASHBOARD INVENTARIO - DASHBOARD INVENTARIO - DASHBOARD INVENTARIO - 
    # FRAME
        self.head_frame = ctk.CTkFrame(self,
                                       height=600,
                                       corner_radius=0,
                                       fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')
    # GRID SETUP
        for rows in range(5):
            self.head_frame.rowconfigure(rows,weight=1)
        for columns in range(5):
            self.head_frame.columnconfigure(columns,weight=1)
    # TITULO
        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Inventario',
                                fg_color=APP_COLORS[2],
                                text_color=APP_COLORS[0],
                                font=FONTS[0],
                                height=30)
        head_inv.grid(row=0,column=0,columnspan=5,sticky='nwe',pady=10)
    

# COMANDOS MENUS
    def Entradas(self,opcion):
        if opcion == 'Entradas de inventario':
            self.CargaPro_Prog()
        if opcion == 'Carga de líneas y grupos':
            self.Lineas_Prog()


