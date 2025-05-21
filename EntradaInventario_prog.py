import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from DatabaseManager import INVENTARIO, LINE_MANAGER, PROV_MANAGER
from style import*

# PROGRAMA DE CARGA DE PRODUCTOS
class EntradasInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')

        title = ctk.CTkLabel(title_frame,
                             text='Entradas a inventario',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=10)
    # PROG FRAME
        self.prog_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.prog_frame.pack(expand=True,fill='both',side='left')
    # GRID SETUP
        for rows in range(20):
            self.prog_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(12):
            self.prog_frame.columnconfigure(columns,weight=1,uniform='column')
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # NUMERO - CODIGO DE PEDIDO
        self.num_pedido_var = tk.StringVar()
        self.num_pedido_entry = ctk.CTkEntry(self.prog_frame,
                                             textvariable=self.num_pedido_var,
                                             fg_color=APP_COLORS[6])
        self.num_pedido_entry.grid(row=4,column=1,columnspan=2,padx=5,sticky='we')
        # PROVEEDOR
        self.proveedor_var = tk.StringVar()
        self.proveedor_entry = ctk.CTkEntry(self.prog_frame,
                                            state='disabled',
                                            textvariable=self.proveedor_var,
                                            fg_color=APP_COLORS[6])
        self.proveedor_entry.grid(row=4,column=3,columnspan=2,padx=5,sticky='we')
        # FECHA
        self.fecha_entry_var = tk.StringVar()
        self.fecha_entry = ctk.CTkEntry(self.prog_frame,
                                        state='disabled',
                                        textvariable=self.fecha_entry_var,
                                        fg_color=APP_COLORS[6])
        self.fecha_entry.grid(row=4,column=5,columnspan=1,padx=5,sticky='we')
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # NUMERO - CODIGO DE PEDIDO
        num_pedido_label = ctk.CTkLabel(self.prog_frame,
                                        text='Numero de pedido',
                                        font=FONTS[1],
                                        text_color=APP_COLORS[4])
        num_pedido_label.grid(row=3,column=1,columnspan=2,padx=5,sticky='w')
        # PROVEEDOR
        proveedor_label = ctk.CTkLabel(self.prog_frame,
                                        text='Proveedor',
                                        font=FONTS[1],
                                        text_color=APP_COLORS[4])
        proveedor_label.grid(row=3,column=4,columnspan=2,padx=5,sticky='w')
        # FECHA - 
        fecha_pedido_label = ctk.CTkLabel(self.prog_frame,
                                        text='Fecha del pedido',
                                        font=FONTS[1],
                                        text_color=APP_COLORS[4])
        fecha_pedido_label.grid(row=3,column=5,columnspan=2,padx=5,sticky='w')
    # MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU -
        self.prov_menu = ctk.CTkOptionMenu(self.prog_frame,
                                           values=PROV_MANAGER.GetProvNames(),
                                           command=self.SelectProvMenu,
                                           fg_color=APP_COLORS[2],
                                           button_color=APP_COLORS[3],
                                           button_hover_color=APP_COLORS[2])
        self.prov_menu.grid(row=3,column=3,columnspan=1,padx=5,sticky='we')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        salir_btn = ctk.CTkButton(self.prog_frame,
                                       text='Volver atrás',
                                       command=self.GoBack_CB,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[4],
                                       hover_color=APP_COLORS[3])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5,pady=5)
        # ABRIR CALENDARIO
        btn_calendario = ctk.CTkButton(self.prog_frame,
                                       text="←",
                                       width=25,
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3],
                                       command=self.abrir_calendario)
        btn_calendario.grid(row=4,column=6,sticky='w')
        # AGREGAR ENTRADA
        btn_agregar_entrada = ctk.CTkButton(self.prog_frame,
                                            text="Agregar producto",
                                            width=25,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.BusquedaProducto)
        btn_agregar_entrada.grid(row=4,column=9,columnspan=2,sticky='we',padx=5)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW
        self.treeview_entradas = ttk.Treeview(self.prog_frame,
                                     style='Custom.Treeview',
                                     columns=('Nombre','Costo','Cantidad'))
        self.treeview_entradas.grid(row=5,column=1,sticky='nswe',padx=10,pady=10,rowspan=14,columnspan=10)
        # CODIGO
        self.treeview_entradas.heading('#0',text='Codigo')
        self.treeview_entradas.column('#0',width=50,anchor='center')
        # NOMBRE - DESCRIPCION
        self.treeview_entradas.heading('Nombre',text='Descripción')
        self.treeview_entradas.column('Nombre',width=200,anchor='center')
        # COSTO
        self.treeview_entradas.heading('Costo',text='Costo')
        self.treeview_entradas.column('Costo',width=100,anchor='center')
        # CANTIDAD
        self.treeview_entradas.heading('Cantidad',text='Cantidad')
        self.treeview_entradas.column('Cantidad',width=50,anchor='center')
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
        scrollbar = ctk.CTkScrollbar(self.prog_frame,
                                     orientation='vertical',
                                     command=self.treeview_entradas.yview)
        scrollbar.grid(row=5,column=11,sticky='nsw',padx=5,pady=5,rowspan=14)
        self.treeview_entradas.configure(yscrollcommand=scrollbar.set)
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 

