import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from DatabaseManager import PROV_MANAGER
from style import FONT, APP_COLORS
# PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - 
class ProveedoresProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.treeview_active = False
        PREFIJOS_L = ['0248','0281','0282','0283','0285','0292','0240','0247',
                    '0278','0243','0244','0246','0273','0278','0284','0285',
                    '0286','0288','0289','0241','0242','0243','0245','0249',
                    '0258','0287','0212']
        PREFIJOS = ['0212','0239','0241','0281','0273','0286']
        ID_FISCAL= ['J','V','E','P','R','G']
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de proveedores',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['title_light'])
        title.pack(pady=5)
    # FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - 
        prov_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        prov_frame.pack(expand=True,fill='both',side='left')
    # GRID SETUP
        for rows in range(18):
            prov_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(16):
            prov_frame.columnconfigure(columns,weight=1,uniform='column')
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # CODIGO
        validarcodigo = self.register(self.ValidarCodigo)
        self.codigo_entry_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.codigo_entry_var,
                                         validate='key',
                                         validatecommand = (validarcodigo,'%P'),
                                         fg_color=APP_COLORS[6])
        self.codigo_entry.grid(row=2,column=6,columnspan=1,sticky='we',padx=5)
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProveedor())
        # NOMBRE
        self.nombre_entry_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.nombre_entry_var,
                                         fg_color=APP_COLORS[6])
        self.nombre_entry.grid(row=3,column=6,columnspan=4,sticky='we',padx=5)
        self.nombre_entry.bind("<Return>", lambda event: self.contacto_entry.focus())
        # CONTACTO
        self.contacto_entry_var = tk.StringVar()
        self.contacto_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.contacto_entry_var,
                                         fg_color=APP_COLORS[6])
        self.contacto_entry.grid(row=4,column=6,columnspan=4,sticky='we',padx=5)
        self.contacto_entry.bind("<Return>", lambda event: self.direccion1_entry.focus())
        # DIRECCION 1
        self.direccion1_entry_var = tk.StringVar()
        self.direccion1_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion1_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion1_entry.grid(row=5,column=6,columnspan=4,sticky='we',padx=5)
        self.direccion1_entry.bind("<Return>", lambda event: self.direccion2_entry.focus())
        # DIRECCION 2
        self.direccion2_entry_var = tk.StringVar()
        self.direccion2_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion2_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion2_entry.grid(row=6,column=6,columnspan=4,sticky='we',padx=5)
        self.direccion2_entry.bind("<Return>", lambda event: self.ciudad_entry.focus())
        # CIUDAD
        self.ciudad_entry_var = tk.StringVar()
        self.ciudad_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.ciudad_entry_var,
                                         fg_color=APP_COLORS[6])
        self.ciudad_entry.grid(row=7,column=6,columnspan=4,sticky='we',padx=5)
        self.ciudad_entry.bind("<Return>", lambda event: self.telefono1_codigo_entry.focus())
        # TELEFONO - CODIGO 1
        validate_phone_pre = self.register(self.ValidatePhonePre)
        self.telefono1_codigo_entry_var = tk.StringVar()
        self.telefono1_codigo_entry = ctk.CTkEntry(prov_frame,
                                         width=85,
                                         validate='key',
                                         validatecommand = (validate_phone_pre,'%P'),
                                         textvariable=self.telefono1_codigo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.telefono1_codigo_entry.grid(row=8,column=7,columnspan=1,sticky='w')
        self.telefono1_codigo_entry.bind("<Return>", lambda event: self.telefono1_entry.focus())
        # TELEFONO 1
        validate_phone = self.register(self.ValidatePhone)
        self.telefono1_entry_var = tk.StringVar()
        self.telefono1_entry = ctk.CTkEntry(prov_frame,
                                            validate='key',
                                            validatecommand = (validate_phone,'%P'),
                                            textvariable=self.telefono1_entry_var,
                                            fg_color=APP_COLORS[6])
        self.telefono1_entry.grid(row=8,column=8,columnspan=2,sticky='we',padx=5)
        self.telefono1_entry.bind("<Return>", lambda event: self.telefono2_codigo_entry.focus())
        # TELEFONO - CODIGO 2
        self.telefono2_codigo_entry_var = tk.StringVar()
        self.telefono2_codigo_entry = ctk.CTkEntry(prov_frame,
                                         width=85,
                                         validate='key',
                                         validatecommand = (validate_phone_pre,'%P'),
                                         textvariable=self.telefono2_codigo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.telefono2_codigo_entry.grid(row=9,column=7,columnspan=1,sticky='w')
        self.telefono2_codigo_entry.bind("<Return>", lambda event: self.telefono2_entry.focus())
        # TELEFONO 2
        self.telefono2_entry_var = tk.StringVar()
        self.telefono2_entry = ctk.CTkEntry(prov_frame,
                                            validate='key',
                                            validatecommand = (validate_phone,'%P'),
                                            textvariable=self.telefono2_entry_var,
                                            fg_color=APP_COLORS[6])
        self.telefono2_entry.grid(row=9,column=8,columnspan=2,sticky='we',padx=5)
        self.telefono2_entry.bind("<Return>", lambda event: self.celular1_codigo_entry.focus())
        # CELULAR - CODIGO 1
        self.celular1_codigo_entry_var = tk.StringVar()
        self.celular1_codigo_entry = ctk.CTkEntry(prov_frame,
                                         width=85,
                                         validate='key',
                                         validatecommand = (validate_phone_pre,'%P'),
                                         textvariable=self.celular1_codigo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.celular1_codigo_entry.grid(row=10,column=7,columnspan=1,sticky='w')
        self.celular1_codigo_entry.bind("<Return>", lambda event: self.celular1_entry.focus())
        # CELULAR 1
        self.celular1_entry_var = tk.StringVar()
        self.celular1_entry = ctk.CTkEntry(prov_frame,
                                           validate='key',
                                           validatecommand = (validate_phone,'%P'),
                                           textvariable=self.celular1_entry_var,
                                           fg_color=APP_COLORS[6])
        self.celular1_entry.grid(row=10,column=8,columnspan=2,sticky='we',padx=5)
        self.celular1_entry.bind("<Return>", lambda event: self.celular2_codigo_entry.focus())
        # CELULAR - CODIGO 2
        self.celular2_codigo_entry_var = tk.StringVar()
        self.celular2_codigo_entry = ctk.CTkEntry(prov_frame,
                                         width=85,
                                         validate='key',
                                         validatecommand = (validate_phone_pre,'%P'),
                                         textvariable=self.celular2_codigo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.celular2_codigo_entry.grid(row=11,column=7,columnspan=1,sticky='w')
        self.celular2_codigo_entry.bind("<Return>", lambda event: self.celular2_entry.focus())
        # CELULAR 2
        self.celular2_entry_var = tk.StringVar()
        self.celular2_entry = ctk.CTkEntry(prov_frame,
                                           validate='key',
                                           validatecommand = (validate_phone,'%P'),
                                           textvariable=self.celular2_entry_var,
                                           fg_color=APP_COLORS[6])
        self.celular2_entry.grid(row=11,column=8,columnspan=2,sticky='we',padx=5)
        self.celular2_entry.bind("<Return>", lambda event: self.email_entry.focus())
        # EMAIL
        self.email_entry_var = tk.StringVar()
        self.email_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.email_entry_var,
                                         fg_color=APP_COLORS[6])
        self.email_entry.grid(row=12,column=6,columnspan=4,sticky='we',padx=5)
        self.email_entry.bind("<Return>", lambda event: self.rif_entry.focus())
        # RIF
        self.rif_entry_var = tk.StringVar()
        self.rif_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.rif_entry_var,
                                         fg_color=APP_COLORS[6])
        self.rif_entry.grid(row=13,column=7,columnspan=3,sticky='we',padx=5)
        self.rif_entry.bind("<Return>", lambda event: self.AgregarProv())
    # PHONE CODES MENU
        # MENU TELEFONO 1
        self.telefono1_menu = ctk.CTkOptionMenu(prov_frame,
                                               fg_color=APP_COLORS[2],
                                               button_color=APP_COLORS[3],
                                               button_hover_color=APP_COLORS[3],
                                               command=lambda opcion:self.telefono1_codigo_entry_var.set(opcion),
                                               values=PREFIJOS)
        self.telefono1_menu.grid(row=8,column=6,columnspan=1,sticky='we',padx=5)
        # MENU TELEFONO 2
        self.telefono2_menu = ctk.CTkOptionMenu(prov_frame,
                                               fg_color=APP_COLORS[2],
                                               button_color=APP_COLORS[3],
                                               button_hover_color=APP_COLORS[3],
                                               command=lambda opcion:self.telefono2_codigo_entry_var.set(opcion),
                                               values=PREFIJOS)
        self.telefono2_menu.grid(row=9,column=6,columnspan=1,sticky='we',padx=5)
        # MENU CELULAR 1
        self.celular1_menu = ctk.CTkOptionMenu(prov_frame,
                                               fg_color=APP_COLORS[2],
                                               button_color=APP_COLORS[3],
                                               button_hover_color=APP_COLORS[3],
                                               command=lambda opcion:self.celular1_codigo_entry_var.set(opcion),
                                               values=['0412','0414','0424','0416','0426'])
        self.celular1_menu.grid(row=10,column=6,columnspan=1,sticky='we',padx=5)
        # MENU CELULAR 2
        self.celular2_menu = ctk.CTkOptionMenu(prov_frame,
                                               fg_color=APP_COLORS[2],
                                               button_color=APP_COLORS[3],
                                               button_hover_color=APP_COLORS[3],
                                               command=lambda opcion:self.celular2_codigo_entry_var.set(opcion),
                                               values=['0412','0414','0424','0416','0426'])
        self.celular2_menu.grid(row=11,column=6,columnspan=1,sticky='we',padx=5)
        # RIF
        self.rif_menu = ctk.CTkOptionMenu(prov_frame,
                                               fg_color=APP_COLORS[2],
                                               button_color=APP_COLORS[3],
                                               button_hover_color=APP_COLORS[3],
                                               command=lambda opcion:self.rif_entry_var.set(f'{opcion}-'),
                                               values=ID_FISCAL)
        self.rif_menu.grid(row=13,column=6,columnspan=1,sticky='we',padx=5)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # CODIGO
        self.codigo_label = ctk.CTkLabel(prov_frame,
                                        text='Código',
                                        font=FONT['text_light'])
        self.codigo_label.grid(row=2,column=5,sticky='e',padx=5)
        # NOMBRE
        self.nombre_label = ctk.CTkLabel(prov_frame,
                                        text='Nombre',
                                        font=FONT['text_light'])
        self.nombre_label.grid(row=3,column=5,sticky='e',padx=5)
        # CONTACTO
        self.contacto_label = ctk.CTkLabel(prov_frame,
                                        text='Contacto',
                                        font=FONT['text_light'])
        self.contacto_label.grid(row=4,column=5,sticky='e',padx=5)
        # DIRECCION 1
        self.direccion1_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 1',
                                        font=FONT['text_light'])
        self.direccion1_label.grid(row=5,column=5,sticky='e',padx=5)
        # DIRECCION 2
        self.direccion2_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 2',
                                        font=FONT['text_light'])
        self.direccion2_label.grid(row=6,column=5,sticky='e',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONT['text_light'])
        self.ciudad_label.grid(row=7,column=5,sticky='e',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONT['text_light'])
        self.ciudad_label.grid(row=7,column=5,sticky='e',padx=5)
        # TELEFONO 1
        self.telefono1_label = ctk.CTkLabel(prov_frame,
                                        text='Teléfono 1',
                                        font=FONT['text_light'])
        self.telefono1_label.grid(row=8,column=5,sticky='e',padx=5)
        # TELEFONO 2
        self.telefono2_label = ctk.CTkLabel(prov_frame,
                                        text='Teléfono 2',
                                        font=FONT['text_light'])
        self.telefono2_label.grid(row=9,column=5,sticky='e',padx=5)
        # CELULAR 1
        self.celular1_label = ctk.CTkLabel(prov_frame,
                                        text='Celular 1',
                                        font=FONT['text_light'])
        self.celular1_label.grid(row=10,column=5,sticky='e',padx=5)
        # CELULAR 2
        self.celular2_label = ctk.CTkLabel(prov_frame,
                                        text='Celular 2',
                                        font=FONT['text_light'])
        self.celular2_label.grid(row=11,column=5,sticky='e',padx=5)
        # EMAIL
        self.email_label = ctk.CTkLabel(prov_frame,
                                        text='Email',
                                        font=FONT['text_light'])
        self.email_label.grid(row=12,column=5,sticky='e',padx=5)
        # RIF
        self.rif_label = ctk.CTkLabel(prov_frame,
                                        text='Id. Fiscal',
                                        font=FONT['text_light'])
        self.rif_label.grid(row=13,column=4,columnspan=2,sticky='e',padx=5)
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        self.goback_btn = ctk.CTkButton(prov_frame,
                                     text='Volver atrás',
                                     command=self.GoBack_CB,
                                     fg_color=APP_COLORS[4],
                                     hover_color=APP_COLORS[3])
        self.goback_btn.grid(row=0,column=0,columnspan=2,sticky='we',padx=5,pady=5)
        # AGREGAR
        self.agregar_btn = ctk.CTkButton(prov_frame,
                                     text='Agregar',
                                     command=self.AgregarProv,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.agregar_btn.grid(row=15,column=6,columnspan=2,sticky='we',padx=5,pady=5)
        # CANCELAR
        self.cancelar_btn = ctk.CTkButton(prov_frame,
                                     text='Cancelar',
                                     command=self.Restablecer,
                                     state='disabled',
                                     fg_color=APP_COLORS[10],
                                     hover_color=APP_COLORS[10])
        self.cancelar_btn.grid(row=15,column=8,columnspan=2,sticky='we',padx=5,pady=5)
        # MODIFICAR
        self.mod_btn = ctk.CTkButton(prov_frame,
                                     text='Modificar',
                                     command=self.ModificarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.mod_btn.grid(row=16,column=6,columnspan=2,sticky='we',padx=5,pady=5)
        # ELIMINAR
        self.del_btn = ctk.CTkButton(prov_frame,
                                     text='Eliminar',
                                     command=self.EliminarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[10],
                                     hover_color=APP_COLORS[10])
        self.del_btn.grid(row=16,column=8,columnspan=2,sticky='we',padx=5,pady=5)
        # BUSCAR PROVEEDOR
        self.buscar_prov_btn = ctk.CTkButton(prov_frame,
                                     text='Buscar proveedor',
                                     command=self.AyudaProveedores,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.buscar_prov_btn.grid(row=2,column=7,columnspan=3,sticky='we',padx=5,pady=5)
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
    # VALIDAR CAMPOS DE TELEFONO Y CELULAR:
    def ValidatePhoneNumber(self,pref,numero,tipo):
        if numero:
            if not pref:
                messagebox.showinfo('Atención',f'Agregue el prefijo del número del {tipo}.')
                return False
            if len(pref) != 4:
                messagebox.showinfo('Atención',f'Revise el prefijo de {tipo}.\n'
                                    'No debe tener espacios y el formato es "0000".')
                return False
            if len(numero) != 7:
                messagebox.showinfo('Atención',f'Revise el número de {tipo}.\n'
                                    'No debe tener espacios y el formato es "0000000".')
                return False
            return pref.strip() + ' - ' + numero.strip()
        return ''
    # AGREGAR PROVEEDOR
    def AgregarProv(self):
        codigo = self.codigo_entry_var.get()
        nombre = self.nombre_entry_var.get()
        contacto = self.contacto_entry_var.get()
        direccion1 = self.direccion1_entry_var.get()
        direccion2 = self.direccion2_entry_var.get()
        ciudad = self.ciudad_entry_var.get()
        pre_telefono_1 = self.telefono1_codigo_entry_var.get()
        telefono_1 = self.telefono1_entry_var.get()
        pre_telefono_2 = self.telefono2_codigo_entry_var.get()
        telefono_2 = self.telefono2_entry_var.get()
        pre_celular_1 = self.celular1_codigo_entry_var.get()
        celular_1 = self.celular1_entry_var.get()
        pre_celular_2 = self.celular2_codigo_entry_var.get()
        celular_2 = self.celular2_entry_var.get()
        email = self.email_entry_var.get()
        rif = self.rif_entry_var.get()
        # CHEQUEAR CODIGO
        if codigo == '':
            messagebox.showinfo('Atención','Debe agregar un codigo de proveedor')
            self.codigo_entry.focus()
            return
        # CHEQUEAR NOMBRE
        if nombre == '':
            messagebox.showinfo('Atención','Debe agregar un nombre de proveedor.')
            self.nombre_entry.focus()
            return
        telefono_1 = self.ValidatePhoneNumber(pre_telefono_1,telefono_1,'Teléfono 1')
        telefono_2 = self.ValidatePhoneNumber(pre_telefono_2,telefono_2,'Teléfono 2')
        celular_1 = self.ValidatePhoneNumber(pre_celular_1,celular_1,'Celular 1')
        celular_2 = self.ValidatePhoneNumber(pre_celular_2,celular_2,'Celular 2')
        if telefono_1 == False or telefono_2 == False or celular_1 == False or celular_2 == False:
            return
        if rif == '':
            messagebox.showinfo('Atención','Debe agregar un número de identificación fiscal.')
            self.rif_entry.focus()
            return
        PROV_MANAGER.Add_Prov(codigo,nombre,contacto,direccion1,direccion2,
                              ciudad,telefono_1,telefono_2,celular_1,celular_2,email,rif)
        self.Restablecer()
    # MODIFICAR PROVEEDOR
    def ModificarProv(self):
        codigo = self.codigo_entry_var.get()
        nombre = self.nombre_entry_var.get()
        contacto = self.contacto_entry_var.get()
        direccion1 = self.direccion1_entry_var.get()
        direccion2 = self.direccion2_entry_var.get()
        ciudad = self.ciudad_entry_var.get()
        pre_telefono_1 = self.telefono1_codigo_entry_var.get()
        telefono_1 = self.telefono1_entry_var.get()
        pre_telefono_2 = self.telefono2_codigo_entry_var.get()
        telefono_2 = self.telefono2_entry_var.get()
        pre_celular_1 = self.celular1_codigo_entry_var.get()
        celular_1 = self.celular1_entry_var.get()
        pre_celular_2 = self.celular2_codigo_entry_var.get()
        celular_2 = self.celular2_entry_var.get()
        email = self.email_entry_var.get()
        rif = self.rif_entry_var.get()
        # CHEQUEAR CODIGO
        if codigo == '':
            messagebox.showinfo('Atención','Debe agregar un codigo de proveedor')
            self.codigo_entry.focus()
            return
        # CHEQUEAR NOMBRE
        if nombre == '':
            messagebox.showinfo('Atención','Debe agregar un nombre de proveedor.')
            self.nombre_entry.focus()
            return
        telefono_1 = self.ValidatePhoneNumber(pre_telefono_1,telefono_1,'Teléfono 1')
        telefono_2 = self.ValidatePhoneNumber(pre_telefono_2,telefono_2,'Teléfono 2')
        celular_1 = self.ValidatePhoneNumber(pre_celular_1,celular_1,'Celular 1')
        celular_2 = self.ValidatePhoneNumber(pre_celular_2,celular_2,'Celular 2')
        if telefono_1 == False or telefono_2 == False or celular_1 == False or celular_2 == False:
            return
        if rif == '':
            messagebox.showinfo('Atención','Debe agregar un número de identificación fiscal.')
            self.rif_entry.focus()
            return
        answer = messagebox.showinfo('¡Atención!',f'Está seguro que desea guardar el proveedor {codigo} - {nombre} '
                                     'con estos datos?')
        if not answer:
            return
        PROV_MANAGER.Mod_Prov(codigo,nombre,contacto,direccion1,direccion2,
                              ciudad,telefono_1,telefono_2,celular_1,celular_2,email,rif)
        self.Restablecer()
    def EliminarProv(self):
        codigo = self.codigo_entry_var.get()
        nombre = self.nombre_entry_var.get()
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea eliminar el proveedor {codigo} - {nombre}?')
        if not answer:
            return
        PROV_MANAGER.Del_Prov(codigo)
        self.Restablecer()
    # CANCELAR SELECCION
    def Restablecer(self):
        self.rif_entry.unbind("<Return>")
        self.rif_entry.bind("<Return>", lambda event: self.AgregarProv())
        self.codigo_entry_var.set('')
        self.nombre_entry_var.set('')
        self.contacto_entry_var.set('')
        self.direccion1_entry_var.set('')
        self.direccion2_entry_var.set('')
        self.ciudad_entry_var.set('')
        self.telefono1_codigo_entry_var.set('')
        self.telefono1_entry_var.set('')
        self.telefono2_codigo_entry_var.set('')
        self.telefono2_entry_var.set('')
        self.celular1_codigo_entry_var.set('')
        self.celular1_entry_var.set('')
        self.celular2_codigo_entry_var.set('')
        self.celular2_entry_var.set('')
        self.email_entry_var.set('')
        self.rif_entry_var.set('')
        # DESBLOQUEAR EL CODIGO DE PROVEEDOR
        self.codigo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        # CONFIGURAR BOTONES
        self.agregar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        # FOCUS EN CODIGO
        self.codigo_entry.focus()
# BUSCAR UN PROVEEDOR POR CODIGO Y PONERLO EN PANTALLA
    def BuscarProveedor(self):
        self.rif_entry.unbind("<Return>")
        self.rif_entry.bind("<Return>", lambda event: self.ModificarProv())
        if self.treeview_active:
            codigo = str(self.search_bar_var.get()).strip()
            self.tree_frame.destroy
            self.treeview_active = False
        else:
            codigo = str(self.codigo_entry_var.get()).strip()
        # CONVERTIR EL CODIGO A ENTERO
        if codigo == '':
            return
        try:
            codigo = int(codigo)
        except Exception as e:
            messagebox.showerror('Error',f'Error con el codigo {codigo}: {str(e)}')
        # VALIDAR EL CODIGO
        if not PROV_MANAGER.ValidateProv(codigo):
            self.nombre_entry.focus()
            return
        proveedor = PROV_MANAGER.GetProv(codigo)
        self.codigo_entry_var.set(codigo)
        self.nombre_entry_var.set(proveedor['nombre'])
        self.contacto_entry_var.set(proveedor['contacto'])
        self.direccion1_entry_var.set(proveedor['direccion1'])
        self.direccion2_entry_var.set(proveedor['direccion2'])
        self.ciudad_entry_var.set(proveedor['ciudad'])
        if proveedor['telefono1']:
            self.telefono1_codigo_entry_var.set(proveedor['telefono1'].split(' - ')[0])
            self.telefono1_entry_var.set(proveedor['telefono1'].split(' - ')[1])
        if proveedor['telefono2']:
            self.telefono2_codigo_entry_var.set(proveedor['telefono2'].split(' - ')[0])
            self.telefono2_entry_var.set(proveedor['telefono2'].split(' - ')[1])
        if proveedor['celular1']:
            self.celular1_codigo_entry_var.set(proveedor['celular1'].split(' - ')[0])
            self.celular1_entry_var.set(proveedor['celular1'].split(' - ')[1])
        if proveedor['celular2']:
            self.celular2_codigo_entry_var.set(proveedor['celular2'].split(' - ')[0])
            self.celular2_entry_var.set(proveedor['celular2'].split(' - ')[1])
        self.email_entry_var.set(proveedor['email'])
        self.rif_entry_var.set(proveedor['rif'])
        # ENTRAR EN MODO EDICION
        self.ModoEdicion()
# MODO EDICION - MODO EDICION - MODO EDICION - MODO EDICION - MODO EDICION - MODO EDICION - MODO EDICION - 
    def ModoEdicion(self):
        # BLOQUEAR EL CODIGO DE PROVEEDOR
        self.codigo_entry.configure(state='disabled',fg_color=APP_COLORS[4])
        # CONFIGURAR BOTONES
        self.agregar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancelar_btn.configure(state='enabled',fg_color=APP_COLORS[9])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[9])
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
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
        self.treeview.bind("<<TreeviewSelect>>",self.ClickTreeview)
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
            font = FONT['text_small'],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONT['text_light'])
    # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.tree_frame,
                                     orientation='vertical',
                                     command=self.treeview.yview)
        scrollbar.grid(row=1,column=3,sticky='ns',padx=5,pady=5,rowspan=2)
        self.treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListProv()
    # SELECIONAR PRODUCTO EN EL TREEVIEW
    def ClickTreeview(self,event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        self.search_bar_var.set(info['text'])
        if PROV_MANAGER.CheckProv(info['text']):
            self.BuscarProveedor()
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
        print(resultados)
        for proveedor in resultados:
            self.treeview.insert("", 'end',
                                 text=proveedor['codigo'],
                                 values=(proveedor['nombre']))
    
    # VALIDAR ENTRADA DE CODIGO
    def ValidarCodigo(self,texto):
        if len(texto) > 3:
            return False
        if texto == '':
            return True
        return texto.isdigit()
    # VALIDAR ENTRADA DE NUMEROS DE TELEFONO (CODIGOS)
    def ValidatePhonePre(self,texto):
        if len(texto) > 4:
            return False
        if texto == '':
            return True
        return texto.isdigit()
    # VALIDAR ENTRADA DE NUMEROS DE TELEFONO
    def ValidatePhone(self,texto):
        if len(texto) > 7:
            return False
        if texto == '':
            return True
        return texto.isdigit()