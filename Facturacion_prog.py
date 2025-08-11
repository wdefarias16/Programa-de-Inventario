import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from PIL import Image, ImageTk
import datetime

class FacturacionProg(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        self.grid_propagate(False)

        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        # GRID SIN ELASTICIDAD
        for r in range(21):
            self.grid_rowconfigure(r,weight=0)
        for c in range(21):
            self.grid_columnconfigure(c,weight=0)
        # FILAS DE ALTURA FIJA, HEADER Y BARRA INFERIOR
        self.grid_rowconfigure(0,weight=0,minsize=100)
        self.grid_rowconfigure(20,weight=0,minsize=10)
        # ZONA DE TRABAJO AJUSTABLE
        for r in range(1,19):
            self.grid_rowconfigure(r, weight=1)
        # COLUMNA LATERAL
        self.grid_columnconfigure(0,  weight=0, minsize=400)  # panel lateral (fijo)
        self.grid_columnconfigure(1,  weight=0)               # margen/col auxiliar si la usas
        for c in range(2, 20):                                # contenido principal (flex)
            self.grid_columnconfigure(c, weight=1)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.grid(row=0,column=0,columnspan=20,sticky='nswe')

        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Ajustes de inventario',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.pack(expand=True)
        # PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - 
        # PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - 
        # FRAME
        self.product_frame = ctk.CTkFrame(self,
                                     width=300,
                                     corner_radius=0,
                                     fg_color=APP_COLOR['main'])
        self.product_frame.grid(row=1,column=0,rowspan=19,sticky='nswe')
        self.product_frame.grid_propagate(False)
        # GRID SET UP
        for r in range(12):
            self.product_frame.rowconfigure(r,weight=1)
        for c in range(5):
            self.product_frame.columnconfigure(c,weight=1)
        # IMAGE
        # PHOTOFRAME
        self.image_path = 'Recursos/Imagenes/Productos'
        default_image = Image.open(f"{self.image_path}/Default.png")
        self.default_image = ctk.CTkImage(light_image=default_image, size=(200,200))
        
        #image_frame = ctk.CTkFrame(self.product_frame,
        #                           corner_radius=0,
        #                           fg_color=APP_COLOR['white_m'])
        #image_frame.grid(row=1,column=1,rowspan=3,columnspan=3)
        
        #self.image_label = ctk.CTkLabel(self.product_frame,
        #                                text='',
        #                                image=self.default_image)
        #self.image_label.grid(row=1,column=0,rowspan=4,columnspan=4)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        main_frame = ctk.CTkFrame(self,
                                     corner_radius=0,
                                     fg_color=APP_COLOR['white_m'])
        main_frame.grid(row=1,column=1,rowspan=19,columnspan=19,sticky='nswe')
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - 
        # FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - 
        footer_frame = ctk.CTkFrame(self,
                                    corner_radius=0,
                                    fg_color=APP_COLOR['sec'])
        footer_frame.grid(row=20,column=0,columnspan=21,sticky='we')
        footer_frame.configure(height=30)
        footer_frame.grid_propagate(False)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------

        btn = ctk.CTkButton(main_frame,
                            text='a',
                            width=10,
                            command=self.visualizar_grilla)
        btn.grid(row=5,column=5)

    def visualizar_grilla(self):
        for r in range(12):
            for c in range(5):
                marcador = ctk.CTkLabel(self.product_frame, text=f"{r},{c}", 
                                        fg_color="#dddddd", 
                                        text_color="gray", 
                                        corner_radius=5)
                marcador.grid(row=r, column=c, sticky="nsew")