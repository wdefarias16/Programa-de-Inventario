import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json,os
from style import FONTS, APP_COLORS, APPEARANCE_MODE
from Database import LINE_MANAGER

# PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS
class LineasGruposProg(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de líneas y grupos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=5)
    # LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - 
        lines_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        lines_frame.pack(expand=True,fill='both',side='left')
    # GRID CONFIG
        for rows in range(5):
            lines_frame.rowconfigure(rows, weight=1)
        for columns in range(5):
            lines_frame.columnconfigure(columns,weight=1)
    # TITULO DE LINEA
        label_lin = ctk.CTkLabel(lines_frame,text='Líneas',font=FONTS[0])
        label_lin.grid(row=0,column=2,sticky='nw',pady=20,padx=5)
    # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Buscador de líneas',font=FONTS[1])
        label_lin_cod.grid(row=1,column=1,sticky='n',padx=5)
    # MENU DE LINEAS
        self.lin_menu = ctk.CTkOptionMenu(lines_frame,
                                          values=LINE_MANAGER.GetLineNames())
        self.lin_menu.grid(row=1,column=1,sticky='swe',pady=5)
    # ENTRADA CODIGO DE LINEAS
        self.CodigoEntradaVar = tk.StringVar()
        lin_entry = ctk.CTkEntry(lines_frame,
                                 textvariable=self.CodigoEntradaVar)
        lin_entry.grid(row=1,column=2,sticky='swe',pady=5)
    # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Código de línea',font=FONTS[1])
        label_lin_cod.grid(row=1,column=3,sticky='sw',padx=5)
    # ENTRADA NOMBRE DE LINEA
        self.NombreEntradaVar = tk.StringVar()
        lin_entry_nom = ctk.CTkEntry(lines_frame,
                                     textvariable=self.NombreEntradaVar)
        lin_entry_nom.grid(row=2,column=2,sticky='nwe')
    # LABEL NOMBRE DE LINEA
        label_lin_nom = ctk.CTkLabel(lines_frame,text='Nombre de línea',font=FONTS[1])
        label_lin_nom.grid(row=2,column=3,sticky='nw',padx=5)
    # BOTON AGREGAR
        addl_btn = ctk.CTkButton(lines_frame,
                                 command=self.AgregarLinea,
                                 text='Agregar',
                                 font=FONTS[0])
        addl_btn.grid(row=3,column=2)
    # GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - 
        group_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        group_frame.pack(expand=True,fill='both',side='left')
    # GRID CONFIG
        for rows in range(5):
            group_frame.rowconfigure(rows, weight=1)
        for columns in range(5):
            group_frame.columnconfigure(columns,weight=1)
    # TITULO DE GRUPO
        label_grup = ctk.CTkLabel(group_frame,text='Grupos',font=FONTS[0])
        label_grup.grid(row=0,column=2,sticky='wn',pady=20)
    # ENTRADA DE LINEA
        self.EntradaCodiLinea = tk.StringVar()
        lin_grup_entry = ctk.CTkEntry(group_frame,textvariable=self.EntradaCodiLinea)
        lin_grup_entry.grid(row=1,column=2,sticky='swe',pady=5)
    # LABEL NOMBRE DE LINEA
        label_grup_nom = ctk.CTkLabel(group_frame,text='Indicar código de línea',font=FONTS[1])
        label_grup_nom.grid(row=1,column=3,sticky='sw',pady=5,padx=5)
    # ENTRADA DE GRUPO
        self.EntradaGrupo = tk.StringVar()
        grup_entry = ctk.CTkEntry(group_frame,textvariable=self.EntradaGrupo)
        grup_entry.grid(row=2,column=2,sticky='nwe')
    # LABEL NOMBRE DE GRUPO
        label_grup_nom = ctk.CTkLabel(group_frame,text='Nombre de grupo',font=FONTS[1])
        label_grup_nom.grid(row=2,column=3,sticky='nw',padx=5)
    # BOTON AGREGAR
        addg_btn = ctk.CTkButton(group_frame,
                                 command=self.AgregarGrupo,
                                 text='Agregar',font=FONTS[0])
        addg_btn.grid(row=3,column=2)
# COMANDO BOTON AGREGAR LINEA
    def AgregarLinea(self):
    # OBTENER VALORES DE ENTRADA
        codigo = self.CodigoEntradaVar.get()
        nombre = self.NombreEntradaVar.get()
    # CHEQUEAR VALORES
        if not codigo or not nombre:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        if LINE_MANAGER.Add_Line(codigo,nombre):
            nuevas_lineas = LINE_MANAGER.GetLineNames()
            self.lin_menu.configure(values=nuevas_lineas)
        else:
            messagebox.showerror('Error','No se pudo agregar la linea')
# COMANDO BOTON AGREGAR GRUPO
    def AgregarGrupo(self):
    # OBTENER VALORES DE ENTRADA
        codigo = self.EntradaCodiLinea.get()
        grupo = self.EntradaGrupo.get()
    # CHEQUEAR VALORES
        if not codigo or not grupo:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        LINE_MANAGER.Add_Group(codigo,grupo)