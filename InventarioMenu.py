import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from style import*
from Main import App

class InventarioMenu(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
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
                                               corner_radius=0,
                                               button_color=APP_COLORS[0],
                                               button_hover_color=APP_COLORS[6],
                                               fg_color=APP_COLORS[0],
                                               text_color=APP_COLORS[4],
                                               font=FONTS[1],
                                               values=['Entradas de inventario'])
        self.entradas_menu.pack(side='left',padx=2)
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
                                bg_color=APP_COLORS[0],
                                text_color=APP_COLORS[1],
                                font=FONTS[0],
                                height=10)
        head_inv.grid(row=0,column=0,columnspan=3,sticky='nswe')
    # BOTON IR ATRAS
        go_back_btn = ctk.CTkButton(self.head_frame,
                                    text='Ir atras')
        go_back_btn.grid(row=4,column=0)
    # COMANDO VOLVER ATRAS
