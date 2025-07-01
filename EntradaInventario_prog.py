import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from DatabaseManager import INVENTARIO, PROV_MANAGER
from style import*
import win32api
import os
import tempfile
import platform
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.styles import ParagraphStyle

# PROGRAMA DE CARGA DE PRODUCTOS
class EntradasInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.validardigit = self.register(self.ValidarDigitos)
        self.lista_productos = []
        self.total_prev = 0.0
        self.inventory_codes = []
        self.iva_default = 0
        self.flete_default = 0
        
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
                                             fg_color=APP_COLORS[6],
                                             border_color=APP_COLORS[2])
        self.num_pedido_entry.grid(row=4,column=1,columnspan=2,padx=5,sticky='we')
        self.num_pedido_entry.focus()
        self.num_pedido_entry.bind("<Return>", self.ObtenerEntrada)
        # PROVEEDOR
        self.proveedor_var = tk.StringVar()
        self.proveedor_entry = ctk.CTkEntry(self.prog_frame,
                                            textvariable=self.proveedor_var,
                                            fg_color=APP_COLORS[6],
                                            border_color=APP_COLORS[2])
        self.proveedor_entry.grid(row=4,column=3,columnspan=2,padx=5,sticky='we')
        self.proveedor_entry.bind("<Return>",lambda event:self.BuscarProvCodigo())
        # FECHA
        self.fecha_entry_var = tk.StringVar()
        self.fecha_entry = ctk.CTkEntry(self.prog_frame,
                                        state='disabled',
                                        textvariable=self.fecha_entry_var,
                                        fg_color=APP_COLORS[6],
                                        border_color=APP_COLORS[2])
        self.fecha_entry.grid(row=4,column=5,columnspan=1,padx=5,sticky='we')
        # TOTAL
        self.total_entry_var = tk.StringVar()
        self.total_entry_var.set(self.total_prev)
        self.total_entry = ctk.CTkEntry(self.prog_frame,
                                        state='disabled',
                                        textvariable=self.total_entry_var,
                                        fg_color=APP_COLORS[8],
                                        border_color=APP_COLORS[8])
        self.total_entry.grid(row=15,column=10,columnspan=1,padx=5,sticky='we')
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # NUMERO - CODIGO DE PEDIDO
        num_pedido_label = ctk.CTkLabel(self.prog_frame,
                                        text='Número de factura',
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
        # TOTAL
        total_label = ctk.CTkLabel(self.prog_frame,
                                        text='Previsualización Total:',
                                        font=FONTS[1],
                                        text_color=APP_COLORS[4])
        total_label.grid(row=15,column=8,columnspan=2,padx=5,sticky='e')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        salir_btn = ctk.CTkButton(self.prog_frame,
                                       text='Volver atrás',
                                       command=self.GoBack_CB,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[4],
                                       hover_color=APP_COLORS[3])
        salir_btn.grid(row=0,column=0,sticky='nw',padx=5,pady=5)
        # AYUDA DE PROVEEDORES
        prov_help_btn = ctk.CTkButton(self.prog_frame,
                                       text='Proveedores',
                                       command=self.AyudaProveedores,
                                       text_color=APP_COLORS[0],
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3])
        prov_help_btn.grid(row=3,column=3,columnspan=1,padx=5,sticky='we')
        # ABRIR CALENDARIO
        self.btn_calendario = ctk.CTkButton(self.prog_frame,
                                            text="←",
                                            width=25,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.AbrirCalendario)
        self.btn_calendario.grid(row=4, column=6, sticky='w')
        # AGREGAR ENTRADA
        self.btn_agregar_entrada = ctk.CTkButton(self.prog_frame,
                                            text="Agregar producto",
                                            width=25,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.BusquedaProducto)
        self.btn_agregar_entrada.grid(row=4,column=9,columnspan=2,sticky='we',padx=5)
        # GUARDAR ENTRADA
        self.btn_guardar_entrada = ctk.CTkButton(self.prog_frame,
                                            text="Guardar Entrada",
                                            width=25,
                                            fg_color=APP_COLORS[8],
                                            hover_color=APP_COLORS[3],
                                            command=self.GuardarFactura)
        self.btn_guardar_entrada.grid(row=1,column=9,columnspan=2,sticky='we',padx=5)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW
        self.treeview_entradas = ttk.Treeview(self.prog_frame,
                                     style='Custom.Treeview',
                                     columns=('Nombre','Cantidad','Costo',
                                              'Descuento_1','Descuento_2','Descuento_3',
                                              'Flete','Neto','Iva','Neto_IVA','SubTotal'))
        self.treeview_entradas.grid(row=5,column=1,sticky='nswe',padx=10,pady=10,rowspan=10,columnspan=10)
        self.treeview_entradas.bind("<<TreeviewSelect>>",self.ClickEntrada)
        # CODIGO
        self.treeview_entradas.heading('#0',text='Código')
        self.treeview_entradas.column('#0',width=50,anchor='center')
        # NOMBRE - DESCRIPCION
        self.treeview_entradas.heading('Nombre',text='Descripción')
        self.treeview_entradas.column('Nombre',width=200,anchor='center')
        # CANTIDAD
        self.treeview_entradas.heading('Cantidad',text='Cantidad')
        self.treeview_entradas.column('Cantidad',width=50,anchor='center')
        # COSTO
        self.treeview_entradas.heading('Costo',text='Costo')
        self.treeview_entradas.column('Costo',width=50,anchor='center')
        # DESCUENTO 1
        self.treeview_entradas.heading('Descuento_1',text='Dto. 1')
        self.treeview_entradas.column('Descuento_1',width=50,anchor='center')
        # DESCUENTO 2
        self.treeview_entradas.heading('Descuento_2',text='Dto. 2')
        self.treeview_entradas.column('Descuento_2',width=50,anchor='center')
        # DESCUENTO 3
        self.treeview_entradas.heading('Descuento_3',text='Dto. 3')
        self.treeview_entradas.column('Descuento_3',width=50,anchor='center')
        # FLETE
        self.treeview_entradas.heading('Flete',text='Flete')
        self.treeview_entradas.column('Flete',width=50,anchor='center')
        # NETO
        self.treeview_entradas.heading('Neto',text='Neto')
        self.treeview_entradas.column('Neto',width=50,anchor='center')
        # IVA
        self.treeview_entradas.heading('Iva',text='I.V.A.')
        self.treeview_entradas.column('Iva',width=80,anchor='center')
        # NETO + IVA 
        self.treeview_entradas.heading('Neto_IVA',text='Neto + I.V.A.')
        self.treeview_entradas.column('Neto_IVA',width=50,anchor='center')
        # SUBTOTAL
        self.treeview_entradas.heading('SubTotal',text='SubTotal')
        self.treeview_entradas.column('SubTotal',width=50,anchor='center')
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
        scrollbar.grid(row=5,column=11,sticky='nsw',padx=5,pady=5,rowspan=10)
        self.treeview_entradas.configure(yscrollcommand=scrollbar.set)

# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - 
    def AbrirCalendario(self):
        top = tk.Toplevel(self.prog_frame)
        top.title('Seleccionar Fecha')
        top.grab_set()
        top.protocol("WM_DELETE_WINDOW", lambda: None)
        top.transient(self)
        top.bind("<Return>",)
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
# BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
# BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
    def BusquedaProducto(self):
    # TREEVIEW - TREEVIEW
    # FRAME DEL TREEVIEW
        self.btn_agregar_entrada.configure(state='disabled')
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('800x550')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        self.tree_frame.transient(self)
    # GRID SETUP
        for rows in range(16):
            self.tree_frame.rowconfigure(rows, weight=1,uniform='a')
        for columns in range(24):
            self.tree_frame.columnconfigure(columns,weight=1,uniform='a')

        # TITULO
        title_frame = ctk.CTkFrame(self.tree_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=24,sticky='nswe')

        title = ctk.CTkLabel(title_frame,
                             text='Busqueda de productos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[3])
        title.pack(pady=10)  
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                       width=200,
                                       textvariable=self.search_bar_var,
                                       fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.search_bar.grid(row=2,column=0,columnspan=2,sticky='we',padx=20)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
        self.search_bar.bind("<Control-BackSpace>", lambda event: self.ListInventory())
        # CANTIDAD
        self.cantidad_var = tk.StringVar()
        self.cantidad_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validardigit,'%P'),
                                     textvariable = self.cantidad_var,
                                     width=100,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.cantidad_entry.grid(row=4,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.cantidad_entry.bind("<Return>",lambda event:self.costo_entry.focus_set())
        # COSTO
        self.costo_var = tk.StringVar()
        self.costo_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validardigit,'%P'),
                                     textvariable = self.costo_var,
                                     width=100,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.costo_entry.grid(row=5,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.costo_entry.bind("<Return>",lambda event:self.descuento_1_entry.focus_set())
        # DESCUENTO 1
        self.descuento_1_var = tk.StringVar()
        self.descuento_1_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            validate = 'key',
                                            validatecommand = (self.validardigit,'%P'),
                                            width=100,
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4],
                                            textvariable = self.descuento_1_var)
        self.descuento_1_entry.grid(row=6,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.descuento_1_entry.bind("<Return>",lambda event:self.descuento_2_entry.focus())
        # DESCUENTO 2
        self.descuento_2_var = tk.StringVar()
        self.descuento_2_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            validate = 'key',
                                            validatecommand = (self.validardigit,'%P'),
                                            width=100,
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4],
                                            textvariable = self.descuento_2_var)
        self.descuento_2_entry.grid(row=7,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.descuento_2_entry.bind("<Return>",lambda event:self.descuento_3_entry.focus())
        # DESCUENTO 3
        self.descuento_3_var = tk.StringVar()
        self.descuento_3_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            validate = 'key',
                                            validatecommand = (self.validardigit,'%P'),
                                            width=100,
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4],
                                            textvariable = self.descuento_3_var)
        self.descuento_3_entry.grid(row=8,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.descuento_3_entry.bind("<Return>",lambda event:self.flete_entry.focus())
        # FLETE
        self.flete_entry_var = tk.StringVar()
        self.flete_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            validate = 'key',
                                            validatecommand = (self.validardigit,'%P'),
                                            width=100,
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4],
                                            textvariable = self.flete_entry_var)
        self.flete_entry.grid(row=9,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.flete_entry_var.set(self.flete_default)
        self.flete_entry.bind("<Return>",lambda event:self.iva_entry.focus())
        # IVA
        self.iva_var = tk.StringVar()
        self.iva_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validardigit,'%P'),
                                     textvariable = self.iva_var,
                                     width=100,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.iva_entry.grid(row=10,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.iva_var.set(self.iva_default)
        self.iva_entry.bind("<Return>",lambda event:self.AgregarProducto())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # BUSQUEDA
        label_busqueda = ctk.CTkLabel(self.tree_frame,
                             text='Busqueda por nombre',
                             font=FONTS[1],
                                        text_color=APP_COLORS[4])
        label_busqueda.grid(row=1,column=0,columnspan=3,sticky='w',padx=20)
        # CANTIDAD
        label_cantidad = ctk.CTkLabel(self.tree_frame,
                                      text='Cantidad',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_cantidad.grid(row=4,column=1,columnspan=3,sticky='w',padx=20)
        # COSTO
        label_costo = ctk.CTkLabel(self.tree_frame,
                                      text='Costo',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_costo.grid(row=5,column=1,columnspan=3,sticky='w',padx=20)
        # DESCUENTO 1
        label_descuento_1 = ctk.CTkLabel(self.tree_frame,
                                       text='Descuento 1',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_descuento_1.grid(row=6,column=1,columnspan=3,sticky='w',padx=20)
        # DESCUENTO 2
        label_descuento_2 = ctk.CTkLabel(self.tree_frame,
                                       text='Descuento 2',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_descuento_2.grid(row=7,column=1,columnspan=3,sticky='w',padx=20)
        # DESCUENTO 3
        label_descuento_3 = ctk.CTkLabel(self.tree_frame,
                                       text='Descuento 3',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_descuento_3.grid(row=8,column=1,columnspan=3,sticky='w',padx=20)
        # FLETE
        label_flete = ctk.CTkLabel(self.tree_frame,
                                       text='Flete',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_flete.grid(row=9,column=1,columnspan=3,sticky='w',padx=20)
        # IVA
        label_iva = ctk.CTkLabel(self.tree_frame,
                                      text='I.V.A.',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_iva.grid(row=10,column=1,columnspan=3,sticky='w',padx=20)
    # BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - 
        # LIMPIAR BUSQUEDA
        clear_btn = ctk.CTkButton(self.tree_frame,
                                    text='Limpiar Búsqueda',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        clear_btn.grid(row=1,column=5,columnspan=2,sticky='w',padx=10)
        # CANCELAR
        def CloseAddProdWindow():
            self.tree_frame.destroy()
            self.btn_agregar_entrada.configure(state='enabled')
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=CloseAddProdWindow,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=14,column=0,columnspan=2,sticky='w',padx=10)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=2,column=2,sticky='nswe',padx=10,rowspan=13,columnspan=21)
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
        scrollbar.grid(row=2,column=23,sticky='nsw',pady=5,rowspan=13)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()
# AGREGAR PRODUCTO A LA LISTA
    def AgregarProducto(self):
        if not self.inventory_codes:
            self.inventory_codes = INVENTARIO.GetCodigos()

        codigo = self.search_bar_var.get()
        if codigo in self.lista_productos:
            messagebox.showerror('Error', f'Producto con código {codigo} ya se encuentra en la lista.')
            return

        if codigo not in self.inventory_codes:
            messagebox.showerror('Error', f'Producto con código {codigo} no se encuentra en la base de datos.')
            return
        
        campos = {
            "cantidad": self.cantidad_var.get(),
            "costo": self.costo_var.get(),
            "descuento_1": self.descuento_1_var.get(),
            "descuento_2": self.descuento_2_var.get(),
            "descuento_3": self.descuento_3_var.get(),
            "flete": self.flete_entry_var.get(),
            "iva": self.iva_var.get()
        }

        try:
            # Parsear y asegurar valores numéricos válidos
            cantidad = int(campos["cantidad"])
            costo = float(campos["costo"])
            descuento_1 = float(campos["descuento_1"] or 0)
            descuento_2 = float(campos["descuento_2"] or 0)
            descuento_3 = float(campos["descuento_3"] or 0)
            flete = float(campos["flete"] or 0)
            iva = float(campos["iva"] or 0)
        except ValueError:
            messagebox.showerror('Error', 'Verifica que todos los campos numéricos estén correctamente llenos.')
            return

        if cantidad <= 0:
            messagebox.showerror('Error', 'Agregue la cantidad del producto.')
            self.cantidad_entry.focus()
            return
        if costo <= 0:
            messagebox.showerror('Error', 'Agregue el costo del producto.')
            self.costo_entry.focus()
            return

        def aplicar_descuentos(valor, *descuentos):
            for d in descuentos:
                valor -= valor * (d / 100)
            return round(valor, 2)

        neto = aplicar_descuentos(costo, descuento_1, descuento_2, descuento_3)

        if flete > 0:
            neto = round(neto * (1 + flete / 100), 2)
            self.flete_default = flete

        if iva > 0:
            neto_iva = round(neto * (1 + iva / 100), 2)
            iva_dif = round(neto_iva - neto, 2)
            self.iva_default = iva
        else:
            neto_iva = neto
            iva_dif = 0

        subtotal = round(cantidad * (neto_iva or neto), 2)

        producto = INVENTARIO.GetProducto(codigo)
        self.treeview_entradas.insert("", 'end',
            text=producto['codigo'],
            values=(
                producto['nombre'],
                cantidad,
                ('$', costo),
                (descuento_1, '%'),
                (descuento_2, '%'),
                (descuento_3, '%'),
                (flete, '%'),
                ('$', neto),
                (f'${iva_dif} - {iva}%'),
                ('$', neto_iva),
                ('$', subtotal)
            )
        )
        self.btn_agregar_entrada.configure(state='enabled')
        self.lista_productos.append(str(codigo).strip())
        self.TotalPrev()
        self.tree_frame.destroy()

# LISTAR INVENTARIO DE LA BUSQUEDA DE PRODDUCTOS
    def ListInventory(self):
        self.cantidad_var.set('')
        self.costo_var.set('')
        self.descuento_1_var.set('')
        self.descuento_2_var.set('')
        self.descuento_3_var.set('')
        self.flete_entry_var.set('')
        self.iva_var.set('')
        self.search_bar.after(100,
            lambda:  self.search_bar.configure(state='normal',
                                               fg_color=APP_COLORS[6],border_color=APP_COLORS[6]))
        self.search_bar_var.set('')
        self.search_bar.after(100,self.search_bar.focus())
        self.costo_entry.after(100,
            lambda: self.costo_entry.configure(state='disabled',
                                               fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.cantidad_entry.after(100,
            lambda: self.cantidad_entry.configure(state='disabled',
                                                  fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.descuento_1_entry.after(100,
            lambda: self.descuento_1_entry.configure(state='disabled',
                                                   fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.descuento_2_entry.after(100,
            lambda: self.descuento_2_entry.configure(state='disabled',
                                                   fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.descuento_3_entry.after(100,
            lambda: self.descuento_3_entry.configure(state='disabled',
                                                   fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.flete_entry.after(100,
            lambda: self.flete_entry.configure(state='disabled',
                                                   fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.iva_entry.after(100,
            lambda: self.iva_entry.configure(state='disabled',
                                                   fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
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
                                         f'$ {producto['costo']}'))

# BUSCAR PRODUCTO POR NOMBRE
    def BuscarProductoNombre(self):
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
# CLICK ON TREEVIEW - BUSQUEDA DE PRODUCTO
    def ClickTreeview(self,event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        codigo = info['text']
        try:
            costo = info['values'][4].split(' ')[1].strip()
        except IndexError:
            costo = ''
        self.search_bar_var.set(codigo)
        self.search_bar.configure(state='disabled',fg_color=APP_COLORS[4],
                                  border_color=APP_COLORS[4])
        self.costo_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                   border_color=APP_COLORS[6])
        self.costo_var.set(costo)
        self.cantidad_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                      border_color=APP_COLORS[6])
        self.descuento_1_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.descuento_2_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.descuento_3_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.flete_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.flete_entry_var.set(self.flete_default)
        self.iva_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.iva_var.set(self.iva_default)
        self.cantidad_entry.focus_set()
# SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR -
# SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR -
# SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR -    
# SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR -
    def ClickEntrada(self,event):
        self.item_id = self.treeview_entradas.selection()
        if not self.item_id:
            print("Advertencia: No hay ningún elemento seleccionado.")
            return
        info = self.treeview_entradas.item(self.item_id)
        self.codigo = str(info['text']).strip()
        datos = info['values']
        self.nombre = datos[0]
        cantidad = datos[1]
        costo = float(datos[2].split(' ')[1])
        porcentaje = float(datos[3].split(' ')[0])
        iva = float(datos[5].split(' ')[0])
        
        # FRAME DE EDICION DE ENTRADAS
        self.edit_window = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[0])
        self.edit_window.geometry('600x350')
        self.edit_window.title('Editar')
        self.edit_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.edit_window.transient(self)
        edit_frame = ctk.CTkFrame(self.edit_window,corner_radius=5,fg_color=APP_COLORS[0])
        edit_frame.pack(expand=True,fill='both')
    # GRID SETUP
        for rows in range(12):
            edit_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(10):
            edit_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
        title_frame = ctk.CTkFrame(edit_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')

        title = ctk.CTkLabel(title_frame,
                             text='Editar entrada',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[3])
        title.pack(pady=10)
    # PRODUCTO
        producto_label = ctk.CTkLabel(edit_frame,
                                      text=self.nombre,
                                      font=FONTS[4],
                                      text_color=APP_COLORS[4],
                                      bg_color='transparent')
        producto_label.grid(row = 2, column = 1, columnspan = 6, padx = 10, sticky = 'w')
    # ENTRADAS
        # CANTIDAD
        self.cantidad_edit_var = tk.StringVar()
        self.cantidad_edit_var.set(cantidad)
        self.cantidad_edit_entry = ctk.CTkEntry(edit_frame,
                                                state='disabled',
                                                textvariable=self.cantidad_edit_var,
                                                validate = 'key',
                                                validatecommand = (self.validardigit,'%P'),
                                                fg_color=APP_COLORS[6],
                                                border_width=0)
        self.cantidad_edit_entry.grid(row = 4, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.cantidad_edit_entry.bind("<Return>",lambda event:self.costo_edit_entry.focus_set())
        # COSTO
        self.costo_edit_var = tk.StringVar()
        self.costo_edit_var.set(costo)
        self.costo_edit_entry = ctk.CTkEntry(edit_frame,
                                             validate = 'key',
                                             validatecommand = (self.validardigit,'%P'),
                                             state='disabled',
                                             textvariable=self.costo_edit_var,
                                             fg_color=APP_COLORS[6],
                                             border_width=0)
        self.costo_edit_entry.grid(row = 5, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.costo_edit_entry.bind("<Return>",lambda event:self.porcentaje_1_edit_entry.focus_set())
        # PORCENTAJE 1
        self.porcentaje_1_edit_var = tk.StringVar()
        self.porcentaje_1_edit_var.set(porcentaje)
        self.porcentaje_1_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.porcentaje_1_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.porcentaje_1_edit_entry.grid(row = 6, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.porcentaje_1_edit_entry.bind("<Return>",lambda event: self.porcentaje_2_edit_entry.focus_set())
        # PORCENTAJE 2
        self.porcentaje_2_edit_var = tk.StringVar()
        self.porcentaje_2_edit_var.set(porcentaje)
        self.porcentaje_2_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.porcentaje_2_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.porcentaje_2_edit_entry.grid(row = 7, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.porcentaje_2_edit_entry.bind("<Return>",lambda event: self.porcentaje_3_edit_entry.focus_set())
        # PORCENTAJE 3
        self.porcentaje_3_edit_var = tk.StringVar()
        self.porcentaje_3_edit_var.set(porcentaje)
        self.porcentaje_3_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.porcentaje_3_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.porcentaje_3_edit_entry.grid(row = 8, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.porcentaje_3_edit_entry.bind("<Return>",lambda event: self.iva_edit_entry.focus_set())
        # FLETE
        self.flete_edit_var = tk.StringVar()
        self.flete_edit_var.set(porcentaje)
        self.flete_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.flete_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.flete_edit_entry.grid(row = 9, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.flete_edit_entry.bind("<Return>",lambda event: self.iva_edit_entry.focus_set())
        # IVA
        self.iva_edit_var = tk.StringVar()
        self.iva_edit_var.set(iva)
        self.iva_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.iva_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.iva_edit_entry.grid(row = 10, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        self.iva_edit_entry.bind("<Return>",lambda event: self.ModEntrada())
    # LABELS
        # CANTIDAD
        cantidad_label = ctk.CTkLabel(edit_frame,
                                      text=f'Cantidad',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        cantidad_label.grid(row = 4, column = 3, columnspan = 2, sticky = 'w')
        # COSTO
        costo_label = ctk.CTkLabel(edit_frame,
                                      text=f'Costo $',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        costo_label.grid(row = 5, column = 3, columnspan = 2, sticky = 'w')
        # PORCENTAJE 1
        porcentaje_1_label = ctk.CTkLabel(edit_frame,
                                      text=f'Descuento 1',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        porcentaje_1_label.grid(row = 6, column = 3, columnspan = 2, sticky = 'w')
        # PORCENTAJE 2
        porcentaje_2_label = ctk.CTkLabel(edit_frame,
                                      text=f'Descuento 2',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        porcentaje_2_label.grid(row = 7, column = 3, columnspan = 2, sticky = 'w')
        # PORCENTAJE 3
        porcentaje_3_label = ctk.CTkLabel(edit_frame,
                                      text=f'Descuento 3',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        porcentaje_3_label.grid(row = 8, column = 3, columnspan = 2, sticky = 'w')
        # FLETE
        flete_label = ctk.CTkLabel(edit_frame,
                                      text=f'Descuento %',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        flete_label.grid(row = 9, column = 3, columnspan = 2, sticky = 'w')
        # IVA
        iva_label = ctk.CTkLabel(edit_frame,
                                      text=f'I.V.A. %',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        iva_label.grid(row = 10, column = 3, columnspan = 2, sticky = 'w')
    # BOTONES
        # EDITAR
        editar_btn = ctk.CTkButton(edit_frame,
                                   text='Editar',
                                   command=self.ModEntradaMode,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        editar_btn.grid(row=4,column=5,columnspan=2,sticky='we',padx=10)
        # ELIMINAR
        eliminar_btn = ctk.CTkButton(edit_frame,
                                   text='Eliminar',
                                   command=self.EliminarEntrada,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        eliminar_btn.grid(row=5,column=5,columnspan=2,sticky='we',padx=10)
        # CANCELAR
        cancelar_btn = ctk.CTkButton(edit_frame,
                                     text='Cancelar',
                                     command=lambda: self.edit_window.destroy(),
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        cancelar_btn.grid(row=6,column=5,columnspan=2,sticky='we',padx=10)
        # ACEPTAR
        aceptar_btn = ctk.CTkButton(edit_frame,
                                    text='Aceptar',
                                    command=self.ModEntrada,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        aceptar_btn.grid(row=8,column=5,columnspan=2,sticky='we',padx=10)
# MODO MODIFICAR ENTRADA
    def ModEntradaMode(self):
        self.cantidad_edit_entry.configure(state='normal')
        self.costo_edit_entry.configure(state='normal')
        self.porcentaje_1_edit_entry.configure(state='normal')
        self.porcentaje_2_edit_entry.configure(state='normal')
        self.porcentaje_3_edit_entry.configure(state='normal')
        self.flete_edit_entry.configure(state='normal')
        self.iva_edit_entry.configure(state='normal')
        self.cantidad_edit_entry.focus()
# MODIFICAR ENTRADA
    def ModEntrada(self):
        item_id = self.item_id
        nombre = self.nombre
        cantidad = costo = porcentaje = iva = None
        try:
            cantidad = int(self.cantidad_edit_var.get())
            costo = float(self.costo_edit_var.get())
            descuento_1 = float(self.porcentaje_1_edit_var.get())
            descuento_2 = float(self.porcentaje_2_edit_var.get())
            descuento_3 = float(self.porcentaje_3_edit_var.get())
            flete = float(self.flete_edit_var.get())
            iva = float(self.iva_edit_entry.get())
        except ValueError:
            if not cantidad:
                messagebox.showerror('¡Atención!','Verifique la cantidad del producto.')
                self.cantidad_edit_entry.focus()
                return
        if cantidad <= 0:
            messagebox.showerror('Error', 'Agregue la cantidad del producto.')
            self.cantidad_entry.focus()
            return
        if costo <= 0:
            messagebox.showerror('Error', 'Agregue el costo del producto.')
            self.costo_entry.focus()
            return

        def aplicar_descuentos(valor, *descuentos):
            for d in descuentos:
                valor -= valor * (d / 100)
            return round(valor, 2)

        neto = aplicar_descuentos(costo, descuento_1, descuento_2, descuento_3)

        if flete > 0:
            neto = round(neto * (1 + flete / 100), 2)

        if iva > 0:
            neto_iva = round(neto * (1 + iva / 100), 2)
            iva_dif = round(neto_iva - neto, 2)
        else:
            neto_iva = neto
            iva_dif = 0

        subtotal = round(cantidad * (neto_iva or neto), 2)
        if item_id:
            self.treeview_entradas.item(item_id,
                                         values=(nombre,
                                             cantidad,
                                             ('$',costo),
                                             (descuento_1,'%'),
                                             (descuento_2,'%'),
                                             (descuento_2,'%'),
                                             (flete,'%'),
                                             ('$',neto),
                                             (f'${iva_dif} - {iva}%'),
                                             ('$',neto_iva),
                                             ('$',subtotal)))
        messagebox.showinfo('Editar entrada','Producto editado correctamente.')
        self.edit_window.destroy()
        self.after(100,lambda: self.TotalPrev())
# ELIMINAR ENTRADA
    def EliminarEntrada(self):
        item_id = self.item_id
        if not item_id:
            messagebox.showerror("Error", "Debe seleccionar un producto para eliminarlo.")
            return
        answer = messagebox.askyesno("Eliminar producto",f"¿Está seguro que desea eliminar el producto '{self.nombre}' de la lista?")
        if answer:
            if self.codigo in self.lista_productos:
                self.lista_productos.remove(self.codigo)
            else:
                print('No existe el codigo')
            self.treeview_entradas.delete(item_id)
            self.TotalPrev()
            messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")
            self.edit_window.destroy()
        else:
            messagebox.showerror("Error", "Debe seleccionar un producto para eliminarlo.")
# CALCULAR TOTAL
    def TotalPrev(self):
        self.total_prev = 0
        
        for item in self.treeview_entradas.get_children():
            info = self.treeview_entradas.item(item)
            subtotal = float(info['values'][10].split(' ')[1].strip())
            self.total_prev += subtotal
    
        self.total_entry_var.set(f'${format(self.total_prev,'.2f')}')

# BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - 
# BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - 
# BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - 
# BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - BUSQUEDA DE PROVEEDORES - 
    def AyudaProveedores(self):
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        self.treeview_active = True
    # FRAME DEL TREEVIEW
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('600x450')
        self.tree_frame.title('Busqueda de proveedores')
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
        self.search_bar.bind("<Return>",lambda event: self.BuscarProvNombre())
    # BOTONES TREEVIEW     
    # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=self.ListProv,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=0,column=1,sticky='w',padx=5)
    
    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Nombre'))
        self.treeview.grid(row=1,column=0,sticky='nswe',padx=10,pady=10,rowspan=2,columnspan=3)
        # EVENTO DE SELECCIONAR PRODUCTO
        self.treeview.bind("<<TreeviewSelect>>",self.ClickTreeviewProvs)
    # CODIGO
        self.treeview.heading('#0',text='Codigo')
        self.treeview.column('#0',width=50,anchor='center')
    # NOMBRE
        self.treeview.heading('Nombre',text='Nombre')
        self.treeview.column('Nombre',width=150,anchor='center')
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
        self.ListProv()
    # SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeviewProvs(self,event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        self.search_bar_var.set(info['text'])
        if PROV_MANAGER.CheckProv(info['text']):
            self.proveedor_var.set(f'{info['text']} - {info['values'][0]}')
        self.tree_frame.destroy()
    def ListProv(self):
        proveedores = PROV_MANAGER.GetProvs()
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        for i,prov in enumerate(proveedores):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
            self.treeview.insert("",'end',
                                 text=proveedores[prov]['codigo'],
                                 values=(proveedores[prov]['nombre']),
                                 tags=(tag,))
        self.treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.treeview.tag_configure('Even.Treeview', background="#eaeaea")
    def BuscarProvNombre(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        busqueda = self.search_bar_var.get().lower()
        resultados = PROV_MANAGER.SearchProvByName(busqueda)
        for proveedor in resultados:
            self.treeview.insert("", 'end',
                                 text=proveedor['codigo'],
                                 values=(proveedor['nombre']))
    def BuscarProvCodigo(self):
        prov = self.proveedor_var.get()
        if not prov:
            return
        if PROV_MANAGER.CheckProv(prov):
            prov = PROV_MANAGER.GetProv(prov)
            self.proveedor_var.set(f'{prov['codigo']} - {prov['nombre']}')
            self.AbrirCalendario()
# VALIDAR LA ENTRADA DE DIGITOS
    def ValidarDigitos(self,texto):
        texto = texto.replace(".", "", 1)
        if texto == '':
            return True
        return texto.isdigit()
    
# GUARDAR LA FACTURA
    def GuardarFactura(self):
        # — Helpers internos para parsear valores —
        def parse_currency(val):
            # Val puede ser tuple ('$', num) o str '$123.45' ó ''.
            if isinstance(val, tuple):
                num = val[1]
            else:
                num = val.replace('$','').strip()
            if num == '' or num is None:
                raise ValueError("Valor monetario vacío")
            return float(num)

        def parse_percent(val):
            # Val puede ser tuple (pct, '%') o str '5%' ó ''.
            if isinstance(val, tuple):
                num = val[0]
            else:
                num = val.replace('%','').strip()
            if num == '' or num is None:
                return 0.0
            return float(num)

        # 1) Cabecera
        num_fact = self.num_pedido_var.get().strip()
        if not num_fact:
            messagebox.showerror('Error','Agregue un número de factura.')
            self.num_pedido_entry.focus(); return

        try:
            prov_code = int(self.proveedor_var.get().split(' - ')[0])
        except:
            messagebox.showerror('Error','Proveedor inválido.')
            self.proveedor_entry.focus(); return

        fecha = self.fecha_entry_var.get().strip()
        if not fecha:
            messagebox.showerror('Error','Seleccione una fecha.'); return

        try:
            total = float(self.total_entry_var.get().lstrip('$').strip())
        except:
            messagebox.showerror('Error','Total inválido.'); return

        # 2) Detalle
        detalle = []
        for iid in self.treeview_entradas.get_children():
            info     = self.treeview_entradas.item(iid)
            codigo   = info['text']
            vals     = info['values']

            try:
                cantidad  = int(vals[1])
                costo     = parse_currency(vals[2])
                desc1     = parse_percent(vals[3])
                desc2     = parse_percent(vals[4])
                desc3     = parse_percent(vals[5])
                flete     = parse_percent(vals[6])
                neto      = parse_currency(vals[7])
                # vals[8] = '$X.YY - Z%' -> solo necesitamos Z%
                iva_pct   = float(vals[8].split('-')[1].replace('%','').strip())
                neto_iva  = parse_currency(vals[9])
                subtotal  = parse_currency(vals[10])
            except Exception as e:
                messagebox.showerror(
                  'Error en línea',
                  f"Producto {codigo}: {e}"
                )
                return

            detalle.append({
                'codigo':     codigo,
                'cantidad':   cantidad,
                'costo':      costo,
                'descuento1': desc1,
                'descuento2': desc2,
                'descuento3': desc3,
                'flete':      flete,
                'iva':        iva_pct,
                'neto':       neto,
                'neto_iva':   neto_iva,
                'subtotal':   subtotal
            })

        if not detalle:
            messagebox.showerror('Error','No hay productos que guardar.'); return

        # 3) Llamada a BD
        try:
            INVENTARIO.GuardarEntradaInventario(
                num_factura=num_fact,
                proveedor=prov_code,
                fecha=fecha,
                total=total,
                detalle_entrada=detalle
            )
            self.GoBack_CB()
        except Exception as e:
            messagebox.showerror('Error al guardar',''+str(e))


    # — Helper para bloquear/desbloquear UI —
    def _set_editable(self, flag: bool):
        state = 'normal' if flag else 'disabled'
        # campos cabecera
        self.num_pedido_entry.configure(state=state)
        self.proveedor_entry.configure(state=state)
        self.btn_calendario.configure(state=state)
        # botones
        self.btn_agregar_entrada.configure(state=state)
        self.btn_guardar_entrada.configure(state=state)
        # Treeview principal: impedir selección
        self.treeview_entradas.configure(selectmode='browse' if flag else 'none')

    # — Lógica para mostrar una entrada existente —
    def ObtenerEntrada(self, event=None):
        num_fact = self.num_pedido_var.get().strip()
        if not num_fact:
            return
        data = INVENTARIO.ObtenerEntrada(num_fact)
        if not data:
            self.proveedor_entry.focus()
            return

        # 1) Bloquear UI
        self._set_editable(False)

        # 2) Rellenar cabecera
        prov_txt = f"{data['proveedor']} - {data['nombre_proveedor']}"
        self.proveedor_var.set(prov_txt)
        # fecha viene como date; formateamos a dd/mm/yyyy
        self.fecha_entry_var.set(data['fecha'].strftime('%d/%m/%Y'))
        self.total_entry_var.set(f"${data['total']:.2f}")

        # 3) Limpiar y rellenar detalle
        for iid in self.treeview_entradas.get_children():
            self.treeview_entradas.delete(iid)

        for item in data['detalle']:
            iva_diff = item['neto_iva'] - item['neto']
            self.treeview_entradas.insert(
                "", "end",
                text=item['codigo'],
                values=(
                  item['nombre'],
                  item['cantidad'],
                  ('$', item['costo']),
                  (item['descuento1'], '%'),
                  (item['descuento2'], '%'),
                  (item['descuento3'], '%'),
                  (item['flete'], '%'),
                  ('$', item['neto']),
                  (f"${iva_diff:.2f} - {item['iva']}%"),
                  ('$', item['neto_iva']),
                  ('$', item['subtotal'])
                )
            )

        # 4) Añadir botón Cancelar (solo visualización)
        self.cancel_btn = ctk.CTkButton(
            self.prog_frame,
            text="Cancelar",
            fg_color=APP_COLORS[9],
            hover_color=APP_COLORS[10],
            command=self.CancelarVisualizacion)
        self.cancel_btn.grid(row=0, column=1, sticky='nw', padx=5, pady=5)
        # Ubica el botón donde mejor encaje (por ejemplo junto a 'Volver atrás'):
        # IMPRIMIR FACT
        self.print_btn = ctk.CTkButton(self.prog_frame,
                                       text="Imprimir factura",
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3],
                                       command=self.ImprimirFactura)
        self.print_btn.grid(row=0, column=2, sticky='nw', padx=5, pady=5)

    # — Vuelve la UI a su estado original —
    def CancelarVisualizacion(self):
        # destruye el botón
        if hasattr(self, 'cancel_btn'):
            self.cancel_btn.destroy()

        # Limpiar campos
        self.num_pedido_var.set('')
        self.proveedor_var.set('')
        self.fecha_entry_var.set('')
        self.total_entry_var.set(f"${0:.2f}")

        # Limpiar detalle
        for iid in self.treeview_entradas.get_children():
            self.treeview_entradas.delete(iid)

        # Rehabilitar edición
        self._set_editable(True)
        # devolver foco al número de factura
        self.num_pedido_entry.focus()

    def ImprimirFactura(self):
        """ Recopila TODOS los campos de self.treeview_entradas,
            genera un PDF y lo envía a impresión."""
        # — Helpers internos —
        def parse_currency_val(val):
            # Val puede ser tuple ('$', número) o string '$123.45' / '123.45'
            if isinstance(val, tuple):
                num = val[1]
            else:
                num = str(val).replace('$', '').strip()
            try:
                return float(num)
            except:
                raise ValueError(f"Formato monetario inválido: {val}")

        def parse_percent_val(val):
            # Val puede ser tuple (pct, '%') o string '5%' / '5'
            if isinstance(val, tuple):
                num = val[0]
            else:
                num = str(val).replace('%','').strip()
            try:
                return float(num)
            except:
                raise ValueError(f"Formato porcentaje inválido: {val}")

        # 1) Leer cabecera
        num_fact  = self.num_pedido_var.get().strip()
        prov_txt  = self.proveedor_var.get()
        fecha_txt = self.fecha_entry_var.get()
        total_txt = self.total_entry_var.get().lstrip('$').strip()

        # 2) Leer detalle completo del Treeview
        detalle = []
        for iid in self.treeview_entradas.get_children():
            info   = self.treeview_entradas.item(iid)
            code   = info['text']
            vals   = info['values']
            desc   = vals[0]
            qty    = int(vals[1])
            costo  = parse_currency_val(vals[2])
            d1     = parse_percent_val(vals[3])
            d2     = parse_percent_val(vals[4])
            d3     = parse_percent_val(vals[5])
            flete  = parse_percent_val(vals[6])
            neto   = parse_currency_val(vals[7])
            # vals[8] = '$X.YY - Z%'  -> extraemos Z%
            iva_pct = float(str(vals[8]).split('-')[1].replace('%','').strip())
            neto_iva = parse_currency_val(vals[9])
            subtotal = parse_currency_val(vals[10])

            detalle.append([
                code,               # Código
                desc,               # Descripción
                qty,                # Cantidad
                f"${costo:.2f}",    # Costo U.
                f"{d1:.2f}%",       # Dto 1
                f"{d2:.2f}%",       # Dto 2
                f"{d3:.2f}%",       # Dto 3
                f"{flete:.2f}%",    # Flete
                f"${neto:.2f}",     # Neto
                f"{iva_pct:.2f}%",  # IVA %
                f"${neto_iva:.2f}", # Neto+IVA
                f"${subtotal:.2f}"  # Subtotal
            ])

        # 3) Generar PDF en carpeta temporal
        tmpdir   = tempfile.gettempdir()
        pdf_path = os.path.join(tmpdir, f"factura_{num_fact}.pdf")
        self.GenerarPDF(
            pdf_path,
            header=[
                ("Factura Nº:", num_fact),
                ("Proveedor:", prov_txt),
                ("Fecha:", fecha_txt),
                ("Total:", f"${float(total_txt):.2f}")
            ],
            detalle=detalle
        )

        # 4) Enviar a imprimir (Win32) o abrir si falla
        try:
            win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)
        except Exception:
            os.startfile(pdf_path)
            messagebox.showwarning(
                "Impresión",
                ("No se pudo imprimir automáticamente.\n"
                 f"PDF guardado en:\n{pdf_path}\n"
                 "Por favor imprime manualmente.")
            )
        else:
            messagebox.showinfo(
                "Impresión",
                f"Factura enviada a imprimir.\nPDF guardado en:\n{pdf_path}"
            )


    def GenerarPDF(self, path: str, header: list, detalle: list):
        """
        Crea un PDF (landscape) con encabezado y tabla de detalle
        que incluya todas las columnas y quepa en la hoja.
        """
        # — Configuración del documento en horizontal —
        doc = SimpleDocTemplate(
            path,
            pagesize=landscape(LETTER),
            leftMargin=20, rightMargin=20,
            topMargin=30, bottomMargin=18
        )
        styles = getSampleStyleSheet()
        story = []

        # Título
        story.append(Paragraph("Factura de Inventario", styles['Title']))
        story.append(Spacer(1, 12))

        # Cabecera
        for label, val in header:
            story.append(Paragraph(f"<b>{label}</b> {val}", styles['Normal']))
        story.append(Spacer(1, 12))

        # Definimos ratios para 12 columnas que sumen 1.0
        ratios = [
            0.06,  # Código
            0.21,  # Descripción
            0.05,  # Cant.
            0.06,  # Costo U.
            0.05,  # Dto 1
            0.05,  # Dto 2
            0.05,  # Dto 3
            0.05,  # Flete
            0.06,  # Neto
            0.05,  # IVA %
            0.06,  # Neto+IVA
            0.10,  # Subtotal
        ]
        # Ancho utilizable
        usable_width = doc.width
        colWidths = [usable_width * r for r in ratios]

        # Encabezados de columna
        cols = [
            "Código", "Descripción", "Cant.", "Costo U.",
            "Dto 1", "Dto 2", "Dto 3", "Flete",
            "Neto", "IVA %", "Neto+IVA", "Subtotal"
        ]
        data = [cols] + detalle

        # Estilo de párrafo para envolver texto largo en la columna Descripción
        wrap_style = ParagraphStyle(
            name='wrap',
            parent=styles['BodyText'],
            fontSize=7,
            leading=8
        )

        # Convertimos la celda de Descripción a Paragraph para que se envuelva
        for row_i in range(1, len(data)):
            desc = data[row_i][1]
            data[row_i][1] = Paragraph(desc, wrap_style)

        # Creamos tabla
        table = Table(data, colWidths=colWidths, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#666666")),
            ('TEXTCOLOR',  (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN',       (2, 1), (-1, -1), 'CENTER'),
            ('VALIGN',      (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID',        (0, 0), (-1, -1), 0.4, colors.black),
            ('FONTNAME',    (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE',    (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0,0), (-1,0), 6),
            ('LEFTPADDING',   (0,0), (-1,-1), 3),
            ('RIGHTPADDING',  (0,0), (-1,-1), 3),
        ]))

        story.append(table)
        doc.build(story)
