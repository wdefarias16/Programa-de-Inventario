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
        # --------------------------------------------------------------------------------
        # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO 
        # --------------------------------------------------------------------------------
        # FRAME
        title_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['sec'],
                        corner_radius=0,)
        title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
        title_label = ctk.CTkLabel(title_frame,
                        text='Carga de productos',
                        text_color=APP_COLOR['white_m'],
                        font=FONT['title_bold'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
        home_btn = ctk.CTkButton(title_frame,
                        image=ICONS['home'],
                        text='',
                        width=30,
                        height=30,
                        fg_color=APP_COLOR['gray'],
                        hover_color=APP_COLOR['black_m'])
        home_btn.place(relx=0.05,rely=0.5,anchor='center')
        # GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON -
        self.go_back_btn = ctk.CTkButton(title_frame,
                text='',
                image=ICONS['home'],
                width=30,
                height=30,
                text_color=APP_COLOR['black_m'],
                font=FONT['text_small'],
                fg_color=APP_COLOR['gray'],
                hover_color=APP_COLOR['main'],
                command=lambda: self.GoBack_CB())
        self.go_back_btn.place(relx=0.1,rely=0.5,anchor='center')
        # --------------------------------------------------------------------------------
        self.SetInicio()
    "Inicializar la interfaz"
    def SetInicio(self):
        # ------------------------------------------------------------------------
        # ENTRY FRAME - ENTRY FRAME - ENTRY FRAME - ENTRY FRAME - ENTRY FRAME - 
        # ------------------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLOR['white_m'],
                                   corner_radius=0)
        self.entry_frame.place(relx=0,rely=0.1,relwidth=1,relheight=0.9,anchor='nw')
        # --------------------------------------------------------------------------------
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - 
        # -------------------------------------------------------------------------------- 
        # CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - 
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.entry_frame,
                                         textvariable=self.codigo_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.codigo_entry.place(relx=0.35,rely=0.2,relwidth=0.1,anchor='w')
        self.codigo_entry.bind("<Return>",lambda event:self.Get_Product_By_Code())
        # LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - 
        self.line_var = tk.StringVar()
        self.linea_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.line_var,
                                   fg_color=APP_COLOR['light_gray'],
                                   border_color=APP_COLOR['light_gray'])
        self.linea_entry.place(relx=0.35,rely=0.26,relwidth=0.1,anchor='w')
        self.linea_entry.bind("<Return>",lambda event:self.Get_Line_By_Code())
        # GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - 
        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.grupo_var,
                                   fg_color=APP_COLOR['light_gray'],
                                   border_color=APP_COLOR['light_gray'])
        self.grupo_entry.place(relx=0.35,rely=0.32,relwidth=0.1,anchor='w')
        self.grupo_entry.bind("<Return>",lambda event:self.Get_Group_By_Code())
        # PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - 
        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.prove_var,
                                   fg_color=APP_COLOR['light_gray'],
                                   border_color=APP_COLOR['light_gray'])
        self.prove_entry.place(relx=0.35,rely=0.38,relwidth=0.1,anchor='w')
        self.prove_entry.bind("<Return>",lambda event:self.Get_Prov_By_Code())
        # NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - 
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.nombre_var,
                                    fg_color=APP_COLOR['light_gray'],
                                    border_color=APP_COLOR['light_gray'])
        self.nombre_entry.place(relx=0.35,rely=0.44,relwidth=0.25,anchor='w')
        self.nombre_entry.bind("<Return>",lambda event:self.costo_entry.focus())
        # COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - 
        self.costo_var = tk.StringVar()
        self.costo_entry = ctk.CTkEntry(self.entry_frame,
                                        validate = 'key',
                                        fg_color=APP_COLOR['light_gray'],
                                        border_color=APP_COLOR['light_gray'],
                                        validatecommand = (self.validatenum,'%P'),
                                        textvariable=self.costo_var)
        self.costo_entry.place(relx=0.35,rely=0.5,relwidth=0.1,anchor='w')
        self.costo_entry.bind("<Return>",lambda event:self.ubi1_entry.focus())
        # UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - 
        self.ubi1_var = tk.StringVar()
        self.ubi1_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi1_var,
                                   fg_color=APP_COLOR['light_gray'],
                                   border_color=APP_COLOR['light_gray'])
        self.ubi1_entry.place(relx=0.35,rely=0.56,relwidth=0.25,anchor='w')
        self.ubi1_entry.bind("<Return>",lambda event:self.ubi2_entry.focus())
        # UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - 
        self.ubi2_var = tk.StringVar()
        self.ubi2_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi2_var,
                                   fg_color=APP_COLOR['light_gray'],
                                   border_color=APP_COLOR['light_gray'])
        self.ubi2_entry.place(relx=0.35,rely=0.62,relwidth=0.25,anchor='w')
        self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
        # PRECIO VENTA 1 - PRECIO VENTA 1 - PRECIO VENTA 1 - PRECIO VENTA 1 - 
        self.precio1_var = tk.StringVar()
        self.precio1_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio1_var)
        self.precio1_entry.place(relx=0.35,rely=0.68,relwidth=0.083,anchor='w')
        self.precio1_entry.bind("<Return>",lambda event:self.precio2_entry.focus())
        # PRECIO VENTA 2 - PRECIO VENTA 2 - PRECIO VENTA 2 - PRECIO VENTA 2 - 
        self.precio2_var = tk.StringVar()
        self.precio2_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio2_var)
        self.precio2_entry.place(relx=0.434,rely=0.68,relwidth=0.083,anchor='w')
        self.precio2_entry.bind("<Return>",lambda event:self.precio3_entry.focus())
        # PRECIO VENTA 3 - PRECIO VENTA 3 - PRECIO VENTA 3 - PRECIO VENTA 3 - 
        self.precio3_var = tk.StringVar()
        self.precio3_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLOR['white_m'],
                                          fg_color=APP_COLOR['green_m'],
                                   textvariable=self.precio3_var)
        self.precio3_entry.place(relx=0.518,rely=0.68,relwidth=0.083,anchor='w')
        self.precio3_entry.bind("<Return>",lambda event:self.AceptarPrecios())
        # -------------------------------------------------------------------------------- 
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # -------------------------------------------------------------------------------- 
        # DATOS DE PRODUCTO - DATOS DE PRODUCTO - DATOS DE PRODUCTO - 
        he_label = ctk.CTkLabel(self.entry_frame,
                                    text='Datos del producto',
                                    font=FONT['subtitle_bold'],
                                    text_color=APP_COLOR['sec'])
        he_label.place(relx=0.35,rely=0.12,anchor='w')
        # CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - CODIGO - 
        codigo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Código',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        codigo_label.place(relx=0.34,rely=0.2,anchor='e')
        # LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - LINEA - 
        linea_label = ctk.CTkLabel(self.entry_frame,
                                    text='Línea',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        linea_label.place(relx=0.34,rely=0.26,anchor='e')
        # GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - GRUPO - 
        grupo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Grupo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        grupo_label.place(relx=0.34,rely=0.32,anchor='e')
        # PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - PROVEEDOR - 
        prove_label = ctk.CTkLabel(self.entry_frame,
                                    text='Proveedor Principal',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        prove_label.place(relx=0.34,rely=0.38,anchor='e')
        # NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - NOMBRE - 
        nombre_label = ctk.CTkLabel(self.entry_frame,
                                    text='Nombre',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        nombre_label.place(relx=0.34,rely=0.44,anchor='e')       
        # COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - COSTO - 
        costo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Costo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        costo_label.place(relx=0.34,rely=0.5,anchor='e')
        # UBICACION 1 - UBICACION 1 - UBICACION 1 - UBICACION 1 - 
        ubi1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        ubi1_label.place(relx=0.34,rely=0.56,anchor='e')
        # UBICACION 2 - UBICACION 2 - UBICACION 2 - UBICACION 2 - 
        ubi2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        ubi2_label.place(relx=0.34,rely=0.62,anchor='e')
        # PRECIOS - PRECIOS - PRECIOS - PRECIOS - PRECIOS - PRECIOS - 
        precios_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precios de venta',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        precios_label.place(relx=0.34,rely=0.68,anchor='e')
        # PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - PRECIO 1 - 
        self.precio1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio1_label.place(relx=0.35,rely=0.74,anchor='w')
        # PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - PRECIO 2 - 
        self.precio2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio2_label.place(relx=0.434,rely=0.74,anchor='w')
        # PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - PRECIO 3 - 
        self.precio3_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 3',
                                    font=FONT['text_light'],
                                    text_color=APP_COLOR['gray'])
        self.precio3_label.place(relx=0.518,rely=0.74,anchor='w')
        # -------------------------------------------------------------------------------- 
        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTO
        # -------------------------------------------------------------------------------- 
        # BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
        self.busqueda_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     image=ICONS['search'],
                                     anchor='w',
                                     width=30,
                                     height=30,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'],
                                     command = self.Products_Help_Window_CB)
        self.busqueda_btn.place(relx=0.46,rely=0.2,anchor='w')
        # CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - CANCELAR - 
        self.refresh_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     width=30,
                                     height=30,
                                     image=ICONS['refresh'],
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'],
                                     command=self.Restablecer)
        self.refresh_btn.place(relx=0.5,rely=0.2,anchor='w')
        # BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - BUSCAR LINEA - 
        self.find_line_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     width=30,
                                     height=30,
                                     image=ICONS['search'],
                                     command=self.Lines_Help_Window_CB,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'])
        self.find_line_btn.place(relx=0.46,rely=0.26,anchor='w')
        # BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - BUSCAR GRUPO - 
        self.find_group_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     width=30,
                                     height=30,
                                     image=ICONS['search'],
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'],
                                     command=self.Groups_Help_Window_CB)
        self.find_group_btn.place(relx=0.46,rely=0.32,anchor='w')
        # BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - BUSCAR PROVEEDOR - 
        self.find_prov_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     width=30,
                                     height=30,
                                     image=ICONS['search'],
                                     command=self.Prov_Help_Window_CB,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'])
        self.find_prov_btn.place(relx=0.46,rely=0.38,anchor='w')
        # GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - GUARDAR - 
        self.guardar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'],
                                     command=self.AgregarProducto)
        self.guardar_btn.place(relx=0.35,rely=0.8,relwidth=0.119,anchor='w')
        # ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - ELIMINAR - 
        self.eliminar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLOR['red_s'],
                                     hover_color=APP_COLOR['red_s'],
                                     command=self.EliminarProducto)
        self.eliminar_btn.place(relx=0.6,rely=0.8,relwidth=0.119,anchor='e')
        # -------------------------------------------------------------------------------- 
        # PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PHOTOFRAME - PH
        # -------------------------------------------------------------------------------- 
        # IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - IMAGE - 
        self.image_path = 'Recursos/Imagenes/Productos'
        default_image = Image.open(f"{self.image_path}/Default.png")
        self.default_image = ctk.CTkImage(light_image=default_image, size=(250,250))
        # IMAGE FRAME
        self.image_frame = ctk.CTkFrame(self.entry_frame,fg_color=APP_COLOR['white_m'])
        self.image_frame.place(relx=0.65,rely=0.1,relheight=0.9,relwidth=0.3,anchor='nw')
        # IMAGEN - IMAGEN - IMAGEN - IMAGEN - IMAGEN - IMAGEN - 
        image_label = ctk.CTkLabel(self.image_frame,
                                    text='Imagen del producto',
                                    font=FONT['subtitle_bold'],
                                    text_color=APP_COLOR['sec'])
        image_label.pack(anchor='n',fill='x')
        # IMAGE LABEL
        self.image_label = ctk.CTkLabel(self.image_frame,
                                        text='',
                                        image=self.default_image)
        self.image_label.pack(anchor="n",pady=20)
        # AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - AGREGAR FOTO - 
        self.add_foto_btn = ctk.CTkButton(self.image_frame,
                                     text='Agregar imagen',
                                     command=self.AddPhoto,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'])
        self.add_foto_btn.pack(anchor='n',pady=10)
# ----------------------------------------------------------------------------------------
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNC
# ----------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------ 
    # ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - 
    # ------------------------------------------------------------------------------------ 
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
    # ------------------------------------------------------------------------------------ 
    # MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT -  
    # ------------------------------------------------------------------------------------ 
    def ModificarProducto(self):
        linea = self.line_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get().split(" - ")[0].strip()
        prove = self.prove_var.get().split(" - ")[0].strip()
        nombre = self.nombre_var.get()
        costo = float(self.costo_var.get())
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        product = INVENTARIO.GetProducto(self.codigo_entry.get())
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
            self.codigo_entry.get(), linea, grupo, prove, nombre, costo, ubi1, ubi2,
            precio1, precio2, precio3,image=image)
            INVENTARIO.EditProduct(producto.ToDict())
            self.ubi2_entry.unbind("<Return>")
            self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
            self.Restablecer()
    # ------------------------------------------------------------------------------------ 
    # DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - 
    # ------------------------------------------------------------------------------------ 
    def EliminarProducto(self):
        answer1 = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if not answer1:
            return
        answer2 = messagebox.askyesno('Atencion','Esto modificará los datos de inventario.'
                                      ' ¿Está seguro de eliminar el producto?')
        if answer1 and answer2:
            INVENTARIO.DelProduct(self.codigo_entry.get())
            self.Restablecer()
    # ------------------------------------------------------------------------------------ 
    # RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - 
    # ------------------------------------------------------------------------------------ 
    def Restablecer(self):
            self.entry_frame.destroy()
            self.SetInicio()
    def UpdateMode(self):
        self.codigo_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.ubi2_entry.unbind("<Return>")
        self.ubi2_entry.bind("<Return>",lambda event:self.ModificarProducto())
        self.guardar_btn.configure(text='Modificar',command=self.ModificarProducto)
        self.eliminar_btn.configure(state='normal',fg_color=APP_COLOR['red_m'],hover_color=APP_COLOR['red_s'])
        self.modprecios_btn = ctk.CTkButton(self.entry_frame,
                                      text='Modificar precios',
                                      fg_color=APP_COLOR['black_m'],
                                      hover_color=APP_COLOR['black'],
                                      command=self.ModificarPreciosMode)
        self.modprecios_btn.place(relx=0.61,rely=0.68,relwidth=0.1,anchor='w')
    # ------------------------------------------------------------------------------------ 
    # MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODI
    # ------------------------------------------------------------------------------------ 
    def ModificarPreciosMode(self):
        self.precio1_entry.focus()
        self.precio1_entry.configure(state='normal')
        self.precio2_entry.configure(state='normal')
        self.precio3_entry.configure(state='normal')
        self.codigo_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.linea_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.grupo_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.prove_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.nombre_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.costo_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.ubi1_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.ubi2_entry.configure(state='disabled',fg_color='#666',border_color='#666')
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.find_group_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.find_prov_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.add_foto_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
        self.busqueda_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.modprecios_btn.configure(command=self.AceptarPrecios,text='Aceptar precios',
                            fg_color=APP_COLOR['green_m'],hover_color=APP_COLOR['green_s'])

    # GUARDAR LOS CAMBIOS DE LOS PRECIOS
    def AceptarPrecios(self):
        codigo = self.codigo_var.get()
        p1 = self.precio1_var.get()
        p2 = self.precio2_var.get()
        p3 = self.precio3_var.get()
        INVENTARIO.EditPrecio(codigo,p1,p2,p3)
        producto = INVENTARIO.GetProducto(self.codigo_entry.get())
        self.SetInicio()
        self.Fill_Entry_Fields(producto)
        self.UpdateMode()

    
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
        self.GetImage(product_data['image'])
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
        self.UpdateMode()
    
    def Get_Product_By_Code(self):
        product_search = self.codigo_var.get().strip()
        product = INVENTARIO.GetProducto(product_search)
        if not product:
            self.linea_entry.focus()
            return
        self.Fill_Entry_Fields(product)
        self.UpdateMode()

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
        line_search = self.line_var.get().split(' - ')[0].strip()
        if not line_search.isdigit():
            messagebox.showerror('Error', 'Error de entrada: Por favor ingrese un número válido.')
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
        group_search = self.grupo_var.get().split('.')[0].strip()
        if not group_search.isdigit():
            messagebox.showerror("Base de datos", f"Ingrese un codigo de grupo válido.")
            self.grupo_var.set('')
            return
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
        PROV = Prov_Help_Window(self)
        if not PROV:
            return
        self.prove_var.set(PROV)

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