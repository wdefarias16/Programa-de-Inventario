import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from InventarioProductos import*
from Database import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import FONTS, APP_COLORS, APPEARANCE_MODE

# PROGRAMA DE CARGA DE PRODUCTOS
class CargaProductosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.treeview_active = False
        self.modprecios_btn_active = False
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')

        title = ctk.CTkLabel(title_frame,
                             text='Carga de productos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=10)
    # CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - CARGA ENTRADAS - 
        self.entry_frame = ctk.CTkFrame(self,
                                   width=400,
                                   fg_color=APP_COLORS[0],
                                   corner_radius=5)
        self.entry_frame.pack(fill='both',expand=True,pady=5)
    # GRID SETUP
        for rows in range(15):
            self.entry_frame.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(10):
            self.entry_frame.columnconfigure(columns,weight=1,uniform='column')
    # MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - 
    # MENU LINEAS
        self.lineas = LINE_MANAGER.GetLineNames()
        self.codigoActualLinea = self.lineas[0].split(" - ")[0]
        self.lin_var = tk.StringVar(value=self.lineas[0])
        self.lin_menu = ctk.CTkOptionMenu(self.entry_frame,
                                     values=self.lineas,
                                     command=self.SelectLinMenu)
        self.lin_menu.grid(row=3,column=1,columnspan=2,sticky='we',padx=5)
    # MENU GRUPO
        self.grup_menu = ctk.CTkOptionMenu(self.entry_frame,
                                      values=LINE_MANAGER.GetGroupNames(self.codigoActualLinea),
                                      command=self.SelectGruMenu)
        self.grup_menu.grid(row=4,column=1,columnspan=2,sticky='we',padx=5)
    # MENU PROVEEDORES
        self.prov_menu = ctk.CTkOptionMenu(self.entry_frame,
                                      values=PROV_MANAGER.GetProvNames(),
                                      command=self.SelectProvMenu)
        self.prov_menu.grid(row=5,column=1,columnspan=2,sticky='we',padx=5)
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # CODIGO
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.entry_frame,
                                         textvariable=self.codigo_var)
        self.codigo_entry.grid(row=2,column=3,columnspan=4,sticky='we')
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProducto())
    # LINEA
        self.linea_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.lin_var)
        self.linea_entry.grid(row=3,column=3,columnspan=4,sticky='we')
    # GRUPO
        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.grupo_var)
        self.grupo_entry.grid(row=4,column=3,columnspan=4,sticky='we')
    # PROVEEDOR
        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.prove_var)
        self.prove_entry.grid(row=5,column=3,columnspan=4,sticky='we')
    # NOMBRE
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.nombre_var)
        self.nombre_entry.grid(row=6,column=3,columnspan=4,sticky='we')
    # COSTO
        self.costo_var = tk.DoubleVar()
        self.costo_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.costo_var)
        self.costo_entry.grid(row=7,column=3,columnspan=4,sticky='we')
    # UBICACION 1
        self.ubi1_var = tk.StringVar()
        self.ubi1_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi1_var)
        self.ubi1_entry.grid(row=8,column=3,columnspan=4,sticky='we')
    # UBICACION 2
        self.ubi2_var = tk.StringVar()
        self.ubi2_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi2_var)
        self.ubi2_entry.grid(row=9,column=3,columnspan=4,sticky='we')
    # PRECIO VENTA 1
        self.precio1_var = tk.DoubleVar()
        self.precio1_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio1_var)
        self.precio1_entry.grid(row=10,column=3,columnspan=1,sticky='we',padx=2)
    # PRECIO VENTA 2
        self.precio2_var = tk.DoubleVar()
        self.precio2_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio2_var)
        self.precio2_entry.grid(row=10,column=4,columnspan=1,sticky='we',padx=2)
    # PRECIO VENTA 3
        self.precio3_var = tk.DoubleVar()
        self.precio3_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio3_var)
        self.precio3_entry.grid(row=10,column=5,columnspan=1,sticky='we',padx=2)
    
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # DATOS DE PRODUCTO
        he_label = ctk.CTkLabel(self.entry_frame,
                                    text='Datos del producto',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        he_label.grid(row=1,column=3,columnspan=1,sticky='w')
    # CODIGO
        codigo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Código',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        codigo_label.grid(row=2,column=7,columnspan=1,sticky='w',padx=5)
    # LINEA
        linea_label = ctk.CTkLabel(self.entry_frame,
                                    text='Línea',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        linea_label.grid(row=3,column=7,columnspan=1,sticky='w',padx=5)
    # GRUPO
        grupo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Grupo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        grupo_label.grid(row=4,column=7,columnspan=1,sticky='w',padx=5)
    # PROVEEDOR
        prove_label = ctk.CTkLabel(self.entry_frame,
                                    text='Proveedor Pricipal',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        prove_label.grid(row=5,column=7,columnspan=1,sticky='w',padx=5)
    # NOMBRE
        nombre_label = ctk.CTkLabel(self.entry_frame,
                                    text='Nombre',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        nombre_label.grid(row=6,column=7,columnspan=1,sticky='w',padx=5)        
    # COSTO
        costo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Costo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        costo_label.grid(row=7,column=7,columnspan=1,sticky='w',padx=5)
    # UBICACION 1
        ubi1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 1',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        ubi1_label.grid(row=8,column=7,columnspan=1,sticky='w',padx=5)
    # UBICACION 2
        ubi2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 2',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        ubi2_label.grid(row=9,column=7,columnspan=1,sticky='w',padx=5)
    # PRECIOS
        precios_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precios de venta',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precios_label.grid(row=10,column=7,columnspan=2,sticky='w',padx=5)
    # PRECIO 1
        precio1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 1',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio1_label.grid(row=11,column=3,columnspan=2,sticky='wn',padx=5,pady=2)
    # PRECIO 2
        precio2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 2',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio2_label.grid(row=11,column=4,columnspan=2,sticky='wn',padx=5,pady=2)
    # PRECIO 3
        precio3_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 3',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio3_label.grid(row=11,column=5,columnspan=2,sticky='wn',padx=5,pady=2)
    
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # AGREGAR FOTO
        self.add_foto_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar Foto',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.add_foto_btn.grid(row=12,column=3,columnspan=2,sticky='wens',padx=4,pady=4)
    # GUARDAR
        self.guardar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.AgregarProducto)
        self.guardar_btn.grid(row=12,column=5,columnspan=2,sticky='wens',padx=4,pady=4)
    # MODIFICAR
        self.modificar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Modificar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.ModificarProducto)
        self.modificar_btn.grid(row=13,column=3,columnspan=2,sticky='wens',padx=4,pady=4)
    # ELIMINAR
        self.eliminar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.EliminarProducto)
        self.eliminar_btn.grid(row=13,column=5,columnspan=2,sticky='wens',padx=4,pady=4)
    # BUSCAR PRODUCTO
        self.busqueda_btn = ctk.CTkButton(self.entry_frame,
                                     text='Buscar un Producto',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.BusquedaProducto)
        self.busqueda_btn.grid(row=1,column=5,columnspan=2,sticky='wens',padx=4,pady=4)
    # VOLVER ATRAS
        salir_btn = ctk.CTkButton(self.entry_frame,
                                       text='Volver atrás',
                                       command=self.GoBack_CB,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[4],
                                       hover_color=APP_COLORS[3])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5)
    # CANCELAR
        self.cancelar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Cancelar',
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.Restablecer)
        self.cancelar_btn.grid(row=1,column=7,sticky='wens',padx=4,pady=4)
    
# FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES
# FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - 
    def AgregarProducto(self):
        codigo = self.codigo_var.get()
        linea = self.lin_var.get()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        costo = self.costo_var.get()
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        precios = LINE_MANAGER.GetPrecios(linea,grupo,costo)
        if codigo == '':
            messagebox.showerror('Error',f"Agregue un codigo de producto.")
        elif costo <=0:
            messagebox.showerror('Error',f'El costo no puede ser menor o igual a 0')
        else:
            if INVENTARIO.CheckCode(codigo) and  INVENTARIO.CheckName(nombre) and LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.ChechProv(prove):
                producto = Product(
                codigo, linea, grupo, prove, nombre, costo, ubi1, ubi2,
                precios[0], precios[1], precios[2])

                INVENTARIO.AddProduct(producto.ToDict())
                self.inventario = INVENTARIO.GetInventory()
                self.Restablecer()
# COMANDO MODIFICAR PRODUCTO 
    def ModificarProducto(self):
        linea = self.lin_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        costo = self.costo_var.get()
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        precios = LINE_MANAGER.GetPrecios(linea,grupo,costo)
        if costo <=0:
            messagebox.showerror('Error',f'El costo no puede ser menor o igual a 0')
        elif nombre == '':
            messagebox.showerror('Error',f'Agregue un nombre de producto')
        else:
            if  LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.ChechProv(prove):
                producto = Product(
                self.mod_codi, linea, grupo, prove, nombre, costo, ubi1, ubi2,
                precios[0], precios[1], precios[2])
                INVENTARIO.EditProduct(producto.ToDict())
                self.inventario = INVENTARIO.GetInventory()
                self.Restablecer()
