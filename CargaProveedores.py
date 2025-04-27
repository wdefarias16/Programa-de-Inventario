import customtkinter as ctk
import tkinter as tk
import json,os
from tkinter import messagebox
from Database import PROV_MANAGER
from style import FONTS, APP_COLORS, APPEARANCE_MODE

# PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - 
class ProveedoresProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de proveedores',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=5)
    # FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - 
        prov_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        prov_frame.pack(expand=True,fill='both',side='left')
    # GRID SETUP
        for rows in range(5):
            prov_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(5):
            prov_frame.columnconfigure(columns,weight=1,uniform='column')
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
    # LABEL DE DATOS
        label_lin = ctk.CTkLabel(prov_frame,
                                     text='Datos del proveedor',
                                     font=FONTS[1])
        label_lin.grid(row=1,column=2,sticky='wn',pady=10,padx=5)
    # LABEL MENU
        label_lin_cod = ctk.CTkLabel(prov_frame,
                                     text='Buscador de proveedores',
                                     font=FONTS[1])
        label_lin_cod.grid(row=1,column=1,sticky='wn',padx=5,pady=10)
    # LABEL CODIGO DE PROVEEDOR
        label_lin_cod = ctk.CTkLabel(prov_frame,text='Código de proveedor',font=FONTS[1])
        label_lin_cod.grid(row=1,column=3,sticky='sw',padx=5)
    # LABEL NOMBRE DE LINEA
        label_lin_nom = ctk.CTkLabel(prov_frame,text='Nombre de proveedor',font=FONTS[1])
        label_lin_nom.grid(row=2,column=3,sticky='nw',padx=5)
    # MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - 
    # MENU DE PROVEEDORES
        self.lin_menu = ctk.CTkOptionMenu(prov_frame,
                                          command=self.SelectProv,
                                          values=PROV_MANAGER.GetProvNames())
        self.lin_menu.grid(row=1,column=1,sticky='swe',pady=5,padx=5)
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
    # ENTRADA CODIGO DE PROVEEDOR
        self.CodigoEntradaVar = tk.StringVar()
        self.prov_entry = ctk.CTkEntry(prov_frame,
                                       fg_color=APP_COLORS[0],
                                       textvariable=self.CodigoEntradaVar)
        self.prov_entry.grid(row=1,column=2,sticky='swe',pady=5)
    # ENTRADA NOMBRE DE LINEA
        self.NombreEntradaVar = tk.StringVar()
        lin_entry_nom = ctk.CTkEntry(prov_frame,
                                     fg_color=APP_COLORS[0],
                                     textvariable=self.NombreEntradaVar)
        lin_entry_nom.grid(row=2,column=2,sticky='nwe')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
    # AGREGAR
        self.addl_btn = ctk.CTkButton(prov_frame,
                                 command=self.AgregarProv,
                                 text='Agregar',
                                 font=FONTS[1])
        self.addl_btn.grid(row=3,column=1,columnspan=3,padx=5,pady=5,sticky='nsew')
    # MODIFICAR
        self.mod_btn = ctk.CTkButton(prov_frame,
                                 command=self.Modificar,
                                 text='Modificar',
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 font=FONTS[1])
        self.mod_btn.grid(row=4,column=1,padx=5,pady=5,sticky='nsew')
    # ELIMINAR
        self.del_btn = ctk.CTkButton(prov_frame,
                                 command=self.Eliminar,
                                 text='Eliminar',
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 font=FONTS[1])
        self.del_btn.grid(row=4,column=2,padx=5,pady=5,sticky='nsew')
    # VOLVER ATRAS 
        self.del_btn = ctk.CTkButton(prov_frame,
                                 command=lambda:self.GoBack_CB,
                                 text='Volver Atrás',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 font=FONTS[1])
        self.del_btn.grid(row=0,column=1,padx=5,pady=5)
    # CANCELAR
        self.cancel_btn = ctk.CTkButton(prov_frame,
                                 command=self.Restablecer,
                                 text='Cancelar',
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 font=FONTS[1])
        self.cancel_btn.grid(row=4,column=3,padx=5,pady=5,sticky='nsew')
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# SELECCIONAR PROVEEDOR
    def SelectProv(self,opcion):
    # LLENAR LAS ENTRADAS CON LOS DATOS DEL PROVEEDOR
        self.CodigoEntradaVar.set(opcion.split(' - ')[0])
        self.NombreEntradaVar.set(opcion.split(' - ')[1])
    # ACTIVAR MODO DE EDICION
        self.addl_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.cancel_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.prov_entry.configure(state='disabled',fg_color='#666')
# RESTABLECER A MODO AGREGAR
    def Restablecer(self):
        self.CodigoEntradaVar.set('')
        self.NombreEntradaVar.set('')
        self.addl_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancel_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.prov_entry.configure(state='normal',fg_color=APP_COLORS[0])
# COMANDO AGREGAR PROVEEDOR
    def AgregarProv(self):
        codigo = self.CodigoEntradaVar.get()
        nombre = self.NombreEntradaVar.get()
        if not codigo or not nombre:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        if PROV_MANAGER.Add_Prov(codigo,nombre):
            nuevos_provs = PROV_MANAGER.GetProvNames()
            self.lin_menu.configure(values=nuevos_provs)
            self.Restablecer()
        else:
            messagebox.showerror('Error','No se pudo agregar El proveedor')
# COMANDO MODIFICAR PROVEEDOR
    def Modificar(self):
        codigo = self.CodigoEntradaVar.get()
        nombre = self.NombreEntradaVar.get()
        if not nombre:
            messagebox.showerror('Error','Debe ingresar un nombre.')
            return
        PROV_MANAGER.Mod_Prov(codigo,nombre)
        nuevos_provs = PROV_MANAGER.GetProvNames()
        self.lin_menu.configure(values=nuevos_provs)
        self.Restablecer()
# COMANDO ELIMINAR PROVEEDOR
    def Eliminar(self):
        codigo = self.CodigoEntradaVar.get()
        answer = messagebox.askyesno('¡Atención!','¿Está seguro que desea eliminar '
                                     f'el proveedor {codigo}?')
        if answer:
            PROV_MANAGER.Del_Prov(codigo)
            nuevos_provs = PROV_MANAGER.GetProvNames()
            self.lin_menu.configure(values=nuevos_provs)
            self.Restablecer()