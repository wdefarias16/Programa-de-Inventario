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
def Add_Customer_Window(self):
    self.CUSTOMER = {}
    # ----------------------------------------------------------------
    # LISTA TOD0 EL INVENTARIO EN EL TREEVIEW DE PRODUCTOS
    # ----------------------------------------------------------------
    def ListCustomers():
        self.search_bar_var.set('')
        customers = CLIENT_MANAGER.GetAllClients()
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        for i, customer in enumerate(customers.values()):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
            self.treeview.insert("",'end',
                                 text=customer['id_fiscal'],
                                 values=(customer['nombre'],),
                                         tags=(tag,))
        self.treeview.tag_configure('Odd.Treeview', background = '#D2D2D2')
        self.treeview.tag_configure('Even.Treeview', background = '#eaeaea')
    # ----------------------------------------------------------------
    # BUSQUEDA PRODUCTOS POR NOMBRE - BUSQUEDA PRODUCTOS POR NOMBRE -  
    # ----------------------------------------------------------------
    def Search_By_Name():
        consulta = self.search_bar_var.get()
        busqueda = CLIENT_MANAGER.SearchClients(consulta)
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        if not busqueda:
             return
        for i, customer in enumerate(busqueda):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
            self.treeview.insert("",'end',
                                 text=customer['codigo'],
                                 values=(customer['nombre'],),
                                         tags=(tag,))
        self.treeview.tag_configure('Odd.Treeview', background = '#D2D2D2')
        self.treeview.tag_configure('Even.Treeview', background = '#eaeaea')
    # ----------------------------------------------------------------
    # LISTA PRODUCTOS INACTIVOS - LISTA PRODUCTOS INACTIVOS - 
    # ----------------------------------------------------------------
    def ListInactives():
        pass
    #    self.search_bar_var.set('')
    #    inventario = CLIENT_MANAGER.GetInactives()
    #    for item in self.treeview.get_children():
    #            self.treeview.delete(item)
    #    for i, customer in enumerate(inventario.values()):
    #        tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
    #        self.treeview.insert("",'end',
    #                             text=customer['codigo'],
    #                             values=(customer['nombre'],),
    #                             tags=(tag,))
    #    self.treeview.tag_configure('Odd.Treeview', background="#D2D2D2")
    #    self.treeview.tag_configure('Even.Treeview', background="#eaeaea")
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeview(event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        product_id = info['text']
        self.CUSTOMER = CLIENT_MANAGER.GetClientByFiscalId(product_id)
        
        # CERRAR LA VENTANA
        help_frame.destroy()
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
    # FRAME DEL TREEVIEW
    help_frame = ctk.CTkToplevel(self,
                               fg_color=APP_COLOR['white_m'])
    help_frame.geometry('900x450')
    help_frame.title('Agregar Cliente')
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
                    text='Agregar Cliente',
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
                              fg_color=APP_COLOR['light_gray'],
                              border_color=APP_COLOR['light_gray'],
                              textvariable=self.search_bar_var)
    self.search_bar.place(relx=0.05,rely=0.18,anchor='w')
    self.search_bar.bind("<Return>",lambda event: Search_By_Name())
    self.search_bar.bind("<Control-BackSpace>", lambda event: ListCustomers())
    self.search_bar.after(100,lambda:self.search_bar.focus())
    # BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - 
    # LIST
    list_btn = ctk.CTkButton(prog_frame,
                                text='',
                                width=30,
                                height=10,
                                image=ICONS['refresh'],
                                command=ListCustomers,
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
                            columns=('Nombre'))
    self.treeview.place(relx=0.5,rely=0.3,relwidth=0.90,relheight=0.60,anchor='n')
    # EVENTO DE SELECCIONAR PRODUCTO
    self.treeview.bind("<<TreeviewSelect>>",ClickTreeview)
    # CODIGO
    self.treeview.heading('#0',text='Codigo')
    self.treeview.column('#0',width=50,anchor='w')
    # NOMBRE
    self.treeview.heading('Nombre',text='Nombre')
    self.treeview.column('Nombre',width=150,anchor='w')
    # CONFIGURACION VISUAL DEL TV
    style = ttk.Style()
    style.theme_use("alt")
    style.configure(
        'Custom.Treeview',
        background = APP_COLOR['white_m'],
        foreground = APP_COLOR['black_m'],
        rowheight = 45,
        font = FONT['text'],
        fieldbackground = APP_COLOR['white'])
    style.configure(
        'Custom.Treeview.Heading',
        background = APP_COLOR['black_m'],
        foreground = APP_COLOR['white_m'],
        font = FONT['text_light'])
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(prog_frame,
                                 orientation='vertical',
                                 command=self.treeview.yview)
    #scrollbar.grid(row=3,column=15,sticky='wns',pady=5,rowspan=7)
    self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
    ListCustomers()
    help_frame.wait_window()
    return self.CUSTOMER