# COMANDO ELIMINAR PRODUCTO
    def EliminarProducto(self):
        answer = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if answer:
            INVENTARIO.DelProduct(self.mod_codi)
            self.ListInventory()
            self.Restablecer()
# MENUS DE SELECCION - MENUS DE SELECCION - MENUS DE SELECCION - MENUS DE SELECCION - MENUS DE SELECCION - MENUS DE SELECCION - 
# AYUDA DE SELECCION DE LINEAS
    def SelectLinMenu(self,opcion):
        self.codigoActualLinea = opcion.split(" - ")[0]
        self.lin_var.set(self.codigoActualLinea)
        nuevos_grupos = LINE_MANAGER.GetGroupNames(self.codigoActualLinea)
        self.grup_menu.configure(values=nuevos_grupos)
# AYUDA DE SELECCION DE GRUPOS
    def SelectGruMenu(self,opcion):
        self.grupo_var.set(opcion.split(' - ')[0])
# AYUDA DE SELECCION DE PROVEEDORES
    def SelectProvMenu(self,opcion):
        codigo = opcion.split(" - ")[0]
        self.prove_var.set(codigo)
# LISTA TOD0 EL INVENTARIO EN EL TREEVIEW
    def ListInventory(self):
        inventario = INVENTARIO.GetInventory()
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        for producto in inventario.values():
            self.treeview.insert("",'end',
                                 text=producto['codigo'],
                                 values=(producto['linea'],
                                         producto['grupo'],
                                         producto['proveedor'],
                                         producto['nombre'],
                                         producto['costo']))
# BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - BUSCAR UN PRODUCTO - 
    # BUSQUEDA POR CODIGO
    def BuscarProducto(self):
        inventario = INVENTARIO.GetCodigos()
        if self.treeview_active:
            codigo = self.search_bar_var.get()
            self.treeview_active = False
        else:
            codigo = self.codigo_entry.get()
        if codigo not in inventario:
            messagebox.showerror('Error de busqueda',f'El producto con codigo {codigo} no existe')
        else:
            for search in inventario:
                if search == codigo:
                    find = search
            producto = INVENTARIO.GetProducto(find)
        # LLENAR LAS ENTRADAS CON LOS DATOS DE PRODUCTO ELEGIDO
            self.codigo_var.set(producto['codigo'])
            self.lin_var.set(producto['linea'])
            self.grupo_var.set(producto['grupo'])
            self.prove_var.set(producto['proveedor'])
            self.nombre_var.set(producto['nombre'])
            self.costo_var.set(producto['costo'])
            self.ubi1_var.set(producto['ubicacion1'])
            self.ubi2_var.set(producto['ubicacion2'])
            self.precio1_var.set(producto['precio1'])
            self.precio2_var.set(producto['precio2'])
            self.precio3_var.set(producto['precio3'])
        # BLOQUEO DE ENTRADAS Y BOTONES
            self.mod_codi = self.codigo_entry.get()
            self.guardar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.add_foto_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.codigo_entry.configure(state='disabled',fg_color='#666')
            self.modificar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.eliminar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.cancelar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        # MODIFICAR PRECIOS
            if self.modprecios_btn_active == False:
                self.modprecios_btn = ctk.CTkButton(self.entry_frame,
                                             text='Modificar precios',
                                             fg_color=APP_COLORS[2],
                                             hover_color=APP_COLORS[3],
                                             command=self.ModificarPrecios)
                self.modprecios_btn.grid(row=10,column=2,sticky='nswe',padx=4,pady=4)
                self.modprecios_btn_active = True
    # BUSQUEDA POR NOMBRE
    def BuscarProductoNombre(self):
        self.inventario = INVENTARIO.GetInventory()
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        busqueda = self.search_bar_var.get().lower()
        resultados = INVENTARIO.BuscarNombres(busqueda)
        for producto in resultados:
            self.treeview.insert("", 'end',
                                 text=producto['codigo'],
                                 values=(producto['linea'],
                                         producto['grupo'],
                                         producto['proveedor'],
                                         producto['nombre'],
                                         producto['costo']))
# RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - RESTABLECER - 
    def Restablecer(self):
            if self.treeview_active:
                self.search_bar.configure(state='normal',fg_color='#fff')
                self.search_bar_var.set('')
            self.guardar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.add_foto_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.codigo_entry.configure(state='normal',fg_color='#fff')
            self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.precio1_entry.configure(state='disabled')
            self.precio2_entry.configure(state='disabled')
            self.precio3_entry.configure(state='disabled')
            self.codigo_var.set('')
            self.lin_var.set('')
            self.grupo_var.set('')
            self.prove_var.set('')
            self.nombre_var.set('')
            self.costo_var.set(0.0)
            self.ubi1_var.set('')
            self.ubi2_var.set('')
            self.precio1_var.set(0)
            self.precio2_var.set(0)
            self.precio3_var.set(0)
            self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.modprecios_btn.destroy()
            self.modprecios_btn_active = False
# MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - MODIFICAR PRECIOS - 
    def ModificarPrecios(self):
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
        self.lin_menu.configure(state='disabled')
        self.grup_menu.configure(state='disabled')
        self.prov_menu.configure(state='disabled')

        self.modprecios_btn.configure(state='enabled',
                                   fg_color=APP_COLORS[2],
                                   text='Guardar precios',
                                   command=self.AceptarPrecios)
        self.add_foto_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.busqueda_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
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
        self.add_foto_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.busqueda_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.codigo_entry.configure(state='normal',fg_color='#fff')
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
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
        self.lin_menu.configure(state='enabled')
        self.grup_menu.configure(state='enabled')
        self.prov_menu.configure(state='enabled')
        self.codigo_var.set('')
        self.lin_var.set('')
        self.grupo_var.set('')
        self.prove_var.set('')
        self.nombre_var.set('')
        self.costo_var.set(0.0)
        self.ubi1_var.set('')
        self.ubi2_var.set('')
        self.precio1_var.set(0)
        self.precio2_var.set(0)
        self.precio3_var.set(0)
# TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - 
# TABLA DE BUSQUEDA DE PRODUCTOS
    def BusquedaProducto(self):
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # FRAME DEL TREEVIEW
        self.treeview_active = True
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('600x450')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.transient(self)
    # GRID SETUP
        self.tree_frame.rowconfigure(0,weight=1)
        self.tree_frame.rowconfigure((1,2),weight=4)
        self.tree_frame.columnconfigure((0,1,2),weight=4)
        self.tree_frame.columnconfigure(3,weight=1)     
    # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                  width=200,
                                  textvariable=self.search_bar_var)
        self.search_bar.grid(row=0,column=2,sticky='we',padx=5)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
    # BOTONES TREEVIEW     
    # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=0,column=1,sticky='w',padx=5)
    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=1,column=0,sticky='nswe',padx=10,pady=10,rowspan=2,columnspan=3)
        # EVENTO DE SELECCIONAR PRODUCTO
        self.treeview.bind("<<TreeviewSelect>>",self.ClickTreeview)
    # CODIGO
        self.treeview.heading('#0',text='Codigo')
        self.treeview.column('#0',width=50,anchor='center')
    # LINEA
        self.treeview.heading('Linea',text='Linea')
        self.treeview.column('Linea',width=50,anchor='center')
    # GRUPO
        self.treeview.heading('Grupo',text='Grupo')
        self.treeview.column('Grupo',width=50,anchor='center')
    # PROVEEDOR
        self.treeview.heading('Proveedor',text='Proveedor')
        self.treeview.column('Proveedor',width=50,anchor='center')
    # NOMBRE
        self.treeview.heading('Nombre',text='Nombre')
        self.treeview.column('Nombre',width=150,anchor='center')
    # COSTO
        self.treeview.heading('Costo',text='Costo')
        self.treeview.column('Costo',width=100,anchor='center')
    # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLORS[0],
            foreground = APP_COLORS[1],
            rowheight = 30,
            font = FONTS[2],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONTS[1])
    # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.tree_frame,
                                     orientation='vertical',
                                     command=self.treeview.yview)
        scrollbar.grid(row=1,column=3,sticky='ns',padx=5,pady=5,rowspan=2)
        self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()
# SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeview(self,event):
        inventario = INVENTARIO.GetCodigos()
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        self.search_bar_var.set(info['text'])
        if info['text'] in inventario:
            self.BuscarProducto()
        self.tree_frame.destroy()