# CLICK ON MENU
    def SelectProvMenu(self,opcion):
        self.proveedor_var.set(opcion)

# CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - 
    def abrir_calendario(self):
        top = tk.Toplevel(self.prog_frame)
        top.title('Seleccionar Fecha')
        top.grab_set()  # para hacer que la ventana emergente sea modal
        cal = Calendar(top, locale='es_ES', date_pattern='dd/mm/yyyy',
                       background=APP_COLORS[3],headersforeground=APP_COLORS[0],
                       headersbackground = APP_COLORS[4], selectbackground = APP_COLORS[2],
                       font=('Arial', 18),headersfont=('Arial', 16))
        cal.pack(pady=20, padx=20)
        def seleccionar_fecha():
            fecha = cal.get_date()
            self.fecha_entry_var.set(fecha)
            top.destroy()
        btn_seleccionar = ctk.CTkButton(top,
                                        fg_color=APP_COLORS[2],
                                        hover_color=APP_COLORS[3],
                                        text="Aceptar",
                                        command=seleccionar_fecha)
        btn_seleccionar.pack(pady=10)
# BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
    def BusquedaProducto(self):
    # TREEVIEW - TREEVIEW
    # FRAME DEL TREEVIEW
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('700x450')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.transient(self)
    # GRID SETUP
        for rows in range(10):
            self.tree_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(8):
            self.tree_frame.columnconfigure(columns,weight=1,uniform='column')     
    # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                  width=200,
                                  textvariable=self.search_bar_var)
        self.search_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
    # CANTIDAD
        self.cantidad_var = tk.IntVar()
        self.cantidad = ctk.CTkEntry(self.tree_frame,
                                  width=200,
                                  textvariable=self.cantidad_var)
        self.cantidad.grid(row=1,column=4,columnspan=2,sticky='we',padx=5)
        self.cantidad.bind("<Return>",lambda event:self.AgregarProducto())
    # LABEL
        label_cantidad = ctk.CTkLabel(self.tree_frame,
                             text='Cantidad del producto',
                             font=FONTS[1],
                                        text_color=APP_COLORS[4])
        label_cantidad.grid(row=0,column=4,columnspan=3,sticky='w',padx=5)
    # LABEL
        label = ctk.CTkLabel(self.tree_frame,
                             text='Busqueda por nombre',
                             font=FONTS[1],
                                        text_color=APP_COLORS[4])
        label.grid(row=0,column=0,columnspan=3,sticky='w',padx=5)
    # BOTONES TREEVIEW     
    # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=1,column=2,sticky='w',padx=5)
    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=7,columnspan=7)
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
        scrollbar.grid(row=2,column=7,sticky='nsw',padx=5,pady=5,rowspan=2)
        self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()
# LISTAR INVENTARIO DE LA BUSQUEDA DE PRODDUCTOS
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
# BUSCAR PRODUCTO POR NOMBRE
    def BuscarProductoNombre(self):
        inventario = INVENTARIO.GetInventory()
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
# CLICK ON TREEVIEW
    def ClickTreeview(self,event):
        inventario = INVENTARIO.GetCodigos()
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        codigo = info['text']
        self.search_bar_var.set(codigo)
        
        
    def AgregarProducto(self):
        inventario = INVENTARIO.GetCodigos()
        codigo = self.search_bar_var.get()
        cantidad = self.cantidad_var.get()
        if codigo in inventario:
            producto = INVENTARIO.GetProducto(codigo)
            self.treeview_entradas.insert("",'end',
                                 text=producto['codigo'],
                                 values=(producto['nombre'],
                                         producto['costo'],
                                         cantidad))
            self.tree_frame.destroy()
        
        
