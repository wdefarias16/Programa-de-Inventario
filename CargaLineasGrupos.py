import customtkinter as ctk
import tkinter as tk
from style import FONTS, APP_COLORS, APPEARANCE_MODE



class LineasGrupos():
    def __init__(self):
    
        self.lineas_grupos = {'001': {'linea': 'Bebidas',
                                 'grupo': ['Jugos', 'Alcohol', 'Refrescos']},
                         '002': {'linea': 'Almuerzos',
                                 'grupo': ['Pizzas', 'Hamburguesas', 'Parrillas']}}


    def GetLineNames(self):
        nombre_lineas = [f"{codigo} - {dato['linea']}" for codigo, dato in self.lineas_grupos.items()]
        return nombre_lineas
    

    def AddLineGroup(self,codigo,linea,grupo):
        pass

# OBTENER NOMBRES DE LINEA


class LineasGruposProg(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,rowspan=1,columnspan=5,sticky='nswe')

        title = ctk.CTkLabel(title_frame,
                             text='Carga de lineas y grupos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack()

        # LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - 
        self.rowconfigure((0,1),weight=1)
        for rows in range(2,13):
            self.rowconfigure(rows, weight=1)
        for columns in range(5):
            self.columnconfigure(columns,weight=1)

        # TITULO DE LINEA
        label_lin = ctk.CTkLabel(self,text='Lineas',font=FONTS[0])
        label_lin.grid(row=1,column=2,sticky='w',pady=5,padx=5)

        # MENU DE LINEAS
        lin_menu = ctk.CTkOptionMenu(self,values=nombre_lineas)
        lin_menu.grid(row=2,column=1,sticky='nswe',pady=5)

        # ENTRADA CODIGO DE LINEAS
        lin_entry = ctk.CTkEntry(self)
        lin_entry.grid(row=2,column=2,sticky='nswe',pady=5)

        # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(self,text='Codigo de linea',font=FONTS[1])
        label_lin_cod.grid(row=2,column=3,sticky='w',padx=5)

        # ENTRADA NOMBRE DE LINEA
        lin_entry_nom = ctk.CTkEntry(self)
        lin_entry_nom.grid(row=3,column=2,sticky='nswe')
        
        # LABEL NOMBRE DE LINEA
        label_lin_nom = ctk.CTkLabel(self,text='Nombre de linea',font=FONTS[1])
        label_lin_nom.grid(row=3,column=3,sticky='w',padx=5)


        # GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - 
        
        # TITULO DE GRUPO
        label_grup = ctk.CTkLabel(self,text='Grupos',font=FONTS[0])
        label_grup.grid(row=5,column=2,sticky='w')

        # ENTRADA DE GRUPO
        grup_entry = ctk.CTkEntry(self)
        grup_entry.grid(row=6,column=2,sticky='nswe')

        # LABEL NOMBRE DE GRUPO
        label_grup_nom = ctk.CTkLabel(self,text='Agregar grupo',font=FONTS[1])
        label_grup_nom.grid(row=6,column=3,sticky='w',padx=5)

        # BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - BOTON AGREGAR - 
        
        add_btn = ctk.CTkButton(self,text='Agregar',font=FONTS[0])
        add_btn.grid(row=8,column=4)

lineas = LineasGrupos()
nombre_lineas= lineas.GetLineNames()