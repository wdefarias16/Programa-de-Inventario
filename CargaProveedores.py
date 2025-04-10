import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json,os
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class Proveedores():
    def __init__(self,filename = 'Data/Proveedores.json'):
    
        self.filename = filename
        self.proveedores = {}
        self.Load_Prov()

    # CARGAR EL ARCHIVO DE DATOS
    def Load_Prov(self):
        # CREAR LA CARPETA DATA SI NO EXISTE
        if not os.path.exists('Data'):
            os.makedirs('Data')
        # VERIFICAR SI EXISTE EL ARCHIVO DE DATOS / CARGAR EL ARCHIVO DE DATOS
        try:
            with open(self.filename,'r') as file:
                self.proveedores = json.load(file)
        except FileNotFoundError:
            self.proveedores={}
            self.Save_Prov()

    # GUARDAR EL ARCHIVO DE DATOS
    def Save_Prov(self):
        with open(self.filename,'w') as file:
            json.dump(self.proveedores,file,indent=4)


    def GetProvNames(self):
        return [f"{codigo} - {info['proveedor']}" for codigo, info in self.proveedores.items()]
    
    def Add_Prov(self,codigo,nombre):
        if codigo in self.proveedores:
            messagebox.showerror('Error',f'El proveedor {codigo} ya se encuentra en la base de datos')
            return False
        
        self.proveedores[codigo]={'proveedor': nombre}
        self.Save_Prov()
        messagebox.showinfo('Info',f'El proveedor {codigo} se ha cargado correctamente')
        return True

# PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - 
class ProveedoresProg(ctk.CTkFrame):
    def __init__(self,parent,prov_manager:Proveedores):
        super().__init__(parent)

        self.prov_manager = prov_manager

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

        # LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - 
        
        lines_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        lines_frame.pack(expand=True,fill='both',side='left')
        
        for rows in range(5):
            lines_frame.rowconfigure(rows, weight=1)
        for columns in range(5):
            lines_frame.columnconfigure(columns,weight=1)

        # TITULO DE LINEA
        label_lin = ctk.CTkLabel(lines_frame,text='Datos del proveedor',font=FONTS[0])
        label_lin.grid(row=0,column=2,sticky='nw',pady=20,padx=5)

        # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Buscador de proveedores',font=FONTS[1])
        label_lin_cod.grid(row=1,column=1,sticky='n',padx=5)

        # MENU DE LINEAS
        self.lin_menu = ctk.CTkOptionMenu(lines_frame,
                                          values=self.prov_manager.GetProvNames())
        self.lin_menu.grid(row=1,column=1,sticky='swe',pady=5)

        # ENTRADA CODIGO DE LINEAS
        self.CodigoEntradaVar = tk.StringVar()
        lin_entry = ctk.CTkEntry(lines_frame,
                                 textvariable=self.CodigoEntradaVar)
        lin_entry.grid(row=1,column=2,sticky='swe',pady=5)

        # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Código de proveedor',font=FONTS[1])
        label_lin_cod.grid(row=1,column=3,sticky='sw',padx=5)

        # ENTRADA NOMBRE DE LINEA
        self.NombreEntradaVar = tk.StringVar()
        lin_entry_nom = ctk.CTkEntry(lines_frame,
                                     textvariable=self.NombreEntradaVar)
        lin_entry_nom.grid(row=2,column=2,sticky='nwe')
        
        # LABEL NOMBRE DE LINEA
        label_lin_nom = ctk.CTkLabel(lines_frame,text='Nombre de proveedor',font=FONTS[1])
        label_lin_nom.grid(row=2,column=3,sticky='nw',padx=5)

        # BOTON AGREGAR
        addl_btn = ctk.CTkButton(lines_frame,
                                 command=self.AgregarProv,
                                 text='Agregar',
                                 font=FONTS[0])
        addl_btn.grid(row=3,column=2)

    # FUNCION DE BOTON AGREGAR PROVEEDOR
    def AgregarProv(self):
        codigo = self.CodigoEntradaVar.get()
        nombre = self.NombreEntradaVar.get()
    
        if not codigo or not nombre:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        if self.prov_manager.Add_Prov(codigo,nombre):
            nuevos_provs = self.prov_manager.GetProvNames()
            self.lin_menu.configure(values=nuevos_provs)
        else:
            messagebox.showerror('Error','No se pudo agregar El proveedor')
    


PROV_MANAGER = Proveedores()