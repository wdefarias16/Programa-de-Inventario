import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from DatabaseManager import INVENTARIO, PROV_MANAGER
from style import*

# PROGRAMA DE CARGA DE PRODUCTOS
class EntradasInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.validardigit = self.register(self.ValidarDigitos)
        self.lista_productos = []
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
        # PROVEEDOR
        self.proveedor_var = tk.StringVar()
        self.proveedor_entry = ctk.CTkEntry(self.prog_frame,
                                            state='disabled',
                                            textvariable=self.proveedor_var,
                                            fg_color=APP_COLORS[6],
                                            border_color=APP_COLORS[2])
        self.proveedor_entry.grid(row=4,column=3,columnspan=2,padx=5,sticky='we')
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
        self.total_entry = ctk.CTkEntry(self.prog_frame,
                                        state='disabled',
                                        textvariable=self.total_entry_var,
                                        fg_color=APP_COLORS[8],
                                        border_color=APP_COLORS[8])
        self.total_entry.grid(row=1,column=10,columnspan=1,padx=5,sticky='we')
        # IVA
        self.iva = ctk.CTkCheckBox(self.prog_frame,
                                   text='I.V.A. 16%',
                                   font=FONTS[1],
                                   text_color=APP_COLORS[4],
                                   hover_color=APP_COLORS[2],
                                   fg_color=APP_COLORS[2],
                                   border_color=APP_COLORS[4],
                                   border_width=2)
        self.iva.grid(row=4,column=6,columnspan=2,padx=5,sticky='e')
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
                                     columns=('Nombre','Cantidad','Costo','Descuento','Neto','SubTotal'))
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
# CLICK PROVEEDORES
    def SelectProvMenu(self,opcion):
        self.proveedor_var.set(opcion)
# CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - CALENDARIO - 
    def abrir_calendario(self):
        top = tk.Toplevel(self.prog_frame)
        top.title('Seleccionar Fecha')
        top.grab_set()
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
    def IVA(self):
        pass
# BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
# BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - BUSCAR PRODUCTO - 
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
        # CANTIDAD
        self.cantidad_var = tk.StringVar()
        self.cantidad_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validardigit,'%P'),
                                     textvariable = self.cantidad_var,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.cantidad_entry.grid(row=5,column=0,columnspan=2,sticky='w',padx=20)
        self.cantidad_entry.bind("<Return>",lambda event:self.costo_entry.focus_set())
        # COSTO
        self.costo_var = tk.StringVar()
        self.costo_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validardigit,'%P'),
                                     textvariable = self.costo_var,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.costo_entry.grid(row=7,column=0,columnspan=2,sticky='w',padx=20)
        self.costo_entry.bind("<Return>",lambda event:self.descuento_entry.focus_set())
        # DESCUENTO
        self.descuento_var = tk.StringVar()
        self.descuento_entry = ctk.CTkEntry(self.tree_frame,
                                            state='disabled',
                                            validate = 'key',
                                            validatecommand = (self.validardigit,'%P'),
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4],
                                            textvariable = self.descuento_var)
        self.descuento_entry.grid(row=9,column=0,columnspan=2,sticky='w',padx=20)
        self.descuento_entry.bind("<Return>",lambda event:self.AgregarProducto())
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
        label_cantidad.grid(row=4,column=0,columnspan=3,sticky='w',padx=20)
        # COSTO
        label_costo = ctk.CTkLabel(self.tree_frame,
                                      text='Costo',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_costo.grid(row=6,column=0,columnspan=3,sticky='w',padx=20)
        # DESCUENTO
        label_descuento = ctk.CTkLabel(self.tree_frame,
                                       text='Descuento',
                                       font=FONTS[1],
                                       text_color=APP_COLORS[4])
        label_descuento.grid(row=8,column=0,columnspan=3,sticky='w',padx=20)
    # BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - 
        # CANCELAR
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=self.ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=14,column=0,columnspan=2,sticky='w',padx=10)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
        self.treeview.grid(row=2,column=2,sticky='nswe',padx=10,rowspan=13,columnspan=13)
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
        scrollbar.grid(row=2,column=15,sticky='nsw',pady=5,rowspan=13)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListInventory()
# AGREGAR PRODUCTO A LA LISTA
    def AgregarProducto(self):
        inventario = INVENTARIO.GetCodigos()
        codigo = self.search_bar_var.get()
        cantidad = int(self.cantidad_var.get())
        costo = float(self.costo_var.get())
        descuento = int(self.descuento_var.get())
        neto = round(costo - (costo * (descuento / 100)),2)
        subtotal = round((cantidad * neto),2)
        if cantidad <= 0:
            messagebox.showerror('Error','Debe agregar la cantidad del producto')
        else:
            if codigo not in self.lista_productos:
                if codigo in inventario:
                    producto = INVENTARIO.GetProducto(codigo)
                    self.treeview_entradas.insert("",'end',
                                         text=producto['codigo'],
                                         values=(producto['nombre'],
                                                 cantidad,
                                                 ('$',costo),
                                                 (descuento,'%'),
                                                 ('$',neto),
                                                 ('$',subtotal)))
                    self.btn_agregar_entrada.configure(state='enabled')
                    self.lista_productos.append(str(codigo).strip())
                    self.tree_frame.destroy()
                    self.TotalFactura()
                else:
                    messagebox.showerror('Error',f'Producto con codigo {codigo} no se encuentra en la base de datos.')
            else:
                messagebox.showerror('Error',f'Producto con codigo {codigo} ya se encuentra en la lista.')
