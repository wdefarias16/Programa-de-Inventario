import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Database import PROV_MANAGER
from style import FONTS, APP_COLORS

# PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - PROGRAMA DE CARGA DE PROVEEDORES - 
class ProveedoresProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.treeview_active = False
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de proveedores',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=5)
    # FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - FRAME PROVEDORES - 
        prov_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        prov_frame.pack(expand=True,fill='both',side='left')
    # GRID SETUP
        for rows in range(18):
            prov_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(6):
            prov_frame.columnconfigure(columns,weight=1,uniform='column')
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # CODIGO
        validarcodigo = self.register(self.ValidarCodigo)
        self.codigo_entry_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.codigo_entry_var,
                                         validate='key',
                                         validatecommand = (validarcodigo,'%P'),
                                         fg_color=APP_COLORS[6])
        self.codigo_entry.grid(row=2,column=2,columnspan=2,sticky='we',padx=5)
        self.codigo_entry.bind("<Return>",lambda event:self.BuscarProveedor())
        # NOMBRE
        self.nombre_entry_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.nombre_entry_var,
                                         fg_color=APP_COLORS[6])
        self.nombre_entry.grid(row=3,column=2,columnspan=2,sticky='we',padx=5)
        # CONTACTO
        self.contacto_entry_var = tk.StringVar()
        self.contacto_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.contacto_entry_var,
                                         fg_color=APP_COLORS[6])
        self.contacto_entry.grid(row=4,column=2,columnspan=2,sticky='we',padx=5)
        # DIRECCION 1
        self.direccion1_entry_var = tk.StringVar()
        self.direccion1_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion1_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion1_entry.grid(row=5,column=2,columnspan=2,sticky='we',padx=5)
        # DIRECCION 2
        self.direccion2_entry_var = tk.StringVar()
        self.direccion2_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.direccion2_entry_var,
                                         fg_color=APP_COLORS[6])
        self.direccion2_entry.grid(row=6,column=2,columnspan=2,sticky='we',padx=5)
        # CIUDAD
        self.ciudad_entry_var = tk.StringVar()
        self.ciudad_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.ciudad_entry_var,
                                         fg_color=APP_COLORS[6])
        self.ciudad_entry.grid(row=7,column=2,columnspan=2,sticky='we',padx=5)
        # TELEFONO
        self.telefono_entry_var = tk.StringVar()
        self.telefono_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.telefono_entry_var,
                                         fg_color=APP_COLORS[6])
        self.telefono_entry.grid(row=8,column=2,columnspan=2,sticky='we',padx=5)
        # CELULAR
        self.celular_entry_var = tk.StringVar()
        self.celular_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.celular_entry_var,
                                         fg_color=APP_COLORS[6])
        self.celular_entry.grid(row=9,column=2,columnspan=2,sticky='we',padx=5)
        # EMAIL
        self.email_entry_var = tk.StringVar()
        self.email_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.email_entry_var,
                                         fg_color=APP_COLORS[6])
        self.email_entry.grid(row=10,column=2,columnspan=2,sticky='we',padx=5)
        # RIF
        self.rif_entry_var = tk.StringVar()
        self.rif_entry = ctk.CTkEntry(prov_frame,
                                         textvariable=self.rif_entry_var,
                                         fg_color=APP_COLORS[6])
        self.rif_entry.grid(row=11,column=2,columnspan=2,sticky='we',padx=5)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # TITULO
        self.titulo_label = ctk.CTkLabel(prov_frame,
                                        text='Cargar datos del proveedor',
                                        font=FONTS[1])
        self.titulo_label.grid(row=1,column=2,sticky='w',padx=5)
        # CODIGO
        self.codigo_label = ctk.CTkLabel(prov_frame,
                                        text='Código',
                                        font=FONTS[1])
        self.codigo_label.grid(row=2,column=4,sticky='w',padx=5)
        # NOMBRE
        self.nombre_label = ctk.CTkLabel(prov_frame,
                                        text='Nombre',
                                        font=FONTS[1])
        self.nombre_label.grid(row=3,column=4,sticky='w',padx=5)
        # CONTACTO
        self.contacto_label = ctk.CTkLabel(prov_frame,
                                        text='Contacto',
                                        font=FONTS[1])
        self.contacto_label.grid(row=4,column=4,sticky='w',padx=5)
        # DIRECCION 1
        self.direccion1_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 1',
                                        font=FONTS[1])
        self.direccion1_label.grid(row=5,column=4,sticky='w',padx=5)
        # DIRECCION 2
        self.direccion2_label = ctk.CTkLabel(prov_frame,
                                        text='Dirección 2',
                                        font=FONTS[1])
        self.direccion2_label.grid(row=6,column=4,sticky='w',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONTS[1])
        self.ciudad_label.grid(row=7,column=4,sticky='w',padx=5)
        # CIUDAD
        self.ciudad_label = ctk.CTkLabel(prov_frame,
                                        text='Ciudad',
                                        font=FONTS[1])
        self.ciudad_label.grid(row=7,column=4,sticky='w',padx=5)
        # TELEFONO
        self.telefono_label = ctk.CTkLabel(prov_frame,
                                        text='Teléfono',
                                        font=FONTS[1])
        self.telefono_label.grid(row=8,column=4,sticky='w',padx=5)
        # CELULAR
        self.celular_label = ctk.CTkLabel(prov_frame,
                                        text='Celular',
                                        font=FONTS[1])
        self.celular_label.grid(row=9,column=4,sticky='w',padx=5)
        # EMAIL
        self.email_label = ctk.CTkLabel(prov_frame,
                                        text='Email',
                                        font=FONTS[1])
        self.email_label.grid(row=10,column=4,sticky='w',padx=5)
        # RIF
        self.rif_label = ctk.CTkLabel(prov_frame,
                                        text='RIF',
                                        font=FONTS[1])
        self.rif_label.grid(row=11,column=4,sticky='w',padx=5)
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        self.goback_btn = ctk.CTkButton(prov_frame,
                                     text='Volver atrás',
                                     command=self.GoBack_CB,
                                     fg_color=APP_COLORS[4],
                                     hover_color=APP_COLORS[3])
        self.goback_btn.grid(row=0,column=0,sticky='we',padx=5,pady=5)
        # AGREGAR
        self.agregar_btn = ctk.CTkButton(prov_frame,
                                     text='Agregar',
                                     command=self.AgregarProv,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.agregar_btn.grid(row=13,column=2,sticky='we',padx=5,pady=5)
        # CANCELAR
        self.cancelar_btn = ctk.CTkButton(prov_frame,
                                     text='Cancelar',
                                     command=self.Restablecer,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.cancelar_btn.grid(row=13,column=3,sticky='we',padx=5,pady=5)
        # MODIFICAR
        self.mod_btn = ctk.CTkButton(prov_frame,
                                     text='Modificar',
                                     command=self.ModificarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.mod_btn.grid(row=14,column=2,sticky='we',padx=5,pady=5)
        # ELIMINAR
        self.del_btn = ctk.CTkButton(prov_frame,
                                     text='Eliminar',
                                     command=self.EliminarProv,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.del_btn.grid(row=14,column=3,sticky='we',padx=5,pady=5)
        # BUSCAR PROVEEDOR
        self.buscar_prov_btn = ctk.CTkButton(prov_frame,
                                     text='Buscar proveedor',
                                     command=self.AyudaProveedores,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.buscar_prov_btn.grid(row=1,column=3,sticky='we',padx=5,pady=5)
# COMANDOS DE BOTONES - COMANDOS DE BOTONES - COMANDOS DE BOTONES - COMANDOS DE BOTONES - COMANDOS DE BOTONES - 
    # AGREGAR PROVEEDOR
    def AgregarProv(self):
        codigo = self.codigo_entry_var.get()
        nombre = self.nombre_entry_var.get()
        contacto = self.contacto_entry_var.get()
        direccion1 = self.direccion1_entry_var.get()
        direccion2 = self.direccion2_entry_var.get()
        ciudad = self.ciudad_entry_var.get()
        telefono = self.telefono_entry_var.get()
        celular = self.celular_entry_var.get()
        email = self.email_entry_var.get()
        rif = self.rif_entry_var.get()

        if len(codigo) != 3 or codigo == '':
            messagebox.showinfo('Atención',f'Debe agregar un codigo de proveedor y el formato debe ser "000".')
        elif nombre == '':
            messagebox.showinfo('Atención',f'Debe agregar un nombre de proveedor.')
        else:
            PROV_MANAGER.Add_Prov(codigo,nombre,contacto,direccion1,direccion2,ciudad,telefono,celular,email,rif)
            self.Restablecer()
    # MODIFICAR PROVEEDOR
    def ModificarProv(self):
        codigo = self.codigo_entry_var.get()
        nombre = self.nombre_entry_var.get()
        contacto = self.contacto_entry_var.get()
        direccion1 = self.direccion1_entry_var.get()
        direccion2 = self.direccion2_entry_var.get()
        ciudad = self.ciudad_entry_var.get()
        telefono = self.telefono_entry_var.get()
        celular = self.celular_entry_var.get()
        email = self.email_entry_var.get()
        rif = self.rif_entry_var.get()
        PROV_MANAGER.Mod_Prov(codigo,nombre,contacto,direccion1,direccion2,ciudad,telefono,celular,email,rif)
        self.Restablecer()
    def EliminarProv(self):
        codigo = self.codigo_entry_var.get()
        PROV_MANAGER.Del_Prov(codigo)
        self.Restablecer()
    # CANCELAR SELECCION
    def Restablecer(self):
        self.codigo_entry_var.set('')
        self.nombre_entry_var.set('')
        self.contacto_entry_var.set('')
        self.direccion1_entry_var.set('')
        self.direccion2_entry_var.set('')
        self.ciudad_entry_var.set('')
        self.telefono_entry_var.set('')
        self.celular_entry_var.set('')
        self.email_entry_var.set('')
        self.rif_entry_var.set('')
        # DESBLOQUEAR EL CODIGO DE PROVEEDOR
        self.codigo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        # CONFIGURAR BOTONES
        self.agregar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.cancelar_btn.configure(state='disabled',fg_color=APP_COLORS[3])
# BUSCAR UN PROVEEDOR POR CODIGO Y PONERLO EN PANTALLA
    def BuscarProveedor(self):
        if self.treeview_active:
            codigo = self.search_bar_var.get()
            self.tree_frame.destroy
            self.treeview_active = False
        else:
            codigo = self.codigo_entry_var.get()
        proveedor = PROV_MANAGER.BuscarProv(codigo)
        if PROV_MANAGER.ChechProv(codigo):
            self.codigo_entry_var.set(codigo)
            self.nombre_entry_var.set(proveedor['nombre'])
            self.contacto_entry_var.set(proveedor['contacto'])
            self.direccion1_entry_var.set(proveedor['direccion1'])
            self.direccion2_entry_var.set(proveedor['direccion2'])
            self.ciudad_entry_var.set(proveedor['ciudad'])
            self.telefono_entry_var.set(proveedor['telefono'])
            self.celular_entry_var.set(proveedor['celular'])
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
        self.cancelar_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
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
    def ClickTreeview(self,event):
        item_id = self.treeview.selection()
        info = self.treeview.item(item_id)
        self.search_bar_var.set(info['text'])
        if PROV_MANAGER.ChechProv(info['text']):
            self.BuscarProveedor()
        self.tree_frame.destroy()
    def ListProv(self):
        proveedores = PROV_MANAGER.GetProv()
        for item in self.treeview.get_children():
                self.treeview.delete(item)
        for codigo,proveedor in proveedores.items():
            self.treeview.insert("",'end',
                                 text=codigo,
                                 values=(proveedor['nombre']))
    def BuscarProvNombre(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        busqueda = self.search_bar_var.get().lower()
        resultados = PROV_MANAGER.BuscarNombres(busqueda)
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