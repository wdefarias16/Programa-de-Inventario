import customtkinter as ctk
import tkinter as tk
import os
from tkinter import ttk, filedialog
from PIL import Image, ImageOps
from InventarioProductos_DB import*
from DatabaseManager import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import FONT, APP_COLORS, ICONS

# PROGRAMA DE CARGA DE PRODUCTOS
class CargaProductosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.validatenum = self.register(self.ValidateNum)
        self.treeview_active = False
        self.modprecios_btn_active = False
        self.current_photo = 'Recursos/Imagenes/Productos/Default.png'
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')

        title = ctk.CTkLabel(title_frame,
                             text='Carga de productos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['title_light'])
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
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # CODIGO
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.entry_frame,
                                         textvariable=self.codigo_var)
        self.codigo_entry.grid(row=2,column=3,columnspan=2,sticky='nswe',pady=5)
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProducto())
    # LINEA
        self.line_var = tk.StringVar()
        self.linea_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.line_var)
        self.linea_entry.grid(row=3,column=3,columnspan=2,sticky='nswe',pady=5)
        self.linea_entry.bind("<Return>",lambda event:self.GetLineByCode())
    # GRUPO
        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.grupo_var)
        self.grupo_entry.grid(row=4,column=3,columnspan=2,sticky='nswe',pady=5)
        self.grupo_entry.bind("<Return>",lambda event:self.GetGroupByCode())
    # PROVEEDOR
        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.prove_var)
        self.prove_entry.grid(row=5,column=3,columnspan=2,sticky='nswe',pady=5)
        self.prove_entry.bind("<Return>",lambda event:self.GetProvByCode())
    # NOMBRE
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.nombre_var)
        self.nombre_entry.grid(row=6,column=3,columnspan=3,sticky='nswe',pady=5)
        self.nombre_entry.bind("<Return>",lambda event:self.costo_entry.focus())
    # COSTO
        self.costo_var = tk.StringVar()
        self.costo_entry = ctk.CTkEntry(self.entry_frame,
                                        validate = 'key',
                                        validatecommand = (self.validatenum,'%P'),
                                        textvariable=self.costo_var)
        self.costo_entry.grid(row=7,column=3,sticky='nswe',pady=5)
        self.costo_entry.bind("<Return>",lambda event:self.ubi1_entry.focus())
    # UBICACION 1
        self.ubi1_var = tk.StringVar()
        self.ubi1_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi1_var)
        self.ubi1_entry.grid(row=8,column=3,columnspan=3,sticky='nswe',pady=5)
        self.ubi1_entry.bind("<Return>",lambda event:self.ubi2_entry.focus())
    # UBICACION 2
        self.ubi2_var = tk.StringVar()
        self.ubi2_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.ubi2_var)
        self.ubi2_entry.grid(row=9,column=3,columnspan=3,sticky='nswe',pady=5)
        self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
    # PRECIO VENTA 1
        self.precio1_var = tk.StringVar()
        self.precio1_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio1_var)
        self.precio1_entry.grid(row=10,column=3,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio1_entry.bind("<Return>",lambda event:self.precio2_entry.focus())
    # PRECIO VENTA 2
        self.precio2_var = tk.StringVar()
        self.precio2_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio2_var)
        self.precio2_entry.grid(row=10,column=4,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio2_entry.bind("<Return>",lambda event:self.precio3_entry.focus())
    # PRECIO VENTA 3
        self.precio3_var = tk.StringVar()
        self.precio3_entry = ctk.CTkEntry(self.entry_frame,
                                          state='disabled',
                                          border_color=APP_COLORS[0],
                                          fg_color=APP_COLORS[8],
                                   textvariable=self.precio3_var)
        self.precio3_entry.grid(row=10,column=5,columnspan=1,sticky='nswe',padx=2,pady=5)
        self.precio3_entry.bind("<Return>",lambda event:self.AceptarPrecios())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # DATOS DE PRODUCTO
        he_label = ctk.CTkLabel(self.entry_frame,
                                    text='Datos del producto',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        he_label.grid(row=1,column=3,columnspan=1,sticky='w')
    # CODIGO
        codigo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Código',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        codigo_label.grid(row=2,column=2,columnspan=1,sticky='e',padx=5)
    # LINEA
        linea_label = ctk.CTkLabel(self.entry_frame,
                                    text='Línea',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        linea_label.grid(row=3,column=2,columnspan=1,sticky='e',padx=5)
    # GRUPO
        grupo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Grupo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        grupo_label.grid(row=4,column=2,columnspan=1,sticky='e',padx=5)
    # PROVEEDOR
        prove_label = ctk.CTkLabel(self.entry_frame,
                                    text='Proveedor Principal',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        prove_label.grid(row=5,column=1,columnspan=2,sticky='e',padx=5)
    # NOMBRE
        nombre_label = ctk.CTkLabel(self.entry_frame,
                                    text='Nombre',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        nombre_label.grid(row=6,column=2,columnspan=1,sticky='e',padx=5)        
    # COSTO
        costo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Costo',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        costo_label.grid(row=7,column=2,columnspan=1,sticky='e',padx=5)
    # UBICACION 1
        ubi1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        ubi1_label.grid(row=8,column=2,columnspan=1,sticky='e',padx=5)
    # UBICACION 2
        ubi2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Ubicación 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        ubi2_label.grid(row=9,column=2,columnspan=1,sticky='e',padx=5)
    # PRECIOS
        precios_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precios de venta',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        precios_label.grid(row=10,column=1,columnspan=2,sticky='e',padx=5)
    # PRECIO 1
        self.precio1_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 1',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        self.precio1_label.grid(row=11,column=3,columnspan=2,sticky='wn',padx=5,pady=2)
    # PRECIO 2
        self.precio2_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 2',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        self.precio2_label.grid(row=11,column=4,columnspan=2,sticky='wn',padx=5,pady=2)
    # PRECIO 3
        self.precio3_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio 3',
                                    font=FONT['text_light'],
                                    text_color=APP_COLORS[4])
        self.precio3_label.grid(row=11,column=5,columnspan=2,sticky='wn',padx=5,pady=2)
    
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # BUSCAR PRODUCTO
        self.busqueda_btn = ctk.CTkButton(self.entry_frame,
                                     text='',
                                     image=ICONS['search'],
                                     anchor='w',
                                     width=10,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=lambda: self.BusquedaProducto() if not self.treeview_active else None)
        self.busqueda_btn.grid(row=2,column=5,sticky='nsw',padx=5,pady=5)
    # CANCELAR
        self.cancelar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Cancelar',
                                     state='disabled',
                                     fg_color=APP_COLORS[10],
                                     hover_color=APP_COLORS[10],
                                     command=self.Restablecer)
        self.cancelar_btn.grid(row=13,column=2,sticky='nswe',padx=4,pady=4)
    # BUSCAR LINEA
        self.find_line_btn = ctk.CTkButton(self.entry_frame,
                                     text='Líneas',
                                     command=self.LineHelp,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.find_line_btn.grid(row=3,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
    # BUSCAR GRUPO
        self.find_group_btn = ctk.CTkButton(self.entry_frame,
                                     text='Grupos',
                                     command=self.GroupHelp,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.find_group_btn.grid(row=4,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
    # BUSCAR PROVEEDOR
        self.find_prov_btn = ctk.CTkButton(self.entry_frame,
                                     text='Proveedores',
                                     command=self.ProvHelp,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.find_prov_btn.grid(row=5,column=5,columnspan=1,sticky='nswe',padx=5,pady=5)
    # AGREGAR FOTO
        self.add_foto_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar Foto',
                                     command=self.AddPhoto,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.add_foto_btn.grid(row=12,column=3,columnspan=2,sticky='nswe',padx=4,pady=4)
    # GUARDAR
        self.guardar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.AgregarProducto)
        self.guardar_btn.grid(row=12,column=5,columnspan=2,sticky='nswe',padx=4,pady=4)
    # MODIFICAR
        self.modificar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Modificar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.ModificarProducto)
        self.modificar_btn.grid(row=13,column=3,columnspan=2,sticky='nswe',padx=4,pady=4)
    # ELIMINAR
        self.eliminar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLORS[10],
                                     hover_color=APP_COLORS[10],
                                     command=self.EliminarProducto)
        self.eliminar_btn.grid(row=13,column=5,columnspan=2,sticky='nswe',padx=4,pady=4)
    # VOLVER ATRAS
        salir_btn = ctk.CTkButton(self.entry_frame,
                                       text='Volver atrás',
                                       command=self.GoBack_CB,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[4],
                                       hover_color=APP_COLORS[3])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5)
    
    # PHOTOFRAME
        self.image_path = 'Recursos/Imagenes/Productos'
        self.product_image = Image.open(f"{self.image_path}/Default.png")
        self.ctk_image = ctk.CTkImage(light_image=self.product_image, size=(200,200))
        
        self.image_frame = ctk.CTkFrame(self.entry_frame,fg_color=APP_COLORS[0])
        self.image_frame.grid(row=2,column=7,columnspan=2,rowspan=12,sticky='nswe',pady=5)
        
        self.image_label = ctk.CTkLabel(self.image_frame,
                                        text='',
                                        image=self.ctk_image)
        self.image_label.pack(side="top", anchor="n",expand=True)
    
# FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES
# FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - FUNCION BOTON AGREGAR PRODUCTO - 
    def AgregarProducto(self):
        codigo = self.codigo_var.get()
        linea = self.line_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get().split(" - ")[0].strip()
        prove = self.prove_var.get().split(" - ")[0].strip()
        nombre = self.nombre_var.get()
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        # CHEQUEAR SI CODIGO NO ESTA VACIO
        if codigo == '':
            messagebox.showerror('Error',f"Agregue un codigo de producto.")
            self.codigo_entry.focus()
            return
        # CHEQUEAR SI LINEA - GRUPO - PROV NO ESTAN VACIOS
        if linea == '' or grupo == '' or prove == '':
            messagebox.showerror('Error',f"Debe agregar línea, Grupo y Proveedor válidos.")
            return
        # CHEQUEAR SI NOMBRE NO ESTA VACIO
        if not INVENTARIO.CheckName(nombre):
            self.nombre_entry.focus()
            return
        # OBTENER EL FLOTANTE DEL COSTO
        try:
            costo = float(self.costo_var.get())
        except Exception as e:
            messagebox.showerror('Error',f'La entrada "Costo" no puede estar vacia')
            self.costo_entry.focus()
            return
        # CHEQUEAR SI COSTO NO ESTA VACIO
        if costo <= 0 or costo == '':
            messagebox.showerror('Error',f'El costo no puede ser menor o igual a 0')
            self.costo_entry.focus()
            return
        # SI PASA LA VERIFICACION SE AGREGA EL PRODUCTO
        if INVENTARIO.CheckCode(codigo) and LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.CheckProv(prove):
            precios = LINE_MANAGER.GetPrecios(linea,grupo,costo)
            producto = Product(
            codigo, linea, grupo, prove, nombre, costo, ubi1, ubi2,
            precios[0], precios[1], precios[2])
            # MOSTRAR PRECIOS Y PORCENTAJES
            porcentajes = LINE_MANAGER.GetPorcentajes(linea,grupo)
            self.precio1_var.set(precios[0])
            self.precio2_var.set(precios[1])
            self.precio3_var.set(precios[2])
            self.precio1_label.configure(text=f'Precio 1: {porcentajes['porcentaje1']}%')
            self.precio2_label.configure(text=f'Precio 2: {porcentajes['porcentaje2']}%')
            self.precio3_label.configure(text=f'Precio 3: {porcentajes['porcentaje3']}%')
            INVENTARIO.AddProduct(producto.ToDict())
            self.Restablecer()
# COMANDO MODIFICAR PRODUCTO 
    def ModificarProducto(self):
        anwser = messagebox.askyesno('¡Atención!','¿Está seguro que desea modificar el producto con estos cambios?')
        if not anwser:
            return
        linea = self.line_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get().split(" - ")[0].strip()
        prove = self.prove_var.get().split(" - ")[0].strip()
        nombre = self.nombre_var.get()
        costo = float(self.costo_var.get())
        ubi1 = self.ubi1_var.get()
        ubi2 = self.ubi2_var.get()
        
        product = INVENTARIO.GetProducto(self.mod_codi)

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
        if not INVENTARIO.CheckName(nombre):
            return
        if  LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.CheckProv(prove):
            producto = Product(
            self.mod_codi, linea, grupo, prove, nombre, costo, ubi1, ubi2,
            precio1, precio2, precio3)
            INVENTARIO.EditProduct(producto.ToDict())
            self.ubi2_entry.unbind("<Return>")
            self.ubi2_entry.bind("<Return>",lambda event:self.AgregarProducto())
            self.Restablecer()
# COMANDO ELIMINAR PRODUCTO
    def EliminarProducto(self):
        answer1 = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if not answer1:
            return
        answer2 = messagebox.askyesno('Atencion','Esto modificará los datos de inventario.'
                                      ' Está seguro de eliminar el producto?')
        if answer1 and answer2:
            INVENTARIO.DelProduct(self.mod_codi)
            self.Restablecer()
# LISTA TOD0 EL INVENTARIO EN EL TREEVIEW DE PRODUCTOS
    def ListInventory(self):
        self.search_bar_var.set('')
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
                                         f'${producto['costo']}'))
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
            self.linea_entry.focus()
            return
        if INVENTARIO.CheckCodeValidate(codigo):
            for search in inventario:
                if search == codigo:
                    producto = INVENTARIO.GetProducto(search)
        # LLENAR LAS ENTRADAS CON LOS DATOS DE PRODUCTO ELEGIDO
            line = LINE_MANAGER.GetLine(producto['linea'])
            group = LINE_MANAGER.GetGroup(producto['linea'],producto['grupo'])
            prov = PROV_MANAGER.GetProv(producto['proveedor'])
            self.codigo_var.set(producto['codigo'])
            self.line_var.set(f'{line[0]} - {line[1]}')
            self.grupo_var.set(f'{group[0]} - {group[1]}')
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
        # BLOQUEO DE ENTRADAS Y BOTONES
            self.mod_codi = self.codigo_entry.get()
            self.guardar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.codigo_entry.configure(state='disabled',fg_color='#666')
            self.modificar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.eliminar_btn.configure(state='enabled',fg_color=APP_COLORS[9],hover_color=APP_COLORS[10])
            self.cancelar_btn.configure(state='enabled',fg_color=APP_COLORS[9])
        # MODIFICAR PRECIOS
            if not self.modprecios_btn_active:
                self.modprecios_btn = ctk.CTkButton(self.entry_frame,
                                             text='Modificar precios',
                                             fg_color=APP_COLORS[2],
                                             hover_color=APP_COLORS[3],
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
    def Restablecer(self):
            if self.modprecios_btn_active:
                self.modprecios_btn.destroy()
                self.modprecios_btn_active = False
            self.guardar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.add_foto_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[10])
            self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[10])
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
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.find_group_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.find_prov_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modprecios_btn.configure(state='enabled',
                                   fg_color=APP_COLORS[2],
                                   text='Guardar precios',
                                   command=self.AceptarPrecios)
        self.add_foto_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.busqueda_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[10])

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
        self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.find_line_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.find_group_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.find_prov_btn.configure(state='enabled',fg_color=APP_COLORS[2])
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
# TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - TREVIEW BUSQUEDA DE PRODUCTOS - 
# TABLA DE BUSQUEDA DE PRODUCTOS
    def BusquedaProducto(self):
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # FRAME DEL TREEVIEW
        self.treeview_active = True
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('900x450')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        self.tree_frame.transient(self)
    # GRID SETUP
        for rows in range(10):
            self.tree_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(10):
            self.tree_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
        title_frame = ctk.CTkFrame(self.tree_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=16,sticky='nswe')
        title = ctk.CTkLabel(title_frame,
                             text='Busqueda de productos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['text'])
        title.pack(pady=10)
    # BARRA DE BUSQUEDA
        label_sb = ctk.CTkLabel(self.tree_frame,
                             text='Busqueda por nombre',
                             bg_color='transparent',
                             text_color=APP_COLORS[4],
                             font=FONT['text_light'])
        label_sb.grid(row=1,column=0,columnspan=3,sticky='ws',padx=15)
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                  width=200,
                                  textvariable=self.search_bar_var)
        self.search_bar.grid(row=2,column=0,columnspan=2,sticky='we',padx=15)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
        self.search_bar.bind("<Control-BackSpace>", lambda event: self.ListInventory())
        self.search_bar.after(100,lambda:self.search_bar.focus())
    # BOTONES TREEVIEW     
    # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Listar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=2,column=2,columnspan=2,sticky='we')
    # CERRAR
        cerrar_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cerrar',
                                    command=self.Cerrar,
                                    fg_color=APP_COLORS[9],
                                    hover_color=APP_COLORS[10])
        cerrar_btn.grid(row=2,column=7,columnspan=2,sticky='we')

    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=3,column=0,sticky='nswe',padx=20,pady=10,rowspan=7,columnspan=10)
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
            font = FONT['text_small'],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONT['text_light'])
    # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.tree_frame,
                                     orientation='vertical',
                                     command=self.treeview.yview)
        scrollbar.grid(row=3,column=15,sticky='wns',pady=5,rowspan=7)
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
    def Cerrar(self):
        self.tree_frame.destroy()
        self.treeview_active = False



# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# FRAME DEL TREEVIEW
    def LineHelp(self):
        self.line_help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[5])
        self.line_help_frame.geometry('600x400')
        self.line_help_frame.title('Ayuda de lineas')
        self.line_help_frame.transient(self)
    # GRID SETUP
        for rows in range(10):
            self.line_help_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(10):
            self.line_help_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
        title_frame = ctk.CTkFrame(self.line_help_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
        title = ctk.CTkLabel(title_frame,
                             text='Ayuda de líneas',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['text'])
        title.pack(pady=10)   
    # BARRA DE BUSQUEDA
        self.search_line_bar_var = tk.StringVar()
        self.search_line_bar = ctk.CTkEntry(self.line_help_frame,
                                       width=200,
                                       textvariable=self.search_line_bar_var)
        self.search_line_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
        self.search_line_bar.after(100,lambda:self.search_line_bar.focus())
        self.search_line_bar.bind("<Return>",lambda event:self.SearchLine())
        self.search_line_bar.bind("<Control-BackSpace>", lambda event: self.ListLines())
    # BOTONES TREEVIEW
        # BUSCAR
        search_btn = ctk.CTkButton(self.line_help_frame,
                                   text='Buscar',
                                   command=self.SearchLine,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
        # CANCELAR
        cancel_btn = ctk.CTkButton(self.line_help_frame,
                                   text='Cancelar',
                                   command=self.ListLines,
                                   fg_color=APP_COLORS[9],
                                   hover_color=APP_COLORS[10])
        cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
        self.line_help_treeview = ttk.Treeview(self.line_help_frame,
                                     style='Custom.Treeview',
                                     columns=('Linea'))
        self.line_help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
        # EVENTO DE SELECCIONAR PRODUCTO
        self.line_help_treeview.bind("<<TreeviewSelect>>",self.SelectLine)
        # CODIGO
        self.line_help_treeview.heading('#0',text='Codigo')
        self.line_help_treeview.column('#0',width=25,anchor='center')
        # LINEA
        self.line_help_treeview.heading('Linea',text='Linea')
        self.line_help_treeview.column('Linea',width=100,anchor='center')

    # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.line_help_frame,
                                     orientation='vertical',
                                     command=self.line_help_treeview.yview)
        scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
        self.line_help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListLines()
# BUSCAR LINEAS POR NOMBRE
    def SearchLine(self):
        for item in self.line_help_treeview.get_children():
            self.line_help_treeview.delete(item)
        search = self.search_line_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchLineByName(search)
        for line in outcome:
            self.line_help_treeview.insert("", 'end',
                                 text=line['codigo'],
                                 values=(line['linea']))
# LISTAR LINEAS
    def ListLines(self):
        self.search_line_bar.focus()
        self.search_line_bar_var.set('')
        lines = LINE_MANAGER.GetLineNames()
        for item in self.line_help_treeview.get_children():
                self.line_help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.line_help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(line.split(' - ')[1].strip(),),
                                       tags=(tag,))  # Asignar el tag a la fila

        # Configurar colores para los tags
        self.line_help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.line_help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UNA LINEA Y AGREGARLA AL CAMPO DE LINEA
    def SelectLine(self,event):
        item_id = self.line_help_treeview.selection()
        info = self.line_help_treeview.item(item_id)
        self.line_var.set(f'{info['text']} - {info['values'][0]}')
        self.grupo_entry.focus()
        self.line_help_frame.destroy()
    def GetLineByCode(self):
        line_search = self.line_var.get().strip()
        try:
            line_search = int(line_search)
        except Exception as e:
            messagebox.showerror('Error','Error de entrada en línea')
            self.line_var.set('')
            return
        line = LINE_MANAGER.GetLine(line_search)
        if line:
            self.line_var.set(f'{line[0]} - {line[1]}')
            self.grupo_entry.focus()
        else:
            messagebox.showerror("Base de datos", f"Error al buscar línea: {line_search}")
            self.line_var.set('')
            return
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 


# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
    def GroupHelp(self):
        try:
            self.current_line = int(self.line_var.get().split(' - ')[0].strip())
            if not LINE_MANAGER.CheckLine(self.current_line):
                messagebox.showerror('Error','Seleccione una línea válida.')
                return
            self.help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[5])
            self.help_frame.geometry('600x400')
            self.help_frame.title('Ayuda de Grupos')
            self.help_frame.transient(self)
        # GRID SETUP
            for rows in range(10):
                self.help_frame.rowconfigure(rows, weight=1,uniform='row')
            for columns in range(10):
                self.help_frame.columnconfigure(columns,weight=1,uniform='column')
        # TITULO
            title_frame = ctk.CTkFrame(self.help_frame,corner_radius=0,fg_color=APP_COLORS[3])
            title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
            title = ctk.CTkLabel(title_frame,
                                 text='Ayuda de Grupos',
                                 bg_color='transparent',
                                 text_color=APP_COLORS[0],
                                 height=50,
                                 font=FONT['text'])
            title.pack(pady=10)   
        # BARRA DE BUSQUEDA
            self.search_help_bar_var = tk.StringVar()
            self.search_help_bar = ctk.CTkEntry(self.help_frame,
                                           width=200,
                                           textvariable=self.search_help_bar_var)
            self.search_help_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
            self.search_help_bar.after(100,lambda:self.search_help_bar.focus())
            self.search_help_bar.bind("<Return>",lambda event:self.SearchGroup())
            self.search_help_bar.bind("<Control-BackSpace>", lambda event: self.ListGroups())
        # BOTONES TREEVIEW
            # BUSCAR
            search_btn = ctk.CTkButton(self.help_frame,
                                       text='Buscar',
                                       command=self.SearchGroup,
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3])
            search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
            # CANCELAR
            cancel_btn = ctk.CTkButton(self.help_frame,
                                       text='Cancelar',
                                       command=self.ListGroups,
                                       fg_color=APP_COLORS[9],
                                       hover_color=APP_COLORS[10])
            cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
        # TREEVIEW
            self.help_treeview = ttk.Treeview(self.help_frame,
                                         style='Custom.Treeview',
                                         columns=('Linea','Grupo'))
            self.help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
            # EVENTO DE SELECCIONAR PRODUCTO
            self.help_treeview.bind("<<TreeviewSelect>>",self.SelectGroup)
            # CODIGO
            self.help_treeview.heading('#0',text='Código')
            self.help_treeview.column('#0',width=25,anchor='center')
            # LINEA
            self.help_treeview.heading('Linea',text='Línea')
            self.help_treeview.column('Linea',width=100,anchor='center')
            # GRUPO
            self.help_treeview.heading('Grupo',text='Grupo')
            self.help_treeview.column('Grupo',width=100,anchor='center')

        # SCROLLBAR DEL TV
            scrollbar = ctk.CTkScrollbar(self.help_frame,
                                         orientation='vertical',
                                         command=self.help_treeview.yview)
            scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
            self.help_treeview.configure(yscrollcommand=scrollbar.set)
        # LISTAR LOS PROVEEDORES
            self.ListGroups()
        except ValueError:
            messagebox.showerror('Error','Seleccione una línea válida.')
        
