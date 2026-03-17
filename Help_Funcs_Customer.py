# DATA
from DatabaseManager import *
from style import *
from Help_Functions import ValidateDigit
# GUI
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter as ctk

# -----------------------------------------------------------------
# PRODUCT HELP WINDOW - PRODUCT HELP WINDOW - PRODUCT HELP WINDOW -
# -----------------------------------------------------------------
def Customer_Help_Window(self):
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
# -----------------------------------------------------------------------
# ADD CUSTOMER WINDOW - ADD CUSTOMER WINDOW - ADD CUSTOMER WINDOW - ADD C
# -----------------------------------------------------------------------
def Add_Customer_Window(self):
    # AGREGAR CLIENTE
    def Add_Customer():
        'Get data'
        data_fields = [(self.customer_fiscal_entry_var,'Debe agregar numero de Cédula o RIF.',self.customer_fiscal_entry),
                       (self.customer_name_entry_var,'Debe agregar el nombre del cliente.',self.customer_name_entry)]
        'Verify data'
        for var,message,widget in data_fields:
             if not var.get().strip():
                  messagebox.showerror('¡Atención!',message)
                  widget.focus()
                  return
        'Get phone number'
        phone_number = self.customer_phone_entry_var.get().strip()      
        'Create data dictionary'
        customer_data = {
             'id_fiscal':self.customer_fiscal_entry_var.get().strip(),
             'name':self.customer_name_entry_var.get().strip(),
             'phone':f"{self.customer_phone_combobox.get()} - {phone_number}" if phone_number else '',
             'address1':self.customer_address_entry_var.get().strip(),
             'address2':'',
             'Ciudad':'',
             'mail':self.customer_mail_entry_var.get().strip()}
        CLIENT_MANAGER.AddClient(customer_data)
        self.CUSTOMER = CLIENT_MANAGER.GetClientByFiscalId(customer_data['id_fiscal'])
        help_frame.destroy()
        return
    # -------------------------------------------------------------------
    # VARIABLES - VARIABLES - VARIABLES - VARIABLES - VARIABLES - VARIABL
    # -------------------------------------------------------------------
    self.CUSTOMER = {}
    self.validate_digit = self.register(ValidateDigit)
    # -------------------------------------------------------------------
    # WINDOW - # WINDOW - # WINDOW - # WINDOW - # WINDOW - # WINDOW - # W
    # -------------------------------------------------------------------
    help_frame = ctk.CTkToplevel(self,
                               fg_color=APP_COLOR['white_m'])
    help_frame.geometry('900x450')
    help_frame.title('Agregar Cliente')
    help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
    help_frame.transient(self)
    # -------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TIT
    # -------------------------------------------------------------------
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
    # -------------------------------------------------------------------
    # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
    # -------------------------------------------------------------------
    # FRAME
    prog_frame = ctk.CTkFrame(help_frame,
                    fg_color=APP_COLOR['white_m'],
                    height=50,
                    corner_radius=0)
    prog_frame.place(relx=0.5,rely=0.10,relwidth=1,relheight=0.90,anchor='n')
    # -------------------------------------------------------------------
    # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES
    # -------------------------------------------------------------------
    # FISCAL ID
    self.customer_fiscal_entry_var = ctk.StringVar()
    self.customer_fiscal_entry = ctk.CTkEntry(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                validate = 'key',
                                validatecommand=(self.validate_digit,'%P'),
                                textvariable=self.customer_fiscal_entry_var)
    self.customer_fiscal_entry.place(relx=0.4,rely=0.3,relwidth=0.1,anchor='w')
    self.customer_fiscal_entry.bind('<Return>',lambda event: self.customer_name_entry.focus())
    # NAME
    self.customer_name_entry_var = ctk.StringVar()
    self.customer_name_entry = ctk.CTkEntry(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                textvariable=self.customer_name_entry_var)
    self.customer_name_entry.place(relx=0.4,rely=0.4,relwidth=0.15,anchor='w')
    self.customer_name_entry.bind('<Return>',lambda event: self.customer_phone_entry.focus())
    # PHONE COMBO
    self.customer_phone_combobox = ctk.CTkComboBox(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                state='readonly',
                                values=PHONE_CODES)
    self.customer_phone_combobox.place(relx=0.4,rely=0.5,relwidth=0.1,anchor='w')
    self.customer_phone_combobox.set(PHONE_CODES[0])
    # PHONE
    self.customer_phone_entry_var = ctk.StringVar()
    self.customer_phone_entry = ctk.CTkEntry(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                validate = 'key',
                                validatecommand=(self.validate_digit,'%P'),
                                textvariable=self.customer_phone_entry_var)
    self.customer_phone_entry.place(relx=0.51,rely=0.5,relwidth=0.08,anchor='w')
    self.customer_phone_entry.bind('<Return>',lambda event: self.customer_address_entry.focus())
    # ADDRESS
    self.customer_address_entry_var = ctk.StringVar()
    self.customer_address_entry = ctk.CTkEntry(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                textvariable=self.customer_address_entry_var)
    self.customer_address_entry.place(relx=0.4,rely=0.6,relwidth=0.19,anchor='w')
    self.customer_address_entry.bind('<Return>',lambda event: self.customer_mail_entry.focus())
    # MAIL
    self.customer_mail_entry_var = ctk.StringVar()
    self.customer_mail_entry = ctk.CTkEntry(help_frame,
                                fg_color=APP_COLOR['light_gray'],
                                border_color=APP_COLOR['light_gray'],
                                textvariable=self.customer_mail_entry_var)
    self.customer_mail_entry.place(relx=0.4,rely=0.7,relwidth=0.19,anchor='w')
    self.customer_mail_entry.bind('<Return>',lambda event: Add_Customer())
    # -------------------------------------------------------------------
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABE
    # -------------------------------------------------------------------
    # FISCAL
    customer_fiscal_label = ctk.CTkLabel(help_frame,
                                text = 'Cédula / RIF',
                                font=FONT['text'],
                                text_color=APP_COLOR['gray'])
    customer_fiscal_label.place(relx=0.39,rely=0.3,anchor='e')
    # NAME
    customer_name_label = ctk.CTkLabel(help_frame,
                                text = 'Nombre',
                                font=FONT['text'],
                                text_color=APP_COLOR['gray'])
    customer_name_label.place(relx=0.39,rely=0.4,anchor='e')
    # PHONE
    customer_phone_label = ctk.CTkLabel(help_frame,
                                text = 'Teléfono',
                                font=FONT['text'],
                                text_color=APP_COLOR['gray'])
    customer_phone_label.place(relx=0.39,rely=0.5,anchor='e')
    # ADDRESS
    customer_address_label = ctk.CTkLabel(help_frame,
                                text = 'Dirección',
                                font=FONT['text'],
                                text_color=APP_COLOR['gray'])
    customer_address_label.place(relx=0.39,rely=0.6,anchor='e')
    # MAIL
    customer_mail_label = ctk.CTkLabel(help_frame,
                                text = 'Correo',
                                font=FONT['text'],
                                text_color=APP_COLOR['gray'])
    customer_mail_label.place(relx=0.39,rely=0.7,anchor='e')
    # -------------------------------------------------------------------
    # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS
    # -------------------------------------------------------------------
    # ADD
    self.add_customer_btn = ctk.CTkButton(help_frame,
                                text='Agregar',
                                font=FONT['text'],
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'],
                                text_color=APP_COLOR['white'],
                                command=Add_Customer)
    self.add_customer_btn.place(relx=0.4,rely=0.8,relwidth=0.19,anchor='w')
    # CLOSE
    cerrar_btn = ctk.CTkButton(help_frame,
                                text='',
                                width=30,
                                image=ICONS['cancel'],
                                command=lambda: help_frame.destroy(),
                                fg_color=APP_COLOR['red_m'],
                                hover_color=APP_COLOR['red_s'])
    cerrar_btn.place(relx=0.95,rely=0.15,anchor='ne')

    help_frame.wait_window()
    return self.CUSTOMER