# LISTAR INVENTARIO DE LA BUSQUEDA DE PRODDUCTOS
    def ListInventory(self):
        self.search_bar_var.set('')
        self.cantidad_var.set('')
        self.costo_var.set('')
        self.descuento_var.set('')
        self.search_bar.after(100,
            lambda:  self.search_bar.configure(state='normal',
                                               fg_color=APP_COLORS[6],border_color=APP_COLORS[6]))
        self.search_bar.after(100,self.search_bar.focus())
        self.costo_entry.after(100,
            lambda: self.costo_entry.configure(state='disabled',
                                               fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.cantidad_entry.after(100,
            lambda: self.cantidad_entry.configure(state='disabled',
                                                  fg_color=APP_COLORS[4],border_color=APP_COLORS[4]))
        self.descuento_entry.after(100,
            lambda: self.descuento_entry.configure(state='disabled',
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
                                         producto['costo']))
# MUESTRA EN PANTALLA EL TOTAL DE LA FACTURA
    def TotalFactura(self):
        total = 0
        for item in self.treeview_entradas.get_children():
            info = self.treeview_entradas.item(item)
            print(info)
            subtotal = float(info['values'][5].split(' ')[1].strip())
            total += subtotal
        self.total_entry_var.set(f'${total}')
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
        self.search_bar_var.set(codigo)
        self.search_bar.configure(state='disabled',fg_color=APP_COLORS[4],
                                  border_color=APP_COLORS[4])
        self.costo_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                   border_color=APP_COLORS[6])
        self.cantidad_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                      border_color=APP_COLORS[6])
        self.descuento_entry.configure(state='normal',fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
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
        porcentaje = int(datos[3].split(' ')[0])
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
        self.costo_edit_entry.bind("<Return>",lambda event:self.porcentaje_edit_entry.focus_set())
        # PORCENTAJE
        self.porcentaje_edit_var = tk.StringVar()
        self.porcentaje_edit_var.set(porcentaje)
        self.porcentaje_edit_entry = ctk.CTkEntry(edit_frame,
                                                  state='disabled',
                                                  textvariable=self.porcentaje_edit_var,
                                                  validate = 'key',
                                                  validatecommand = (self.validardigit,'%P'),
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
                                      text=f'Costo $',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        costo_label.grid(row = 5, column = 3, columnspan = 2, sticky = 'w')
        # PORCENTAJE
        porcentaje_label = ctk.CTkLabel(edit_frame,
                                      text=f'Descuento %',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        porcentaje_label.grid(row = 6, column = 3, columnspan = 2, sticky = 'w')
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
        aceptar_btn.grid(row=8,column=1,columnspan=2,sticky='we',padx=10)
# MODO MODIFICAR ENTRADA
    def ModEntradaMode(self):
        self.cantidad_edit_entry.configure(state='normal')
        self.costo_edit_entry.configure(state='normal')
        self.porcentaje_edit_entry.configure(state='normal')
        self.cantidad_edit_entry.focus()
# MODIFICAR ENTRADA
    def ModEntrada(self):
        item_id = self.item_id
        nombre = self.nombre
        cantidad = int(self.cantidad_edit_var.get())
        costo = float(self.costo_edit_var.get())
        porcentaje = int(self.porcentaje_edit_var.get())
        neto = round(costo - (costo * (porcentaje / 100)),2)
        subtotal = round((cantidad * neto),2)

        if not cantidad or cantidad <= 0:
            messagebox.showerror('Error de carga','Debe agregar cantidad del producto.')
        elif not costo or costo <= 0:
            messagebox.showerror('Error de carga','Debe agregar costo del producto.')
        else:
            if not porcentaje:
                porcentaje = 0
            if item_id:
                self.treeview_entradas.item(item_id,
                                            values = (nombre,
                                                      cantidad,
                                                      ('$',costo),
                                                      (porcentaje,'%'),
                                                      ('$',neto),
                                                      ('$',subtotal)))
                messagebox.showinfo('Editar entrada','Producto editado correctamente.')
                self.edit_window.destroy()
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
                print(self.lista_productos)
            else:
                print('No existe el codigo')
            self.treeview_entradas.delete(item_id)
            messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")
            self.edit_window.destroy()
        else:
            messagebox.showerror("Error", "Debe seleccionar un producto para eliminarlo.")
# VALIDAR LA ENTRADA DE DIGITOS
    def ValidarDigitos(self,texto):
        texto = texto.replace(".", "", 1)
        if texto == '':
            return True
        return texto.isdigit()