# BUSCAR PROVEEDORES POR NOMBRE
    def SearchGroup(self):
        for item in self.help_treeview.get_children():
            self.help_treeview.delete(item)
        search = self.search_help_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchGroupByName(search,line=self.current_line)
        for group in outcome:
            self.help_treeview.insert("", 'end',
                                 text=group['codigo'],
                                 values=(group['linea'],
                                         group['grupo']))
# LISTAR PROVEEDORES
    def ListGroups(self):
        self.search_help_bar.focus()
        self.search_help_bar_var.set('')
        lines = LINE_MANAGER.GetGroupNames(self.current_line)
        for item in self.help_treeview.get_children():
                self.help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(self.current_line,
                                                line.split(' - ')[1].strip()),
                                       tags=(tag,))
        self.help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UN PROVEEDOR Y AGREGARLO AL CAMPO DE PROVEEEDOR
    def SelectGroup(self,event):
        item_id = self.help_treeview.selection()
        info = self.help_treeview.item(item_id)
        self.grupo_var.set(f'{info['text']} - {info['values'][1]}')
        self.help_frame.destroy()
# BUSCAR UN GRUPO EN LA ENTRADA
    def GetGroupByCode(self):
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
        group_code = str(str(line[0]) + '.' + group_search)
        group = LINE_MANAGER.GetGroup(line_search,group_code)
        if group:
            self.grupo_var.set(f'{group[0]} - {group[1]}')
            self.prove_entry.focus()
        else:
            messagebox.showerror("Base de datos", f"No se encontro el grupo {group_search}")
            self.grupo_var.set('')
            return
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 


# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
    def ProvHelp(self):
        self.help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[5])
        self.help_frame.geometry('600x400')
        self.help_frame.title('Ayuda de Proveedores')
        self.help_frame.transient(self)
    # GRID SETUP
        for rows in range(10):
            self.help_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(10):
            self.help_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
        title_frame = ctk.CTkFrame(self.help_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
        title = ctk.CTkLabel(title_frame,
                             text='Ayuda de Proveedores',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['text'])
        title.pack(pady=10)   
    # BARRA DE BUSQUEDA
        self.search_help_bar_var = tk.StringVar()
        self.search_help_bar = ctk.CTkEntry(self.help_frame,
                                       width=200,
                                       textvariable=self.search_help_bar_var)
        self.search_help_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
        self.search_help_bar.after(100,lambda:self.search_help_bar.focus())
        self.search_help_bar.bind("<Return>",lambda event:self.SearchProv())
        self.search_help_bar.bind("<Control-BackSpace>", lambda event: self.ListProvs())
    # BOTONES TREEVIEW
        # BUSCAR
        search_btn = ctk.CTkButton(self.help_frame,
                                   text='Buscar',
                                   command=self.SearchLine,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
        # CANCELAR
        cancel_btn = ctk.CTkButton(self.help_frame,
                                   text='Cancelar',
                                   command=self.ListLines,
                                   fg_color=APP_COLORS[9],
                                   hover_color=APP_COLORS[10])
        cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
        self.help_treeview = ttk.Treeview(self.help_frame,
                                     style='Custom.Treeview',
                                     columns=('Proveedor'))
        self.help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
        # EVENTO DE SELECCIONAR PRODUCTO
        self.help_treeview.bind("<<TreeviewSelect>>",self.SelectProv)
        # CODIGO
        self.help_treeview.heading('#0',text='Código')
        self.help_treeview.column('#0',width=25,anchor='center')
        # PROVEEDOR
        self.help_treeview.heading('Proveedor',text='Proveedor')
        self.help_treeview.column('Proveedor',width=100,anchor='center')

    # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.help_frame,
                                     orientation='vertical',
                                     command=self.help_treeview.yview)
        scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
        self.help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR LOS PROVEEDORES
        self.ListProvs()
# BUSCAR PROVEEDORES POR NOMBRE
    def SearchProv(self):
        for item in self.help_treeview.get_children():
            self.help_treeview.delete(item)
        search = self.search_help_bar_var.get().lower()
        outcome = PROV_MANAGER.SearchProvByName(search)
        for prov in outcome:
            self.help_treeview.insert("", 'end',
                                 text=prov['codigo'],
                                 values=(prov['nombre']))
# LISTAR PROVEEDORES
    def ListProvs(self):
        self.search_help_bar.focus()
        self.search_help_bar_var.set('')
        lines = PROV_MANAGER.GetProvNames()
        for item in self.help_treeview.get_children():
                self.help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(line.split(' - ')[1].strip(),),
                                       tags=(tag,))
        self.help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UN PROVEEDOR Y AGREGARLO AL CAMPO DE PROVEEEDOR
    def SelectProv(self,event):
        item_id = self.help_treeview.selection()
        info = self.help_treeview.item(item_id)
        self.prove_var.set(f'{info['text']} - {info['values'][0]}')
        self.nombre_entry.focus()
        self.help_frame.destroy()
