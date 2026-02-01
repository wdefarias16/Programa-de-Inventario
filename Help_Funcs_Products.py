# DATA
from DatabaseManager import *
from style import *
# GUI
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

# -----------------------------------------------------------------
# PRODUCT HELP WINDOW - PRODUCT HELP WINDOW - PRODUCT HELP WINDOW - 
# -----------------------------------------------------------------
def Products_Help_Window(self):
    self.PRODUCTO = {}
    # ----------------------------------------------------------------
    # LISTA TOD0 EL INVENTARIO EN EL TREEVIEW DE PRODUCTOS
    # ----------------------------------------------------------------
    def ListInventory():
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
    # ----------------------------------------------------------------
    # LISTA PRODUCTOS INACTIVOS - LISTA PRODUCTOS INACTIVOS - 
    # ----------------------------------------------------------------
    def ListInactives():
        self.search_bar_var.set('')
        inventario = INVENTARIO.GetInactives()
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
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeview(event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        product_id = info['text']
        self.PRODUCTO = INVENTARIO.GetProducto(product_id)
        # OBTENER LINEA - GRUPO - PROVEEDOR
        # LINEA
        line_id = self.PRODUCTO['linea']
        linea = LINE_MANAGER.GetLine(line_id)
        # GRUPO
        grupo_id = self.PRODUCTO['grupo']
        grupo = LINE_MANAGER.GetGroup(line_id,grupo_id)
        # PROVEEDOR
        proveedor_id = self.PRODUCTO['proveedor']
        proveedor = PROV_MANAGER.GetProv(proveedor_id)
        # AGREGAR LOS DATOS AL PRODUCTO
        self.PRODUCTO['linea'] = f'{linea['codigo']} - {linea['nombre']}'
        self.PRODUCTO['grupo'] = f'{grupo['codigo']} - {grupo['nombre']}'
        self.PRODUCTO['proveedor'] = f'{proveedor['codigo']} - {proveedor['nombre']}'
        # CERRAR LA VENTANA
        help_frame.destroy()
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # FRAME DEL TREEVIEW
    help_frame = ctk.CTkToplevel(self,
                               fg_color=APP_COLOR['white_m'])
    help_frame.geometry('900x450')
    help_frame.title('Busqueda de productos')
    help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
    help_frame.transient(self)
    # TITLE FRAME
    title_frame = ctk.CTkFrame(help_frame,
                    fg_color=APP_COLOR['sec'],
                    height=50,
                    corner_radius=0)
    title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.10,anchor='n')
    # TITLE LABEL - TITLE LABEL - TITLE LABEL
    title_label = ctk.CTkLabel(title_frame,
                    text='Búsqueda de productos',
                    bg_color='transparent',
                    text_color=APP_COLOR['white_m'],
                    font=FONT['text'])
    title_label.pack(expand=True,fill='x',pady=5)
    # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
    prog_frame = ctk.CTkFrame(help_frame,
                    fg_color=APP_COLOR['white_m'],
                    height=50,
                    corner_radius=0)
    prog_frame.place(relx=0.5,rely=0.10,relwidth=1,relheight=0.90,anchor='n')
    # BARRA DE BUSQUEDA
    # LABEL
    label_sb = ctk.CTkLabel(prog_frame,
                         text='Busqueda por nombre',
                         bg_color='transparent',
                         text_color=APP_COLOR['gray'],
                         font=FONT['text_light'])
    label_sb.place(relx=0.05,rely=0.08,anchor='nw')
    # ENTRY
    self.search_bar_var = tk.StringVar()
    self.search_bar = ctk.CTkEntry(prog_frame,
                              width=200,
                              textvariable=self.search_bar_var)
    self.search_bar.place(relx=0.05,rely=0.18,anchor='w')
    self.search_bar.bind("<Return>",lambda event:self.BuscarProductoNombre())
    self.search_bar.bind("<Control-BackSpace>", lambda event: ListInventory())
    self.search_bar.after(100,lambda:self.search_bar.focus())
    # BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - 
    # LIST
    list_btn = ctk.CTkButton(prog_frame,
                                text='',
                                width=30,
                                height=10,
                                image=ICONS['refresh'],
                                command=ListInventory,
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'])
    list_btn.place(relx=0.30,rely=0.18,anchor='w')
    # LIST INACTIVE
    list_inactive_btn = ctk.CTkButton(prog_frame,
                                text='',
                                width=30,
                                height=10,
                                image=ICONS['cancel'],
                                command=ListInactives,
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'])
    list_inactive_btn.place(relx=0.36,rely=0.18,anchor='w')
    # CERRAR
    def CloseHelp():
        help_frame.destroy()
    cerrar_btn = ctk.CTkButton(prog_frame,
                                text='',
                                width=30,
                                image=ICONS['cancel'],
                                command=CloseHelp,
                                fg_color=APP_COLOR['red_m'],
                                hover_color=APP_COLOR['red_s'])
    cerrar_btn.place(relx=0.95,rely=0.05,anchor='ne')
    # TREEVIEW
    self.treeview = ttk.Treeview(prog_frame,
                            style='Custom.Treeview',
                            columns=('Linea','Grupo','Proveedor','Nombre','Costo'))
    self.treeview.place(relx=0.5,rely=0.3,relwidth=0.90,relheight=0.60,anchor='n')
    # EVENTO DE SELECCIONAR PRODUCTO
    self.treeview.bind("<<TreeviewSelect>>",ClickTreeview)
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
        background = APP_COLOR['white_m'],
        foreground = APP_COLOR['black_m'],
        rowheight = 30,
        font = FONT['text_small'],
        fieldbackground = APP_COLOR['white_m'])
    style.configure(
        'Custom.Treeview.Heading',
        background = APP_COLOR['black_m'],
        foreground = APP_COLOR['black_m'],
        font = FONT['text_light'])
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(prog_frame,
                                 orientation='vertical',
                                 command=self.treeview.yview)
    #scrollbar.grid(row=3,column=15,sticky='wns',pady=5,rowspan=7)
    self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
    ListInventory()
    help_frame.wait_window()
    return self.PRODUCTO