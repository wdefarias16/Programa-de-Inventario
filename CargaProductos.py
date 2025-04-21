import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ProductDataBase import*
from Database import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class CargaProductosProg(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

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
        entry_frame = ctk.CTkFrame(self,
                                   width=400,
                                   corner_radius=5,
                                   fg_color=APP_COLORS[5])
        entry_frame.pack(fill='y',side='left',pady=5)

        # GRID SETUP
        for rows in range(14):
            entry_frame.rowconfigure(rows,weight=1)
        for columns in range(8):
            entry_frame.columnconfigure(columns,weight=1)
        
        # MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - MENUS - 
        self.lineas = LINE_MANAGER.GetLineNames()
        self.codigoActualLinea = self.lineas[0].split(" - ")[0]
        self.lin_var = tk.StringVar(value=self.lineas[0])
        lin_menu = ctk.CTkOptionMenu(entry_frame,
                                     values=self.lineas,
                                     command=self.SelectLinMenu)
        lin_menu.grid(row=4,column=0,columnspan=2,sticky='we',padx=5)

        self.grup_menu = ctk.CTkOptionMenu(entry_frame,
                                      values=LINE_MANAGER.GetGroupNames(self.codigoActualLinea),
                                      command=self.SelectGruMenu)
        self.grup_menu.grid(row=5,column=0,columnspan=2,sticky='we',padx=5)

        prov_menu = ctk.CTkOptionMenu(entry_frame,
                                      values=PROV_MANAGER.GetProvNames(),
                                      command=self.SelectProvMenu)
        prov_menu.grid(row=6,column=0,columnspan=2,sticky='we',padx=5)
        
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        self.codigo_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.codigo_var)
        self.codigo_entry.grid(row=3,column=2,columnspan=2,sticky='we')

        self.linea_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.lin_var)
        self.linea_entry.grid(row=4,column=2,columnspan=2,sticky='we')

        self.grupo_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.grupo_var)
        self.grupo_entry.grid(row=5,column=2,columnspan=2,sticky='we')

        self.prove_var = tk.StringVar()
        self.prove_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.prove_var)
        self.prove_entry.grid(row=6,column=2,columnspan=2,sticky='we')

        self.nombre_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.nombre_var)
        self.nombre_entry.grid(row=7,column=2,columnspan=2,sticky='we')

        self.precio_var = tk.DoubleVar()
        self.precio_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.precio_var)
        self.precio_entry.grid(row=8,column=2,columnspan=2,sticky='we')

        self.canti_var = tk.IntVar()
        self.canti_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.canti_var)
        self.canti_entry.grid(row=9,column=2,columnspan=2,sticky='we')

        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        
        he_label = ctk.CTkLabel(entry_frame,
                                    text='Datos del producto',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        he_label.grid(row=1,column=2,columnspan=1,sticky='w')
        
        codigo_label = ctk.CTkLabel(entry_frame,
                                    text='Codigo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        codigo_label.grid(row=3,column=4,columnspan=1,sticky='w',padx=5)

        linea_label = ctk.CTkLabel(entry_frame,
                                    text='Línea',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        linea_label.grid(row=4,column=4,columnspan=1,sticky='w',padx=5)

        grupo_label = ctk.CTkLabel(entry_frame,
                                    text='Grupo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        grupo_label.grid(row=5,column=4,columnspan=1,sticky='w',padx=5)

        prove_label = ctk.CTkLabel(entry_frame,
                                    text='Proveedor',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        prove_label.grid(row=6,column=4,columnspan=1,sticky='w',padx=5)

        nombre_label = ctk.CTkLabel(entry_frame,
                                    text='Nombre',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        nombre_label.grid(row=7,column=4,columnspan=1,sticky='w',padx=5)        

        precio_label = ctk.CTkLabel(entry_frame,
                                    text='Precio',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio_label.grid(row=8,column=4,columnspan=1,sticky='w',padx=5)

        canti_label = ctk.CTkLabel(entry_frame,
                                    text='Cantidad',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        canti_label.grid(row=9,column=4,columnspan=1,sticky='w',padx=5)

        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 

        self.add_foto_btn = ctk.CTkButton(entry_frame,
                                     text='Agregar Foto',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.add_foto_btn.grid(row=11,column=0,columnspan=2)

        self.guardar_btn = ctk.CTkButton(entry_frame,
                                     text='Agregar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.AgregarProducto)
        self.guardar_btn.grid(row=11,column=2,columnspan=2)

        self.modificar_btn = ctk.CTkButton(entry_frame,
                                     state='disabled',
                                     text='Modificar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.ModificarProducto)
        self.modificar_btn.grid(row=12,column=0,columnspan=2)

        self.eliminar_btn = ctk.CTkButton(entry_frame,
                                     state='disabled',
                                     text='Eliminar',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3],
                                     command=self.EliminarProducto)
        self.eliminar_btn.grid(row=12,column=2,columnspan=2)
        
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # FRAME DEL TREEVIEW
        tree_frame = ctk.CTkFrame(self,
                                   corner_radius=5,
                                   fg_color=APP_COLORS[5])
        tree_frame.pack(expand=True,fill='both',side='right',pady=5) 
        
        # GRID SETUP
        tree_frame.rowconfigure(0,weight=1)
        tree_frame.rowconfigure((1,2),weight=4)
        tree_frame.columnconfigure((0,1,2),weight=4)
        tree_frame.columnconfigure(3,weight=1)     
   
        # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(tree_frame,
                                  width=200,
                                  textvariable=self.search_bar_var)
        self.search_bar.grid(row=0,column=2,sticky='we',padx=5)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProducto())

        # BOTONES TREEVIEW     
        cancel_btn = ctk.CTkButton(tree_frame,
                                    text='Cancelar',
                                    command=self.Cancel,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=0,column=1,sticky='e',padx=5)

        # TREEVIEW
        self.treeview = ttk.Treeview(tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Precio','Cantidad'))
        self.treeview.grid(row=1,column=0,sticky='nswe',padx=10,pady=10,rowspan=2,columnspan=3)

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
        scrollbar = ctk.CTkScrollbar(tree_frame,
                                     orientation='vertical',
                                     command=self.treeview.yview)
        scrollbar.grid(row=1,column=3,sticky='ns',padx=5,pady=5,rowspan=2)
        self.treeview.configure(yscrollcommand=scrollbar.set)


        # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()



    # FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES - FUNCION BOTONES
    # FUNCION BOTON AGREGAR PRODUCTO
    def AgregarProducto(self):
        codigo = self.codigo_var.get()
        linea = self.lin_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        canti = self.canti_var.get()

        if LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(grupo):
            producto = Product(codigo,linea,grupo,prove,nombre,precio,canti)
            INVENTARIO.AddProduct(producto.ToDict())
            # SE AGREGA EL NUEVO PRODUCTO AL TREEVIEW
            self.treeview.insert("",'end',text=codigo,values=(linea,grupo,prove,nombre,precio,canti))
            self.inventario = INVENTARIO.GetInventory()

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
            self.treeview.insert("",'end',text=producto['codigo'],values=(
                                                                producto['linea'],
                                                                producto['grupo'],
                                                                producto['proveedor'],
                                                                producto['nombre'],
                                                                producto['precio'],
                                                                producto['cantidad']))
    # BUSCAR UN PRODUCTO CON LA BARRA DE BUSQUEDA    
    def BuscarProducto(self):
        codigo = self.search_bar_var.get()
        if codigo not in self.inventario:
            messagebox.showerror('Error de busqueda',f'El producto con codigo {codigo} no existe')
        else:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            producto = self.inventario[codigo]
            # MOSTRAR EN LISTA SOLO EL PRODUCTO ELEGIDO
            self.treeview.insert("",'end',text=producto['codigo'],values=(
                                                                producto['linea'],
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
            
    def ModificarProducto(self):
        linea = self.lin_var.get().split(" - ")[0].strip()
        grupo = self.grupo_var.get()
        prove = self.prove_var.get()
        nombre = self.nombre_var.get()
        precio = self.precio_var.get()
        canti = self.canti_var.get()
        if LINE_MANAGER.CheckLine(linea) and LINE_MANAGER.CheckGrupo(grupo):
            producto = Product(self.mod_codi,linea,grupo,prove,nombre,precio,canti)
            INVENTARIO.EditProduct(producto.ToDict())
            self.ListInventory()
            self.Restablecer()

    def Cancel(self):
        self.ListInventory()
        self.Restablecer()

    def EliminarProducto(self):
        answer = messagebox.askyesno('Atencion','¿Desea eliminar el producto?')
        if answer:
            INVENTARIO.DelProduct(self.mod_codi)
            self.ListInventory()
            self.Restablecer()

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