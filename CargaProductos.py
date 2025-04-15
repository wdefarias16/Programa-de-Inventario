import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
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
        for rows in range(10):
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
        lin_menu.grid(row=4,column=1,columnspan=2,sticky='we',padx=5)

        self.grup_menu = ctk.CTkOptionMenu(entry_frame,
                                      values=LINE_MANAGER.GetGroupNames(self.codigoActualLinea),
                                      command=self.SelectGruMenu)
        self.grup_menu.grid(row=5,column=1,columnspan=2,sticky='we',padx=5)

        prov_menu = ctk.CTkOptionMenu(entry_frame,
                                      values=PROV_MANAGER.GetProvNames(),
                                      command=self.SelectProvMenu)
        prov_menu.grid(row=6,column=1,columnspan=2,sticky='we',padx=5)
        
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        self.codigo_var = tk.StringVar()
        codigo_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.codigo_var)
        codigo_entry.grid(row=3,column=3,columnspan=2,sticky='we')

        linea_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.lin_var)
        linea_entry.grid(row=4,column=3,columnspan=2,sticky='we')

        self.grupo_var = tk.StringVar()
        grupo_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.grupo_var)
        grupo_entry.grid(row=5,column=3,columnspan=2,sticky='we')

        self.prove_var = tk.StringVar()
        prove_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.prove_var)
        prove_entry.grid(row=6,column=3,columnspan=2,sticky='we')

        self.nombre_var = tk.StringVar()
        nombre_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.nombre_var)
        nombre_entry.grid(row=7,column=3,columnspan=2,sticky='we')

        self.precio_var = tk.DoubleVar()
        precio_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=self.precio_var)
        precio_entry.grid(row=8,column=3,columnspan=2,sticky='we')

        self.canti_var = tk.IntVar()
        canti_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=self.canti_var)
        canti_entry.grid(row=9,column=3,columnspan=2,sticky='we')

        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        
        he_label = ctk.CTkLabel(entry_frame,
                                    text='Datos del producto',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        he_label.grid(row=1,column=3,columnspan=2,sticky='w')
        
        codigo_label = ctk.CTkLabel(entry_frame,
                                    text='Codigo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        codigo_label.grid(row=3,column=5,columnspan=2,sticky='w',padx=5)

        linea_label = ctk.CTkLabel(entry_frame,
                                    text='Línea',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        linea_label.grid(row=4,column=5,columnspan=2,sticky='w',padx=5)

        grupo_label = ctk.CTkLabel(entry_frame,
                                    text='Grupo',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        grupo_label.grid(row=5,column=5,columnspan=2,sticky='w',padx=5)

        prove_label = ctk.CTkLabel(entry_frame,
                                    text='Proveedor',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        prove_label.grid(row=6,column=5,columnspan=2,sticky='w',padx=5)

        nombre_label = ctk.CTkLabel(entry_frame,
                                    text='Nombre',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        nombre_label.grid(row=7,column=5,columnspan=2,sticky='w',padx=5)        

        precio_label = ctk.CTkLabel(entry_frame,
                                    text='Precio',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        precio_label.grid(row=8,column=5,columnspan=2,sticky='w',padx=5)

        canti_label = ctk.CTkLabel(entry_frame,
                                    text='Cantidad',
                                    font=FONTS[1],
                                    text_color=APP_COLORS[4])
        canti_label.grid(row=9,column=5,columnspan=2,sticky='w',padx=5)

        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 

        add_foto_btn = ctk.CTkButton(entry_frame,
                                     text='Agregar Foto')
        add_foto_btn.grid(row=11,column=1,columnspan=2,sticky='we',padx=5)

        guardar_btn = ctk.CTkButton(entry_frame,
                                     text='Agregar',
                                     command=self.AgregarProducto)
        guardar_btn.grid(row=11,column=3,columnspan=2,sticky='we')
        
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # FRAME DEL TREEVIEW
        tree_frame = ctk.CTkFrame(self,
                                   corner_radius=5,
                                   fg_color=APP_COLORS[5])
        tree_frame.pack(expand=True,fill='both',side='left',pady=5)

        # TREEVIEW
        self.treeview = ttk.Treeview(tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Precio','Cantidad'))
        self.treeview.pack(expand=True,fill='both',padx=10,pady=10)

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
            self.treeview.insert("",'end',text=codigo,values=(linea,grupo,prove,nombre,precio,canti))

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


    def ListInventory(self):
        self.inventario = INVENTARIO.GetInventory()

        for producto in self.inventario.values():
            self.treeview.insert("",'end',text=producto['codigo'],values=(
                                                                producto['linea'],
                                                                producto['grupo'],
                                                                producto['proveedor'],
                                                                producto['nombre'],
                                                                producto['precio'],
                                                                producto['cantidad']))
            #Prueba

