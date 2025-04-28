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
        for rows in range(14):
            self.entry_frame.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(8):
            self.entry_frame.columnconfigure(columns,weight=1,uniform='column')
    # MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - 
    # MENU LINEAS
        self.lineas = LINE_MANAGER.GetLineNames()
        self.codigoActualLinea = self.lineas[0].split(" - ")[0]
        self.lin_var = tk.StringVar(value=self.lineas[0])
        self.lin_menu = ctk.CTkOptionMenu(self.entry_frame,
                                     values=self.lineas,
                                     command=self.SelectLinMenu)
        self.lin_menu.grid(row=4,column=2,sticky='we',padx=5)
    # MENU GRUPO
        self.grup_menu = ctk.CTkOptionMenu(self.entry_frame,
                                      values=LINE_MANAGER.GetGroupNames(self.codigoActualLinea),
                                      command=self.SelectGruMenu)
        self.grup_menu.grid(row=5,column=2,sticky='we',padx=5)
    # MENU PROVEEDORES
        self.prov_menu = ctk.CTkOptionMenu(self.entry_frame,
                                      values=PROV_MANAGER.GetProvNames(),
                                      command=self.SelectProvMenu)
        self.prov_menu.grid(row=6,column=2,sticky='we',padx=5)
    # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
    # CODIGO
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.entry_frame,
                                         textvariable=self.codigo_var)
        self.codigo_entry.grid(row=3,column=3,columnspan=2,sticky='we')
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProductoMain())
    # LINEA
        self.linea_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.lin_var)
        self.linea_entry.grid(row=4,column=3,columnspan=2,sticky='we')
    # GRUPO
        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.grupo_var)
        self.grupo_entry.grid(row=5,column=3,columnspan=2,sticky='we')
    # PROVEEDOR
        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.prove_var)
        self.prove_entry.grid(row=6,column=3,columnspan=2,sticky='we')
    # NOMBRE
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.nombre_var)
        self.nombre_entry.grid(row=7,column=3,columnspan=2,sticky='we')
    # PRECIO
        self.precio_var = tk.DoubleVar()
        self.precio_entry = ctk.CTkEntry(self.entry_frame,
                                    textvariable=self.precio_var)
        self.precio_entry.grid(row=8,column=3,columnspan=2,sticky='we')
    # CANTIDAD
        self.canti_var = tk.IntVar()
        self.canti_entry = ctk.CTkEntry(self.entry_frame,
                                   textvariable=self.canti_var)
        self.canti_entry.grid(row=9,column=3,columnspan=2,sticky='we')
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # DATOS DE PRODUCTO
        he_label = ctk.CTkLabel(self.entry_frame,
                                    text='Datos del producto',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        he_label.grid(row=2,column=3,columnspan=1,sticky='w')
    # CODIGO
        codigo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Código',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        codigo_label.grid(row=3,column=5,columnspan=1,sticky='w',padx=5)
    # LINEA
        linea_label = ctk.CTkLabel(self.entry_frame,
                                    text='Línea',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        linea_label.grid(row=4,column=5,columnspan=1,sticky='w',padx=5)
    # GRUPO
        grupo_label = ctk.CTkLabel(self.entry_frame,
                                    text='Grupo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        grupo_label.grid(row=5,column=5,columnspan=1,sticky='w',padx=5)
    # PROVEEDOR
        prove_label = ctk.CTkLabel(self.entry_frame,
                                    text='Proveedor',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        prove_label.grid(row=6,column=5,columnspan=1,sticky='w',padx=5)
    # NOMBRE
        nombre_label = ctk.CTkLabel(self.entry_frame,
                                    text='Nombre',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        nombre_label.grid(row=7,column=5,columnspan=1,sticky='w',padx=5)        
    # PRECIO
        precio_label = ctk.CTkLabel(self.entry_frame,
                                    text='Precio',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio_label.grid(row=8,column=5,columnspan=1,sticky='w',padx=5)
    # CANTIDAD
        canti_label = ctk.CTkLabel(self.entry_frame,
                                    text='Cantidad',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        canti_label.grid(row=9,column=5,columnspan=1,sticky='w',padx=5)
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -BOTONES - BOTONES - BOTONES
    # AGREGAR FOTO
        self.add_foto_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar Foto',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.add_foto_btn.grid(row=11,column=3,sticky='wens',padx=4,pady=4)
    # GUARDAR
        self.guardar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.AgregarProducto)
        self.guardar_btn.grid(row=11,column=4,sticky='wens',padx=4,pady=4)
    # MODIFICAR
        self.modificar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Modificar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.ModificarProducto)
        self.modificar_btn.grid(row=12,column=3,sticky='wens',padx=4,pady=4)
    # ELIMINAR
        self.eliminar_btn = ctk.CTkButton(self.entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.EliminarProducto)
        self.eliminar_btn.grid(row=12,column=4,sticky='wens',padx=4,pady=4)
    # BUSCAR PRODUCTO
        self.busqueda_btn = ctk.CTkButton(self.entry_frame,
                                     text='Buscar un Producto',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.BusquedaProducto)
        self.busqueda_btn.grid(row=2,column=4,sticky='wens',padx=4,pady=4)
        # SALIR
        salir_btn = ctk.CTkButton(self.entry_frame,
                                       text='Volver atrás',
                                       command=self.GoBack_CB,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[4],
                                       hover_color=APP_COLORS[3])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5)
    
# FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES
# FUNCION BOTON AGREGAR PRODUCTO
    def AgregarProducto(self):
        codigo = self.codigo_var.get()
        linea = self.lin_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        canti = self.canti_var.get()
        if codigo == '':
            messagebox.showerror('Error',f"Agregue un codigo de producto.")
        elif precio <=0 or canti <= 0:
            messagebox.showerror('Error',f'El precio ni la cantidad pueden ser menores o iguales a 0')
        else:
            if INVENTARIO.CheckCode(codigo) and  INVENTARIO.CheckName(nombre) and LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.ChechProv(prove):
                producto = Product(codigo,linea,grupo,prove,nombre,precio,canti)
                INVENTARIO.AddProduct(producto.ToDict())
                self.inventario = INVENTARIO.GetInventory()
                self.RestablecerMain()
# AYUDA DE SELECCION DE LINEAS
    def SelectLinMenu(self,opcion):
        self.codigoActualLinea = opcion.split(" - ")[0]
        self.lin_var.set(self.codigoActualLinea)
        nuevos_grupos = LINE_MANAGER.GetGroupNames(self.codigoActualLinea)
        self.grup_menu.configure(values=nuevos_grupos)
# AYUDA DE SELECCION DE GRUPOS
    def SelectGruMenu(self,opcion):
        self.grupo_var.set(opcion)
# AYUDA DE SELECCION DE PROVEEDORES
    def SelectProvMenu(self,opcion):
        codigo = opcion.split(" - ")[0]
        self.prove_var.set(codigo)
# LISTA TOD0 EL INVENTARIO AL COMIENZO DEL PROGRAMA
    def ListInventory(self):
        self.inventario = INVENTARIO.GetInventory()
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        for producto in self.inventario.values():
            self.treeview.insert("",'end',
                                 text=producto['codigo'],
                                 values=(producto['linea'],
                                         producto['grupo'],
                                         producto['proveedor'],
                                         producto['nombre'],
                                         producto['precio'],
                                         producto['cantidad']))
# BUSCAR UN PRODUCTO CON LA BARRA DE BUSQUEDA    
    def BuscarProducto(self):
        self.inventario = INVENTARIO.GetInventory()
        codigo = self.search_bar_var.get()
        if codigo not in self.inventario:
            messagebox.showerror('Error de busqueda',f'El producto con codigo {codigo} no existe')
        else:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            producto = self.inventario[codigo]
        # MOSTRAR EN LISTA SOLO EL PRODUCTO ELEGIDO
            self.treeview.insert("",'end',
                                 text=producto['codigo'],
                                 values=(producto['linea'],
                                         producto['grupo'],
                                         producto['proveedor'],
                                         producto['nombre'],
                                         producto['precio'],
                                         producto['cantidad']))
        # LLENAR LAS ENTRADAS CON LOS DATOS DE PRODUCTO ELEGIDO
            self.codigo_var.set(producto['codigo'])
            self.lin_var.set(producto['linea'])
            self.grupo_var.set(producto['grupo'])
            self.prove_var.set(producto['proveedor'])
            self.nombre_var.set(producto['nombre'])
            self.precio_var.set(producto['precio'])
            self.canti_var.set(producto['cantidad'])
        # BLOQUEO DE ENTRADAS Y BOTONES
            self.mod_codi = self.codigo_entry.get()
            self.guardar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.add_foto_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.codigo_entry.configure(state='disabled',fg_color='#666')
            self.search_bar.configure(state='disabled',fg_color='#666')
            self.modificar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.eliminar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            # CANCELAR
            self.cancelar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Cancelar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.CancelMain)
            self.cancelar_btn.grid(row=3,column=6,sticky='wens',padx=4,pady=4)
    def BuscarProductoMain(self):
        self.inventario = INVENTARIO.GetInventory()
        codigo = self.codigo_entry.get()
        if codigo not in self.inventario:
            messagebox.showerror('Error de busqueda',f'El producto con codigo {codigo} no existe')
        else:
            producto = self.inventario[codigo]
        # LLENAR LAS ENTRADAS CON LOS DATOS DE PRODUCTO ELEGIDO
            self.codigo_var.set(producto['codigo'])
            self.lin_var.set(producto['linea'])
            self.grupo_var.set(producto['grupo'])
            self.prove_var.set(producto['proveedor'])
            self.nombre_var.set(producto['nombre'])
            self.precio_var.set(producto['precio'])
            self.canti_var.set(producto['cantidad'])
        # BLOQUEO DE ENTRADAS Y BOTONES
            self.mod_codi = self.codigo_entry.get()
            self.guardar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.add_foto_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.codigo_entry.configure(state='disabled',fg_color='#666')
            self.modificar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.eliminar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            # CANCELAR
            self.cancelar_btn = ctk.CTkButton(self.entry_frame,
                                     text='Cancelar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.CancelMain)
            self.cancelar_btn.grid(row=3,column=6,sticky='wens',padx=4,pady=4)
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
                                         producto['precio'],
                                         producto['cantidad']))
# COMANDO MODIFICAR PRODUCTO      
    def ModificarProducto(self):
        linea = self.lin_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        canti = self.canti_var.get()
        if precio <=0 or canti <= 0:
            messagebox.showerror('Error',f'El precio ni la cantidad pueden ser menores o iguales a 0')
        elif nombre == '':
            messagebox.showerror('Error',f'Agregue un nombre de producto')
        else:
            if  LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(linea,grupo) and PROV_MANAGER.ChechProv(prove):
                producto = Product(self.mod_codi,linea,grupo,prove,nombre,precio,canti)
                INVENTARIO.EditProduct(producto.ToDict())
                self.inventario = INVENTARIO.GetInventory()
                self.RestablecerMain()
# COMANDO CANCELAR
    def Cancel(self):
        self.ListInventory()
        self.Restablecer()
        self.cancelar_btn.destroy()
    def CancelMain(self):
        self.RestablecerMain()
        self.cancelar_btn.destroy()
# COMANDO ELIMINAR PRODUCTO
    def EliminarProducto(self):
        answer = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if answer:
            INVENTARIO.DelProduct(self.mod_codi)
            self.ListInventory()
            self.Restablecer()
# FUNCION RESTABLECER
    def Restablecer(self):
            self.guardar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.add_foto_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.codigo_entry.configure(state='normal',fg_color='#fff')
            self.search_bar.configure(state='normal',fg_color='#fff')
            self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.search_bar_var.set('')
            self.codigo_var.set('')
            self.lin_var.set('')
            self.grupo_var.set('')
            self.prove_var.set('')
            self.nombre_var.set('')
            self.precio_var.set(0.0)
            self.canti_var.set(0)
    def RestablecerMain(self):
            self.guardar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.add_foto_btn.configure(state='enabled',fg_color=APP_COLORS[2])
            self.codigo_entry.configure(state='normal',fg_color='#fff')
            self.modificar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.eliminar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
            self.codigo_var.set('')
            self.lin_var.set('')
            self.grupo_var.set('')
            self.prove_var.set('')
            self.nombre_var.set('')
            self.precio_var.set(0.0)
            self.canti_var.set(0)
# SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeview(self,event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        self.search_bar_var.set(info['text'])
        if info['text'] in self.inventario:
            self.BuscarProducto()
        self.tree_frame.destroy()
# ACTUALIZAR CAMBIOS
    def Actualizar(self):
        self.lineas = LINE_MANAGER.GetLineNames()
        self.lin_menu.configure(values=self.lineas)
        self.prov_menu.configure(values=PROV_MANAGER.GetProvNames())

    def BusquedaProducto(self):
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # FRAME DEL TREEVIEW
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
                                    command=self.Cancel,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=0,column=1,sticky='w',padx=5)
    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Precio','Cantidad'))
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
    # PRECIO
        self.treeview.heading('Precio',text='Precio')
        self.treeview.column('Precio',width=100,anchor='center')
    #PRECIO
        self.treeview.heading('Cantidad',text='Cantidad')
        self.treeview.column('Cantidad',width=100,anchor='center')
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