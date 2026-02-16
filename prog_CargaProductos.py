import customtkinter as ctk
import tkinter as tk
import os
from tkinter import ttk, filedialog
from PIL import Image, ImageOps
from DB_InventarioProductos import*
from DatabaseManager import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import FONT, APP_COLOR, ICONS
# HELP FUNCS
from Help_Funcs_Products import Products_Help_Window
from Help_Funcs_LinesGroups import Lines_Help_Window, Groups_Help_Window
from Help_Funcs_Provs import Prov_Help_Window

# PROGRAMA DE CARGA DE PRODUCTOS
class CargaProductosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLOR['white_m'])
        self.validatenum = self.register(self.ValidateNum)
        self.treeview_active = False
        self.modprecios_btn_active = False
        self.default_image = 'Recursos/Imagenes/Productos/Default.png'
        self.current_photo = self.default_image
        self.inventario = INVENTARIO.GetCodigos()
        self.PRODUCT = {}
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLOR['sec'])
        title_frame.pack(fill='x')
        # LABEL - LABEL - LABEL - LABEL - LABEL - LABEL - LABEL - 
        title = ctk.CTkLabel(title_frame,
                             text='Carga de productos',
                             bg_color='transparent',
                             text_color=APP_COLOR['white_m'],
                             height=50,
                             font=FONT['title_light'])
        title.pack(pady=10)
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - 
    # CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - 
        self.entry_frame = ctk.CTkFrame(self,
                                   width=400,
                                   fg_color=APP_COLOR['white_m'],
                                   corner_radius=5)
        self.entry_frame.pack(fill='both',expand=True,pady=5)
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - 
    # GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - GRID SETUP - 
        for rows in range(15):
            self.entry_frame.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(10):
            self.entry_frame.columnconfigure(columns,weight=1,uniform='column')
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - 
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.entry_frame,
                                         textvariable=self.codigo_var)
        self.codigo_entry.grid(row=2,column=3,columnspan=2,sticky='nswe',pady=5)
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProducto())
        # LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - 
        self.line_var = tk.StringVar()
        self.linea_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.line_var)
        self.linea_entry.grid(row=3,column=3,columnspan=2,sticky='nswe',pady=5)
        self.linea_entry.bind("<Return>",lambda event:self.Get_Line_By_Code())
        # GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - 
        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.grupo_var)
        self.grupo_entry.grid(row=4,column=3,columnspan=2,sticky='nswe',pady=5)
        self.grupo_entry.bind("<Return>",lambda event:self.Get_Group_By_Code())
        # PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - 
        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.prove_var)
        self.prove_entry.grid(row=5,column=3,columnspan=2,sticky='nswe',pady=5)
        self.prove_entry.bind("<Return>",lambda event:self.Get_Prov_By_Code())
        # NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - 
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.nombre_var)
        self.nombre_entry.grid(row=6,column=3,columnspan=3,sticky='nswe',pady=5)
        self.nombre_entry.bind("<Return>",lambda event:self.costo_entry.focus())
        # COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - 
        self.costo_var = tk.StringVar()
        self.costo_entry = ctk.CTkEntry(self.entry_frame,
                                        validate = 'key',
                                        validatecommand = (self.validatenum,'%P'),
                                        textvariable=self.costo_var)
        self.costo_entry.grid(row=7,column=3,sticky='nswe',pady=5)
        self.costo_entry.bind("<Return>",lambda event:self.ubi1_entry.focus())
        # UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - 
        self.ubi1_var = tk.StringVar()
        self.ubi1_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi1_var)
        self.ubi1_entry.grid(row=8,column=3,columnspan=3,sticky='nswe',pady=5)
        self.ubi1_entry.bind("<Return>",lambda event:self.ubi2_entry.focus())
        # UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - 
        self.ubi2_var = tk.StringVar()
        self.ubi2_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi2_var)
        self.ubi2_entry.grid(row=9,column=3,columnspan=3,sticky='nswe',pady=5)
        self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
        # PRECIO VENTA 1 - PRECIO VENTA 1 - PRECIO VENTA 1 - PRECIO VENTA 1 - 
        self.precio1_var = tk.StringVar()
        self.precio1_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio1_var)
        self.precio1_entry.grid(row=10,column=3,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio1_entry.bind("<Return>",lambda event:self.precio2_entry.focus())
        # PRECIO VENTA 2 - PRECIO VENTA 2 - PRECIO VENTA 2 - PRECIO VENTA 2 - 
        self.precio2_var = tk.StringVar()
        self.precio2_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio2_var)
        self.precio2_entry.grid(row=10,column=4,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio2_entry.bind("<Return>",lambda event:self.precio3_entry.focus())
        # PRECIO VENTA 3 - PRECIO VENTA 3 - PRECIO VENTA 3 - PRECIO VENTA 3 - 
        self.precio3_var = tk.StringVar()
        self.precio3_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio3_var)
        self.precio3_entry.grid(row=10,column=5,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio3_entry.bind("<Return>",lambda event:self.AceptarPrecios())
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
        # DATOS DE PRODUCTO - DATOS DE PRODUCTO - DATOS DE PRODUCTO - 
        he_label = ctk.CTkLabel(self.entry_frame,
                                    text='Datos del producto',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        he_label.grid(row=1,column=3,columnspan=1,sticky='w')
        # IMAGEN - IMAGEN - IMAGEN - IMAGEN - IMAGEN - IMAGEN - 
        image_label = ctk.CTkLabel(self.entry_frame,
                                    text='Imagen del producto',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        image_label.grid(row=1,column=7,columnspan=2,sticky='w')
        # CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - 
        codigo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Código',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        codigo_label.grid(row=2,column=2,columnspan=1,sticky='e',padx=5)
        # LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - 
        linea_label = ctk.CTkLabel(self.entry_frame,
                                    text='Línea',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        linea_label.grid(row=3,column=2,columnspan=1,sticky='e',padx=5)
        # GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - 
        grupo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Grupo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        grupo_label.grid(row=4,column=2,columnspan=1,sticky='e',padx=5)
        # PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - 
        prove_label = ctk.CTkLabel(self.entry_frame,
                                    text='Proveedor Principal',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        prove_label.grid(row=5,column=1,columnspan=2,sticky='e',padx=5)
        # NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - 
        nombre_label = ctk.CTkLabel(self.entry_frame,
                                    text='Nombre',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        nombre_label.grid(row=6,column=2,columnspan=1,sticky='e',padx=5)        
        # COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - 
        costo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Costo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        costo_label.grid(row=7,column=2,columnspan=1,sticky='e',padx=5)
        # UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - 
        ubi1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        ubi1_label.grid(row=8,column=2,columnspan=1,sticky='e',padx=5)
        # UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - 
        ubi2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        ubi2_label.grid(row=9,column=2,columnspan=1,sticky='e',padx=5)
        # PRECIOS - PRECIOS - PRECIOS - PRECIOS - PRECIOS - PRECIOS - 
        precios_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precios de venta',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        precios_label.grid(row=10,column=1,columnspan=2,sticky='e',padx=5)
        # PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - 
        self.precio1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio1_label.grid(row=11,column=3,columnspan=2,sticky='wn',padx=5,pady=2)
        # PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - 
        self.precio2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio2_label.grid(row=11,column=4,columnspan=2,sticky='wn',padx=5,pady=2)
        # PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - 
        self.precio3_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 3',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio3_label.grid(row=11,column=5,columnspan=2,sticky='wn',padx=5,pady=2)
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
        # BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
        self.busqueda_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     image=ICONS['search'],
                                     anchor='w',
                                     width=10,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'],
                                     command = self.Products_Help_Window_CB)
        self.busqueda_btn.grid(row=2,column=5,sticky='nsw',padx=5,pady=5)
        # CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - 
        self.cancelar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Cancelar',
                                     state='disabled',
                                     fg_color=APP_COLOR['red_s'],
                                     hover_color=APP_COLOR['red_s'],
                                     command=self.Restablecer)
        self.cancelar_btn.grid(row=13,column=2,sticky='nswe',padx=4,pady=4)
        # BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - 
        self.find_line_btn = ctk.CTkButton(self.entry_frame,
                                     text='Líneas',
                                     command=self.Lines_Help_Window_CB,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.find_line_btn.grid(row=3,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
        # BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - 
        self.find_group_btn = ctk.CTkButton(self.entry_frame,
                                     text='Grupos',
                                     command=self.Groups_Help_Window_CB,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.find_group_btn.grid(row=4,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
        # BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - 
        self.find_prov_btn = ctk.CTkButton(self.entry_frame,
                                     text='Proveedores',
                                     command=self.Prov_Help_Window_CB,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.find_prov_btn.grid(row=5,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
        # AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - 
        self.add_foto_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar Foto',
                                     command=self.AddPhoto,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.add_foto_btn.grid(row=12,column=3,columnspan=2,sticky='nswe',padx=4,pady=4)
        # GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - 
        self.guardar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'],
                                     command=self.AgregarProducto)
        self.guardar_btn.grid(row=12,column=5,columnspan=2,sticky='nswe',padx=4,pady=4)
        # MODIFICAR - MODIFICAR - MODIFICAR - MODIFICAR - MODIFICAR - MODIFICAR - MODIFICAR - 
        self.modificar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Modificar',
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec'],
                                     command=self.ModificarProducto)
        self.modificar_btn.grid(row=13,column=3,columnspan=2,sticky='nswe',padx=4,pady=4)
        # ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - 
        self.eliminar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLOR['red_s'],
                                     hover_color=APP_COLOR['red_s'],
                                     command=self.EliminarProducto)
        self.eliminar_btn.grid(row=13,column=5,columnspan=2,sticky='nswe',padx=4,pady=4)
        # VOLVER ATRAS - VOLVER ATRAS - VOLVER ATRAS - VOLVER ATRAS - VOLVER ATRAS - 
        salir_btn = ctk.CTkButton(self.entry_frame,
                                     text='Volver atrás',
                                     command=self.GoBack_CB,
                                     text_color=APP_COLOR['white_m'],
                                     fg_color=APP_COLOR['gray'],
                                     hover_color=APP_COLOR['sec'])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5)
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - 
    # PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - 
    # PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - 
    # PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - 
        # IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - 
        self.image_path = 'Recursos/Imagenes/Productos'
        default_image = Image.open(f"{self.image_path}/Default.png")
        self.default_image = ctk.CTkImage(light_image=default_image, size=(250,250))
        # IMAGE FRAME
        self.image_frame = ctk.CTkFrame(self.entry_frame,fg_color=APP_COLOR['white_m'])
        self.image_frame.grid(row=2,column=7,columnspan=2,rowspan=12,sticky='nswe',pady=5)
        # IMAGE LABEL
        self.image_label = ctk.CTkLabel(self.image_frame,
                                        text='',
                                        image=self.default_image)
        self.image_label.pack(side="top", anchor="n",expand=True)
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
    # ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - 
    # ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - 
    def AgregarProducto(self):
        # GET VALUES
        codigo = self.codigo_var.get()
        linea = self.line_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get().split(" - ")[0].strip()
        prove = self.prove_var.get().split(" - ")[0].strip()
        nombre = self.nombre_var.get()
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        image = self.current_photo
        # CHECK CODE
        if codigo == '':
            messagebox.showerror('Error',f"Agregue un codigo de producto.")
            self.codigo_entry.focus()
            return
        # CHECK LINE
        if linea == '' or grupo == '' or prove == '':
            messagebox.showerror('Error',f"Debe agregar línea, Grupo y Proveedor válidos.")
            return
        # CHECK NAME
        if not nombre:
            messagebox.showerror('Error',f'La entrada "Nombre" no puede estar vacia')
            self.nombre_entry.focus()
            return
        # COST TO FLOAT
        try:
            costo = float(self.costo_var.get())
        except Exception as e:
            messagebox.showerror('Error',f'La entrada "Costo" no puede estar vacia')
            self.costo_entry.focus()
            return
        # CHECK COST
        if costo <= 0 or costo == '':
            messagebox.showerror('Error',f'El costo no puede ser menor o igual a 0')
            self.costo_entry.focus()
            return
        # ADD PRODUCT
        if INVENTARIO.CheckCode(codigo) and LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.CheckProv(prove):
            precios = LINE_MANAGER.GetPrecios(linea,grupo,costo)
            producto = Product(
            codigo, linea, grupo, prove, nombre, costo, ubi1, ubi2,
            precios[0], precios[1], precios[2],image=image)
            # MOSTRAR PRECIOS Y PORCENTAJES
            porcentajes = LINE_MANAGER.GetPorcentajes(linea,grupo)
            self.precio1_var.set(precios[0])
            self.precio2_var.set(precios[1])
            self.precio3_var.set(precios[2])
            self.precio1_label.configure(text=f'Precio 1: {porcentajes['porcentaje1']}%')
            self.precio2_label.configure(text=f'Precio 2: {porcentajes['porcentaje2']}%')
            self.precio3_label.configure(text=f'Precio 3: {porcentajes['porcentaje3']}%')
            INVENTARIO.AddProduct(producto.ToDict())
            self.inventario = INVENTARIO.GetCodigos()
            self.Restablecer()
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
# MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - 
# MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - 
    def ModificarProducto(self):
        linea = self.line_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get().split(" - ")[0].strip()
        prove = self.prove_var.get().split(" - ")[0].strip()
        nombre = self.nombre_var.get()
        costo = float(self.costo_var.get())
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        product = INVENTARIO.GetProducto(self.mod_codi)
        image = self.current_photo
        if not costo or costo <= 0:
            messagebox.showerror('Error',f'El costo no puede ser menor o igual a 0')
            return
        if costo != product['costo']:
            precios = LINE_MANAGER.GetPrecios(linea,grupo,costo)
            precio1 = precios[0]
            precio2 = precios[1]
            precio3 = precios[2]
        else:
            precio1 = float(self.precio1_var.get())
            precio2 = float(self.precio2_var.get())
            precio3 = float(self.precio3_var.get())
        # CHECK NAME
        if not nombre:
            messagebox.showerror('Error',f'La entrada "Nombre" no puede estar vacia')
            self.nombre_entry.focus()
            return
        # VALIDATE CHANGES
        anwser = messagebox.askyesno('¡Atención!','¿Está seguro que desea modificar el producto con estos cambios?')
        if not anwser:
            return
        if  LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.CheckProv(prove):
            producto = Product(
            self.mod_codi, linea, grupo, prove, nombre, costo, ubi1, ubi2,
            precio1, precio2, precio3,image=image)
            INVENTARIO.EditProduct(producto.ToDict())
            self.ubi2_entry.unbind("<Return>")
            self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
            self.Restablecer()
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
# DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - 
# DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - 
    def EliminarProducto(self):
        print(self.mod_codi)
        answer1 = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if not answer1:
            return
        answer2 = messagebox.askyesno('Atencion','Esto modificará los datos de inventario.'
                                      ' ¿Está seguro de eliminar el producto?')
        if answer1 and answer2:
            INVENTARIO.DelProduct(self.mod_codi)
            self.Restablecer()
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
# BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - 
# BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - 
    # BUSQUEDA POR CODIGO
    def BuscarProducto(self):
        # IF TREEVIEW IS ACTIVE, GETS THE CODE FROM THAT WINDOW
        if self.treeview_active:
            codigo = self.search_bar_var.get()
            self.treeview_active = False
        # IF TREEVIEW IS NOT ACTIVE, GETS THE CODE FROM MAIN CODE ENTRY
        else:
            codigo = self.codigo_entry.get()
        # VERIFY IF CODE IS INACTIVE
        if INVENTARIO.CheckInactive(codigo):
            self.codigo_var.set('')
            return
        # IF CODE NOT IN INVENTORY, JUMPS TO NEXT ENTRY TO ADD NEW PRODUCT
        if codigo not in self.inventario:
            self.linea_entry.focus()
            return
        # VERIFY CODE IS IN INVENTORY LIST
        if INVENTARIO.CheckCodeValidate(codigo):
            for search in self.inventario:
                if search == codigo:
                    producto = INVENTARIO.GetProducto(search)
        # LLENAR LAS ENTRADAS CON LOS DATOS DE PRODUCTO ELEGIDO
            line = LINE_MANAGER.GetLine(producto['linea'])
            group = LINE_MANAGER.GetGroup(producto['linea'],producto['grupo'])
            prov = PROV_MANAGER.GetProv(producto['proveedor'])
            self.codigo_var.set(producto['codigo'])
            self.line_var.set(f'{line['codigo']} - {line['nombre']}')
            self.grupo_var.set(f'{group['codigo']} - {group['nombre']}')
            self.prove_var.set(f'{prov['codigo']} - {prov['nombre']}')
            self.nombre_var.set(producto['nombre'])
            self.costo_var.set(producto['costo'])
            self.ubi1_var.set(producto['ubicacion1'])
            self.ubi2_var.set(producto['ubicacion2'])
            self.precio1_var.set(producto['precio1'])
            self.precio2_var.set(producto['precio2'])
            self.precio3_var.set(producto['precio3'])
            porcentajes = LINE_MANAGER.GetPorcentajes(line[0],group[0])
            self.precio1_label.configure(text=f'Precio 1: {porcentajes['porcentaje1']}%')
            self.precio2_label.configure(text=f'Precio 2: {porcentajes['porcentaje2']}%')
            self.precio3_label.configure(text=f'Precio 3: {porcentajes['porcentaje3']}%')
            self.ubi2_entry.unbind("<Return>")
            self.ubi2_entry.bind("<Return>",lambda event:self.ModificarProducto())
            self.current_photo = producto['image']
            self.GetImage(self.current_photo)
        # BLOQUEO DE ENTRADAS Y BOTONES
            self.mod_codi = self.codigo_entry.get()
            self.guardar_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
            self.codigo_entry.configure(state='disabled',fg_color='#666')
            self.modificar_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
            self.eliminar_btn.configure(state='enabled',fg_color=APP_COLOR['red_m'],hover_color=APP_COLOR['red_s'])
            self.cancelar_btn.configure(state='enabled',fg_color=APP_COLOR['red_m'])
        # MODIFICAR PRECIOS
            if not self.modprecios_btn_active:
                self.modprecios_btn = ctk.CTkButton(self.entry_frame,
                                             text='Modificar precios',
                                             fg_color=APP_COLOR['main'],
                                             hover_color=APP_COLOR['sec'],
                                             command=self.ModificarPrecios)
                self.modprecios_btn.grid(row=10,column=6,sticky='nswe',padx=4,pady=4)
                self.modprecios_btn_active = True
        else:
            self.linea_entry.focus()
    # BUSQUEDA POR NOMBRE
    def BuscarProductoNombre(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        search = self.search_bar_var.get().lower()
        outcome = INVENTARIO.BuscarNombres(search)
        for product in outcome:
            self.treeview.insert("", 'end',
                                 text=product['codigo'],
                                 values=(product['linea'],
                                         product['grupo'],
                                         product['proveedor'],
                                         product['nombre'],
                                         product['costo']))
# RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - 
# RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - 
    def Restablecer(self):
            if self.modprecios_btn_active:
                self.modprecios_btn.destroy()
                self.modprecios_btn_active = False
            self.guardar_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
            self.add_foto_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
            self.modificar_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
            self.eliminar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
            self.cancelar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
            self.codigo_entry.configure(state='normal',fg_color='#fff')
            self.precio1_entry.configure(state='disabled')
            self.precio2_entry.configure(state='disabled')
            self.precio3_entry.configure(state='disabled')
            self.codigo_var.set('')
            self.line_var.set('')
            self.grupo_var.set('')
            self.prove_var.set('')
            self.nombre_var.set('')
            self.costo_var.set('')
            self.ubi1_var.set('')
            self.ubi2_var.set('')
            self.precio1_var.set('')
            self.precio2_var.set('')
            self.precio3_var.set('')
            self.precio1_label.configure(text='Precio 1')
            self.precio2_label.configure(text='Precio 2')
            self.precio3_label.configure(text='Precio 3')
            self.ubi2_entry.unbind("<Return>")
            self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
            self.codigo_entry.focus()
            self.image_label.configure(image=self.default_image)
            self.current_photo = self.default_image
# MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - 
    def ModificarPrecios(self):
        self.precio1_entry.focus()
        self.precio1_entry.configure(state='normal')
        self.precio2_entry.configure(state='normal')
        self.precio3_entry.configure(state='normal')
        self.codigo_entry.configure(state='disabled',fg_color='#666')
        self.linea_entry.configure(state='disabled',fg_color='#666')
        self.grupo_entry.configure(state='disabled',fg_color='#666')
        self.prove_entry.configure(state='disabled',fg_color='#666')
        self.nombre_entry.configure(state='disabled',fg_color='#666')
        self.costo_entry.configure(state='disabled',fg_color='#666')
        self.ubi1_entry.configure(state='disabled',fg_color='#666')
        self.ubi2_entry.configure(state='disabled',fg_color='#666')
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.find_group_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.find_prov_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.modprecios_btn.configure(state='enabled',
                                   fg_color=APP_COLOR['main'],
                                   text='Guardar precios',
                                   command=self.AceptarPrecios)
        self.add_foto_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
        self.busqueda_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.cancelar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
    # GUARDAR LOS CAMBIOS DE LOS PRECIOS
    def AceptarPrecios(self):
        codigo = self.codigo_var.get()
        p1 = self.precio1_var.get()
        p2 = self.precio2_var.get()
        p3 = self.precio3_var.get()
        INVENTARIO.EditPrecio(codigo,p1,p2,p3)
        self.RestablecerModificarPrecios()
    # RESTABLECER DESPUES DEL CAMBIO DE PRECIOS
    def RestablecerModificarPrecios(self):
        self.modprecios_btn_active = False
        self.modprecios_btn.destroy()
        self.add_foto_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
        self.busqueda_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
        self.find_line_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
        self.find_group_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
        self.find_prov_btn.configure(state='enabled',fg_color=APP_COLOR['main'])
        self.precio1_entry.configure(state='disabled')
        self.precio2_entry.configure(state='disabled')
        self.precio3_entry.configure(state='disabled')
        self.codigo_entry.configure(state='normal',fg_color='#fff')
        self.linea_entry.configure(state='normal',fg_color='#fff')
        self.grupo_entry.configure(state='normal',fg_color='#fff')
        self.prove_entry.configure(state='normal',fg_color='#fff')
        self.nombre_entry.configure(state='normal',fg_color='#fff')
        self.costo_entry.configure(state='normal',fg_color='#fff')
        self.ubi1_entry.configure(state='normal',fg_color='#fff')
        self.ubi2_entry.configure(state='normal',fg_color='#fff')
        self.codigo_var.set('')
        self.line_var.set('')
        self.grupo_var.set('')
        self.prove_var.set('')
        self.nombre_var.set('')
        self.costo_var.set('')
        self.ubi1_var.set('')
        self.ubi2_var.set('')
        self.precio1_var.set('')
        self.precio2_var.set('')
        self.precio3_var.set('')
        self.precio1_label.configure(text='Precio 1')
        self.precio2_label.configure(text='Precio 2')
        self.precio3_label.configure(text='Precio 3')
        self.ubi2_entry.unbind("<Return>")
        self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
        self.codigo_entry.focus()
        self.image_label.configure(image=self.default_image)
        self.current_photo = self.default_image
    # ---------------------------------------------------------------
    # FILL ENTRIES - FILL ENTRIES - FILL ENTRIES - FILL ENTRIES - 
    # ---------------------------------------------------------------
    def Fill_Entry_Fields(self,product_data):
        self.codigo_var.set(product_data['codigo'])
        self.line_var.set(product_data['linea'])
        self.grupo_var.set(product_data['grupo'])
        self.prove_var.set(product_data['proveedor'])
        self.nombre_var.set(product_data['nombre'])
        self.costo_var.set(product_data['costo'])
        self.ubi1_var.set(product_data['ubicacion1'])
        self.ubi2_var.set(product_data['ubicacion2'])
        self.precio1_var.set(product_data['precio1'])
        self.precio2_var.set(product_data['precio2'])
        self.precio3_var.set(product_data['precio3'])
# -------------------------------------------------------------------
# HELP WINDOWS - HELP WINDOWS - HELP WINDOWS - HELP WINDOWS - 
# -------------------------------------------------------------------
    # ---------------------------------------------------------------
    # PRODUCT HELP WINDOW - PRODUCT HELP WINDOW - PRODUCT HELP WINDOW
    # ---------------------------------------------------------------
    def Products_Help_Window_CB(self):
        self.PRODUCT = Products_Help_Window(self)
        if not self.PRODUCT:
            return
        product_data = self.PRODUCT
        self.Fill_Entry_Fields(product_data)
    # ---------------------------------------------------------------
    # LINES HELP WINDOW - LINES HELP WINDOW - LINES HELP WINDOW - 
    # ---------------------------------------------------------------
    def Lines_Help_Window_CB(self):
        LINE = Lines_Help_Window(self)
        if not LINE:
            return
        self.line_var.set(LINE)
    # ---------------------------------------------------------------
    # SEARCH LINE BY CODE - SEARCH LINE BY CODE
    # ---------------------------------------------------------------
    def Get_Line_By_Code(self):
        line_search = self.line_var.get().strip()
        try:
            line_search = int(line_search)
        except Exception as e:
            messagebox.showerror('Error','Error de entrada en línea')
            self.line_var.set('')
            return
        line = LINE_MANAGER.GetLine(line_search)
        if line:
            self.line_var.set(f'{line['codigo']} - {line['nombre']}')
            self.grupo_entry.focus()
        else:
            messagebox.showerror("Base de datos", f"Error al buscar línea: {line_search}")
            self.line_var.set('')
            return
    # ---------------------------------------------------------------
    # GROUP HELP WINDOW - GROUP HELP WINDOW - GROUP HELP WINDOW - 
    # ---------------------------------------------------------------
    def Groups_Help_Window_CB(self):
        try:
            linea_id = int(self.line_var.get().split(' - ')[0])
        except:
            messagebox.showerror('Base de datos.','Seleccione una línea válida.')
            return
        GROUP = Groups_Help_Window(self,linea_id)
        self.grupo_var.set(f'{GROUP['codigo']} - {GROUP['nombre']}')
    # ---------------------------------------------------------------
    # SEARCH GROUP BY CODE - SEARCH GROUP BY CODE
    # ---------------------------------------------------------------
    def Get_Group_By_Code(self):
        line_search = self.line_var.get().split(' - ')[0].strip()
        if line_search:
            line = LINE_MANAGER.GetLine(int(line_search))
            if not line:
                messagebox.showerror("Error", f"Seleccione una linea válida.")
                return
        else:
            messagebox.showerror("Error", f"Seleccione una linea válida.")
            return
        group_search = self.grupo_var.get()
        group_code = str(str(line['codigo']) + '.' + group_search)
        group = LINE_MANAGER.GetGroup(line_search,group_code)
        if group:
            self.grupo_var.set(f'{group['codigo']} - {group['nombre']}')
            self.prove_entry.focus()
        else:
            messagebox.showerror("Base de datos", f"No se encontro el grupo {group_search}")
            self.grupo_var.set('')
            return
    # ---------------------------------------------------------------
    # GROUP HELP WINDOW - GROUP HELP WINDOW - GROUP HELP WINDOW - 
    # ---------------------------------------------------------------
    def Prov_Help_Window_CB(self):
        pass
    # ---------------------------------------------------------------
    # SEARCH PROV BY CODE - SEARCH PROV BY CODE - SEARCH PROV BY CODE
    # ---------------------------------------------------------------        
    def Get_Prov_By_Code(self):
            prov_search = self.prove_var.get().strip()
            try:
                prov_search = int(prov_search)
            except Exception as e:
                messagebox.showerror('Error','Error de entrada en proveedor')
                self.prove_var.set('')
                return
            prov = PROV_MANAGER.GetProv(int(prov_search))
            if prov:
                self.prove_var.set(f'{prov['codigo']} - {prov['nombre']}')
                self.nombre_entry.focus()
            else:
                self.prove_var.set('')
                return
            

    def ValidateNum(self,text):
        text = text.replace(".", "", 1)
        if text == '':
            return True
        return text.isdigit()
# ADD A PHOTO TO A PRODUCT
    def AddPhoto(self):
        # GET THE PRODUCT CODE
        codigo = self.codigo_var.get()
        if not codigo:
            messagebox.showwarning('Atención','Seleccione un producto al que agregar una foto.')
            return
        # OPEN THE SOURCE IMAGE
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
        )
        if not file_path:
            return
        # CONFIGURE IMAGE
        img = Image.open(file_path)
        img = ImageOps.exif_transpose(img)
        w, h = img.size
        # RESIZE
        max_size = 500
        scale = min(max_size / w, max_size / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        # PILLOW FILTER
        try:
            resample_filter = Image.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image.LANCZOS
        # FINAL IMAGE
        img_resized = img.resize((new_w, new_h), resample_filter)
        # SAVE THE IMAGE
        folder = "Recursos/Imagenes/Productos"
        os.makedirs(folder, exist_ok=True)
        file_name = f'{codigo}_img.png'
        save_path = os.path.join(folder, file_name)
        img_resized.save(save_path)
        # TRACE THE CURRENT DISPLAYED IMAGE
        self.current_photo = save_path
        # UPDATE THE LABEL WITH THE NEW IMAGE
        photo = ctk.CTkImage(light_image=img_resized, size=(int(new_w/2),int(new_h/2)))
        self.image_label.configure(image=photo)
    def GetImage(self,image):
        if not image:
            image = 'Recursos/Imagenes/Productos/Default.png'
        img = Image.open(image)
        w, h = img.size

        photo = ctk.CTkImage(light_image=img, size=(int(w/2),int(h/2)))
        self.image_label.configure(image=photo)