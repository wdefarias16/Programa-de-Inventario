import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk, messagebox
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
        self.btn_agregar_entrada = ctk.CTkButton(self.prog_frame,
                                            text="Agregar producto",
                                            width=25,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.BusquedaProducto)
        self.btn_agregar_entrada.grid(row=4,column=9,columnspan=2,sticky='we',padx=5)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW
        self.treeview_entradas = ttk.Treeview(self.prog_frame,
                                     style='Custom.Treeview',
                                     columns=('Nombre','Cantidad','Costo','Descuento','Neto'))
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
        # DESCUENTO
        self.treeview_entradas.heading('Descuento',text='Descuento')
        self.treeview_entradas.column('Descuento',width=50,anchor='center')
        # NETO
        self.treeview_entradas.heading('Neto',text='Neto')
        self.treeview_entradas.column('Neto',width=50,anchor='center')
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
        self.btn_agregar_entrada.configure(state='disabled')
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('800x400')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        self.tree_frame.transient(self)
    # GRID SETUP
        for rows in range(16):
            self.tree_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(16):
            self.tree_frame.columnconfigure(columns,weight=1,uniform='column')     
    # ENTRADAS
        # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                  width=200,
                                  textvariable=self.search_bar_var)
        self.search_bar.grid(row=2,column=0,columnspan=2,sticky='we',padx=10)
        self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
        # CANTIDAD
        self.cantidad_var = tk.IntVar()
        self.cantidad_var.set('')
        self.cantidad_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     fg_color=APP_COLORS[4],
                                     textvariable = self.cantidad_var)
        self.cantidad_entry.grid(row=5,column=0,columnspan=2,sticky='w',padx=10)
        self.cantidad_entry.bind("<Return>",lambda event:self.costo_entry.focus_set())
        # COSTO
        self.costo_var = tk.DoubleVar()
        self.costo_var.set('')
        self.costo_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     fg_color=APP_COLORS[4],
                                     textvariable = self.costo_var)
        self.costo_entry.grid(row=7,column=0,columnspan=2,sticky='w',padx=10)
        self.costo_entry.bind("<Return>",lambda event:self.descuento_entry.focus_set())
        # DESCUENTO
        self.descuento_var = tk.IntVar()
        self.descuento_var.set('')
        self.descuento_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            fg_color=APP_COLORS[4],
                                            textvariable = self.descuento_var)
        self.descuento_entry.grid(row=9,column=0,columnspan=2,sticky='w',padx=10)
        self.descuento_entry.bind("<Return>",lambda event:self.AgregarProducto())
    # LABELS
        # BUSQUEDA
        label_busqueda = ctk.CTkLabel(self.tree_frame,
                             text='Busqueda por nombre',
                             font=FONTS[1],
                                        text_color=APP_COLORS[4])
        label_busqueda.grid(row=1,column=0,columnspan=3,sticky='w',padx=10)
        # CANTIDAD
        label_cantidad = ctk.CTkLabel(self.tree_frame,
                                      text='Cantidad',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_cantidad.grid(row=4,column=0,columnspan=3,sticky='w',padx=10)
        # COSTO
        label_costo = ctk.CTkLabel(self.tree_frame,
                                      text='Costo',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_costo.grid(row=6,column=0,columnspan=3,sticky='w',padx=10)
        # DESCUENTO
        label_descuento = ctk.CTkLabel(self.tree_frame,
                                       text='Descuento',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_descuento.grid(row=8,column=0,columnspan=3,sticky='w',padx=10)
    # BOTONES TREEVIEW     
        # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=14,column=0,columnspan=2,sticky='w',padx=10)
    # TREEVIEW
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=0,column=2,sticky='nswe',padx=10,pady=10,rowspan=16,columnspan=13)
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
        scrollbar.grid(row=0,column=15,sticky='nsw',pady=5,rowspan=16)
        self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()
# LISTAR INVENTARIO DE LA BUSQUEDA DE PRODDUCTOS
    def ListInventory(self):
        self.search_bar_var.set('')
        self.cantidad_var.set('')
        self.search_bar.configure(state='normal',fg_color=APP_COLORS[6])
        self.costo_entry.after(100, lambda: self.costo_entry.configure(state='disabled',fg_color=APP_COLORS[4]))
        self.cantidad_entry.after(100, lambda: self.cantidad_entry.configure(state='disabled',fg_color=APP_COLORS[4]))
        self.descuento_entry.after(100, lambda: self.descuento_entry.configure(state='disabled',fg_color=APP_COLORS[4]))
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
        print(info)
        codigo = info['text']
        self.search_bar_var.set(codigo)
        self.search_bar.configure(state='disabled',fg_color=APP_COLORS[4])
        self.costo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.cantidad_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.descuento_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.cantidad_entry.focus_set()
# SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - SELECCIONAR ENTRADA PARA MODIFICAR - 
    def ClickEntrada(self,event):
        item_id = self.treeview_entradas.selection()
        info = self.treeview_entradas.item(item_id)
        codigo = info['text']
        datos = info['values']
        print(datos)
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
        for rows in range(10):
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
                                      text=f'{datos[0]}',
                                      font=FONTS[4],
                                      text_color=APP_COLORS[4],
                                      bg_color='transparent')
        producto_label.grid(row = 2, column = 1, columnspan = 4, padx = 10, sticky = 'w')
    # ENTRADAS
        # CANTIDAD
        self.cantidad_edit_var = tk.IntVar()
        self.cantidad_edit_var.set(datos[1])
        self.cantidad_edit_entry = ctk.CTkEntry(edit_frame,
                                                state='disabled',
                                                textvariable=self.cantidad_edit_var,
                                                fg_color=APP_COLORS[6],
                                                border_width=0)
        self.cantidad_edit_entry.grid(row = 4, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        # COSTO
        self.costo_edit_var = tk.DoubleVar()
        self.costo_edit_var.set(datos[2])
        self.costo_edit_entry = ctk.CTkEntry(edit_frame,
                                             state='disabled',
                                             textvariable=self.costo_edit_var,
                                             fg_color=APP_COLORS[6],
                                             border_width=0)
        self.costo_edit_entry.grid(row = 5, column = 1, columnspan = 2, padx = 10, sticky = 'we')
        # PORCENTAJE
        self.porcentaje_edit_var = tk.IntVar()
        self.porcentaje_edit_var.set(datos[3])
        self.porcentaje_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.porcentaje_edit_var,
                                                  fg_color=APP_COLORS[6],
                                                  border_width=0)
        self.porcentaje_edit_entry.grid(row = 6, column = 1, columnspan = 2, padx = 10, sticky = 'we')
    # LABELS
        # CANTIDAD
        cantidad_label = ctk.CTkLabel(edit_frame,
                                      text=f'Cantidad',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        cantidad_label.grid(row = 4, column = 3, columnspan = 2, sticky = 'w')
        # COSTO
        costo_label = ctk.CTkLabel(edit_frame,
                                      text=f'Costo',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        costo_label.grid(row = 5, column = 3, columnspan = 2, sticky = 'w')
        # PORCENTAJE
        porcentaje_label = ctk.CTkLabel(edit_frame,
                                      text=f'Porcentaje',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        porcentaje_label.grid(row = 6, column = 3, columnspan = 2, sticky = 'w')
    # BOTONES
        # EDITAR
        editar_btn = ctk.CTkButton(edit_frame,
                                   text='Editar',
                                   command=self.ModEntrada,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        editar_btn.grid(row=4,column=5,columnspan=2,sticky='we',padx=10)
        # CANCELAR
        cancelar_btn = ctk.CTkButton(edit_frame,
                                     text='Cancelar',
                                     command=lambda: self.edit_window.destroy(),
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        cancelar_btn.grid(row=5,column=5,columnspan=2,sticky='we',padx=10)
        # ACEPTAR
        aceptar_btn = ctk.CTkButton(edit_frame,
                                    text='Aceptar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        aceptar_btn.grid(row=8,column=1,columnspan=2,sticky='we',padx=10)
        

# MODIFICAR ENTRADA
    def ModEntrada(self):
        self.cantidad_edit_entry.configure(state='normal')
        self.costo_edit_entry.configure(state='normal')
        self.porcentaje_edit_entry.configure(state='normal')
        self.cantidad_edit_entry.focus()
        # cantidad = self.cantidad_edit_var.get()
        # costo = self. costo_edit_var.get()
# AGREGAR PRODUCTO A LA ENTRADA
    def AgregarProducto(self):
        inventario = INVENTARIO.GetCodigos()
        codigo = self.search_bar_var.get()
        cantidad = self.cantidad_var.get()
        costo = self.costo_var.get()
        descuento = self.descuento_var.get()
        neto = costo - (costo * (descuento / 100))
        if cantidad <= 0:
            messagebox.showerror('Error','Debe agregar la cantidad del producto')
        else:
            if codigo in inventario:
                producto = INVENTARIO.GetProducto(codigo)
                self.treeview_entradas.insert("",'end',
                                     text=producto['codigo'],
                                     values=(producto['nombre'],
                                             cantidad,
                                             f'${costo}',
                                             f'{descuento}%',
                                             f'${neto}'))
                self.btn_agregar_entrada.configure(state='enabled')
                self.tree_frame.destroy()
            else:
                messagebox.showerror('Error',f'Producto con codigo {codigo} no se encuentra en la base de datos.')