# BUSCAR UN GRUPO EN LA ENTRADA        
    def GetProvByCode(self):
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
            
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
# PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - PROV HELP - 
    def ValidateNum(self,text):
        text = text.replace(".", "", 1)
        if text == '':
            return True
        return text.isdigit()
    
    def AddPhoto(self):
        codigo = self.codigo_var.get()
        if not codigo:
            messagebox.showwarning('Atención','Seleccione un producto al que agregar una foto.')
            return
        
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
        )
        if not file_path:
            return
        
        img = Image.open(file_path)
        img = ImageOps.exif_transpose(img)
        w, h = img.size
        
        max_size = 500
        scale = min(max_size / w, max_size / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        
        # Filtro compatible según versión de Pillow
        try:
            resample_filter = Image.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image.LANCZOS
        
        img_resized = img.resize((new_w, new_h), resample_filter)
        
        folder = "Recursos/Imagenes/Productos"
        os.makedirs(folder, exist_ok=True)
        
        file_name = f'{codigo}_img.png'
        save_path = os.path.join(folder, file_name)
        img_resized.save(save_path)

        photo = ctk.CTkImage(light_image=img_resized, size=(int(new_w/2),int(new_h/2)))
        self.current_photo = save_path
        self.UpdatePhoto(photo)

    def UpdatePhoto(self,photo):
        self.image_label.configure(image=photo)



        # # PHOTOFRAME
        # self.image_path = 'Recursos/Imagenes/Productos'
        # self.product_image = Image.open(f"{self.image_path}/Default.png")
        # self.ctk_image = ctk.CTkImage(light_image=self.product_image, size=(150,150))
        # 
        # self.image_frame = ctk.CTkFrame(self.entry_frame,fg_color=APP_COLORS[0])
        # self.image_frame.grid(row=2,column=7,columnspan=2,rowspan=3,sticky='nswe')
        # 
        # self.image_label = ctk.CTkLabel(self.image_frame,
        #                                 text='',
        #                                 image=self.ctk_image)
        # self.image_label.pack(expand=True)