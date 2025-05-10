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
        for rows in range(18):
            prov_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(6):
            prov_frame.columnconfigure(columns,weight=1,uniform='column')
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # CODIGO
        validarcodigo = self.register(self.ValidarCodigo)
        self.codigo_entry_var = tk.IntVar()
        self.codigo_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.codigo_entry_var,
                                         validate='key',
                                         validatecommand = (validarcodigo,'%P'),
                                         fg_color=APP_COLORS[6])
        self.codigo_entry.grid(row=2,column=2,columnspan=2,sticky='we',padx=5)
        # NOMBRE
        self.nombre_entry_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.nombre_entry_var,
                                         fg_color=APP_COLORS[6])
        self.nombre_entry.grid(row=3,column=2,columnspan=2,sticky='we',padx=5)
        # CONTACTO
        self.contacto_entry_var = tk.StringVar()
        self.contacto_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.contacto_entry_var,
                                         fg_color=APP_COLORS[6])
        self.contacto_entry.grid(row=4,column=2,columnspan=2,sticky='we',padx=5)
        # DIRECCION 1
        self.direccion1_entry_var = tk.StringVar()
        self.direccion1_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion1_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion1_entry.grid(row=5,column=2,columnspan=2,sticky='we',padx=5)
        # DIRECCION 2
        self.direccion2_entry_var = tk.StringVar()
        self.direccion2_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion2_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion2_entry.grid(row=6,column=2,columnspan=2,sticky='we',padx=5)
        # CIUDAD
        self.ciudad_entry_var = tk.StringVar()
        self.ciudad_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.ciudad_entry_var,
                                         fg_color=APP_COLORS[6])
        self.ciudad_entry.grid(row=7,column=2,columnspan=2,sticky='we',padx=5)
        # TELEFONO
        self.telefono_entry_var = tk.StringVar()
        self.telefono_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.telefono_entry_var,
                                         fg_color=APP_COLORS[6])
        self.telefono_entry.grid(row=8,column=2,columnspan=2,sticky='we',padx=5)
        # CELULAR
        self.celular_entry_var = tk.StringVar()
        self.celular_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.celular_entry_var,
                                         fg_color=APP_COLORS[6])
        self.celular_entry.grid(row=9,column=2,columnspan=2,sticky='we',padx=5)
        # EMAIL
        self.email_entry_var = tk.StringVar()
        self.email_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.email_entry_var,
                                         fg_color=APP_COLORS[6])
        self.email_entry.grid(row=10,column=2,columnspan=2,sticky='we',padx=5)
        # RIF
        self.rif_entry_var = tk.StringVar()
        self.rif_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.rif_entry_var,
                                         fg_color=APP_COLORS[6])
        self.rif_entry.grid(row=11,column=2,columnspan=2,sticky='we',padx=5)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # TITULO
        self.titulo_label = ctk.CTkLabel(prov_frame,
                                        text='Cargar datos del proveedor',
                                        font=FONTS[1])
        self.titulo_label.grid(row=1,column=2,sticky='w',padx=5)
        # CODIGO
        self.codigo_label = ctk.CTkLabel(prov_frame,
                                        text='Código',
                                        font=FONTS[1])
        self.codigo_label.grid(row=2,column=4,sticky='w',padx=5)
        # NOMBRE
        self.nombre_label = ctk.CTkLabel(prov_frame,
                                        text='Nombre',
                                        font=FONTS[1])
        self.nombre_label.grid(row=3,column=4,sticky='w',padx=5)
        # CONTACTO
        self.contacto_label = ctk.CTkLabel(prov_frame,
                                        text='Contacto',
                                        font=FONTS[1])
        self.contacto_label.grid(row=4,column=4,sticky='w',padx=5)
        # DIRECCION 1
        self.direccion1_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 1',
                                        font=FONTS[1])
        self.direccion1_label.grid(row=5,column=4,sticky='w',padx=5)
        # DIRECCION 2
        self.direccion2_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 2',
                                        font=FONTS[1])
        self.direccion2_label.grid(row=6,column=4,sticky='w',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONTS[1])
        self.ciudad_label.grid(row=7,column=4,sticky='w',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONTS[1])
        self.ciudad_label.grid(row=7,column=4,sticky='w',padx=5)
        # TELEFONO
        self.telefono_label = ctk.CTkLabel(prov_frame,
                                        text='Teléfono',
                                        font=FONTS[1])
        self.telefono_label.grid(row=8,column=4,sticky='w',padx=5)
        # CELULAR
        self.celular_label = ctk.CTkLabel(prov_frame,
                                        text='Celular',
                                        font=FONTS[1])
        self.celular_label.grid(row=9,column=4,sticky='w',padx=5)
        # EMAIL
        self.email_label = ctk.CTkLabel(prov_frame,
                                        text='Email',
                                        font=FONTS[1])
        self.email_label.grid(row=10,column=4,sticky='w',padx=5)
        # RIF
        self.rif_label = ctk.CTkLabel(prov_frame,
                                        text='RIF',
                                        font=FONTS[1])
        self.rif_label.grid(row=11,column=4,sticky='w',padx=5)
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        self.goback_btn = ctk.CTkButton(prov_frame,
                                     text='Volver atrás',
                                     command=self.GoBack_CB,
                                     fg_color=APP_COLORS[4],
                                     hover_color=APP_COLORS[3])
        self.goback_btn.grid(row=0,column=0,sticky='we',padx=5,pady=5)
        # AGREGAR
        self.agregar_btn = ctk.CTkButton(prov_frame,
                                     text='Agregar',
                                     command=self.AgregarProv,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.agregar_btn.grid(row=13,column=2,sticky='we',padx=5,pady=5)
        # CANCELAR
        self.cancelar_btn = ctk.CTkButton(prov_frame,
                                     text='Cancelar',
                                     command=self.Cancelar,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.cancelar_btn.grid(row=13,column=3,sticky='we',padx=5,pady=5)
        # MODIFICAR
        self.mod_btn = ctk.CTkButton(prov_frame,
                                     text='Modificar',
                                     command=self.ModificarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.mod_btn.grid(row=14,column=2,sticky='we',padx=5,pady=5)
        # ELIMINAR
        self.del_btn = ctk.CTkButton(prov_frame,
                                     text='Eliminar',
                                     command=self.EliminarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.del_btn.grid(row=14,column=3,sticky='we',padx=5,pady=5)
# COMANDOS DE BOTONES
    def AgregarProv(self):
        pass
    def ModificarProv(self):
        pass
    def EliminarProv(self):
        pass
    def Cancelar(self):
        self.codigo_entry_var.set('0')
        self.nombre_entry_var.set('')
        self.contacto_entry_var.set('')

    
    # VALIDAR ENTRADA DE CODIGO
    def ValidarCodigo(self,texto):
        if len(texto) > 3:
            return False
        if texto == '':
            return True
        return texto.isdigit()