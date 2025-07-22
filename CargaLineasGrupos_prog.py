import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from style import FONT,APP_COLORS
from DatabaseManager import LINE_MANAGER

# PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS
class LineasGruposProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.modo_agregar_grupo_activo = False
        self.cancel_grupo_btn_active = False
        self.addgrupo_btn_active = False
        # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de líneas y grupos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['title_light'])
        title.pack(pady=10)
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        self.main_frame = ctk.CTkFrame(self,
                                       corner_radius=0,
                                       fg_color=APP_COLORS[0])
        self.main_frame.pack(fill='both',expand=True)
        # GRID SET UP
        for rows in range(16):
            self.main_frame.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(6):
            self.main_frame.columnconfigure(columns,weight=1,uniform='column')

    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # CODIGO
        validarlinea = self.register(self.ValidarCodigoLinea)  
        self.codigo_entry_var = tk.StringVar()
        self.codigo_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validarlinea,'%P'),
                                         textvariable=self.codigo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.codigo_entry.grid(row=2,column=2,columnspan=2,sticky='we',padx=5)
        self.codigo_entry.bind("<Return>", lambda event: self.GetLineByCode())
        self.codigo_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.codigo_entry.bind("<Control-s>",lambda event: self.LineHelp())
        self.codigo_entry.bind("<Control-S>",lambda event: self.LineHelp())
        self.codigo_entry.focus()
        # NOMBRE - DESCRIPCION
        self.nombre_entry_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.nombre_entry_var,
                                         fg_color=APP_COLORS[6])
        self.nombre_entry.grid(row=3,column=2,columnspan=2,sticky='we',padx=5)
        self.nombre_entry.bind("<Return>", lambda event: self.AgregarLinea())
        self.nombre_entry.bind("<Control-Return>", lambda event: self.ModoAgregarGrupo())
        self.nombre_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # TITULO LINEAS
        self.titulo_line = ctk.CTkLabel(self.main_frame,
                                        text='Cargar una línea',
                                        font=FONT['text_light'])
        self.titulo_line.grid(row=1,column=2,sticky='w')
        # CODIGO
        codigo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de línea',
                                    font=FONT['text_light'])
        codigo_label.grid(row=2,column=4,columnspan=2,sticky='w')
        # NOMBRE - DESCRIPCION
        descrip_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONT['text_light'])
        descrip_label.grid(row=3,column=4,columnspan=2,sticky='w')
    # LINE HELP BUTTON - LINE HELP BUTTON - LINE HELP BUTTON - LINE HELP BUTTON - LINE HELP BUTTON - LINE HELP BUTTON - 
        # BUSCAR LINEA
        self.find_line_btn = ctk.CTkButton(self.main_frame,
                                     text='Líneas',
                                     command=self.LineHelp,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.find_line_btn.grid(row=2,column=1,sticky='we',padx=5)
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # VOLVER ATRAS
        self.goback_btn = ctk.CTkButton(self.main_frame,
                                     text='Volver atrás',
                                     command=self.GoBack_CB,
                                     fg_color=APP_COLORS[4],
                                     hover_color=APP_COLORS[3])
        self.goback_btn.grid(row=0,column=0,sticky='we',padx=5,pady=5)
        # AGREGAR
        self.add_btn = ctk.CTkButton(self.main_frame,
                                     text='Agregar',
                                     command=self.AgregarLinea,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.add_btn.grid(row=4,column=2,sticky='we',padx=5,pady=5)
        # MODIFICAR
        self.mod_btn = ctk.CTkButton(self.main_frame,
                                     text='Modificar',
                                     command=self.ModificarLinea,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.mod_btn.grid(row=5,column=2,sticky='we',padx=5,pady=5)
        # ELIMINAR
        self.del_btn = ctk.CTkButton(self.main_frame,
                                     text='Eliminar',
                                     command=self.EliminarLinea,
                                     state='disabled',
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        self.del_btn.grid(row=4,column=3,sticky='we',padx=5,pady=5)
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# FUNCIONES DE LINEA
    # AGREGAR LINEA
    def AgregarLinea(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        if codigo == '' or nombre == '':
            messagebox.showerror('Error','Debe rellenar los campos')
        else:
            if LINE_MANAGER.Add_Line(codigo,nombre):
                self.Restablecer()
    # ELIMINAR LINEA
    def EliminarLinea(self):
        codigo = self.codigo_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar la línea {codigo}?'
                                     '\nEsto Eliminará tambien todos sus grupos.')
        if answer:
            LINE_MANAGER.Del_Linea(codigo)
            self.Restablecer()
    # MODIFICAR LINEA
    def ModificarLinea(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea modificar la línea {codigo}?')
        if answer:
            LINE_MANAGER.Mod_Linea(codigo,nombre)
            self.Restablecer()
# FUNCIONES DE GRUPO
    # AGREGAR GRUPO
    def AgregarGrupo(self):
        codigo = self.codigo_entry_var.get()
        codigo_grupo = self.codigo_grupo_entry_var.get()
        nombre_grupo = self.grupo_entry_var.get()
        if codigo_grupo == '':
            messagebox.showerror('Error de carga','Debe agregar un codigo de grupo.')
            self.codigo_grupo_entry.focus()
            return
        if nombre_grupo == '':
            messagebox.showerror('Error de carga','Debe agregar un nombre de grupo.')
            self.grupo_entry.focus()
            return
        try:
            p1 = float(self.PorV1_entry_var.get())
            p2 = float(self.PorV2_entry_var.get())
            p3 = float(self.PorV3_entry_var.get())
        except Exception:
            messagebox.showerror('Error de carga','Debe cargar los porcentajes.'
                                 '\nNinguno puede ser menor o igual a 0')
            return
        if p1 <= 0 or p2 <= 0 or p3 <= 0:
            messagebox.showerror('Error de carga','Debe cargar los porcentajes.'
                                 '\nNinguno puede ser menor o igual a 0')
            self.PorV1_entry.focus()
            return
        LINE_MANAGER.Add_Group(codigo,codigo_grupo,nombre_grupo,p1,p2,p3)
        self.LimpiarGrupo()
        self.codigo_grupo_entry.focus()
    # MODIFICAR GRUPO
    def ModificarGrupo(self):
        linea = self.codigo_entry_var.get()
        grupo = self.codigo_grupo_entry_var.get()
        nombre_grupo = self.grupo_entry_var.get()
        if nombre_grupo == '':
            messagebox.showerror('Error de carga','Debe agregar un nombre de grupo.')
            self.grupo_entry.focus()
            return
        try:
            p1 = float(self.PorV1_entry_var.get())
            p2 = float(self.PorV2_entry_var.get())
            p3 = float(self.PorV3_entry_var.get())
        except Exception:
            messagebox.showerror('Error de carga','Debe cargar los porcentajes.'
                                 '\nNinguno puede ser menor o igual a 0')
            return
        if p1 <= 0 or p2 <= 0 or p3 <= 0:
            messagebox.showerror('Error de carga','Debe cargar los porcentajes.'
                                 '\nNinguno puede ser menor o igual a 0')
            self.PorV1_entry.focus()
            return
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea modificar el grupo {grupo} con los valores actuales?')
        if not answer:
            return
        LINE_MANAGER.Mod_Grupo(linea,grupo,nombre_grupo,p1,p2,p3)
        self.LimpiarGrupo()
    # ELIMINAR GRUPO
    def EliminarGrupo(self):
        linea = self.codigo_entry_var.get()
        grupo = self.codigo_grupo_entry_var.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar el grupo {grupo}?')
        if answer:
            LINE_MANAGER.Del_Group(linea,grupo)
        self.LimpiarGrupo()
# MODO AGREGAR GRUPO - MODO AGREGAR GRUPO - MODO AGREGAR GRUPO - MODO AGREGAR GRUPO - MODO AGREGAR GRUPO - MODO AGREGAR GRUPO - 
    def ModoAgregarGrupo(self):
        self.current_line = LINE_MANAGER.CheckLine(self.codigo_entry_var.get())
        if not self.current_line:
            messagebox.showerror('Error','Seleccione una línea válida.')
            return
        self.modo_agregar_grupo_activo = True
        self.addgrupo_btn.destroy()
        # TITULO CARGA GRUPO
        self.titulo_grupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Carga de grupo',
                                    font=FONT['text_light'])
        self.titulo_grupo_label.grid(row=7,column=2,columnspan=2,sticky='w')
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # ENTRADA CODIGO GRUPO
        validargrupo = self.register(self.ValidarCodigoGrupo)
        self.codigo_grupo_entry_var = tk.StringVar()
        self.codigo_grupo_entry = ctk.CTkEntry(self.main_frame,
                                        validate = 'key',
                                        validatecommand = (validargrupo,'%P'),
                                        textvariable=self.codigo_grupo_entry_var,
                                        fg_color=APP_COLORS[6])
        self.codigo_grupo_entry.grid(row=8,column=2,columnspan=2,sticky='we',padx=5)
        self.codigo_grupo_entry.bind("<Return>", lambda event: self.GetGroupByCode())
        self.codigo_grupo_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.codigo_grupo_entry.bind("<Control-BackSpace>",lambda event: self.LimpiarGrupo())
        self.codigo_grupo_entry.bind("<Control-s>",lambda event: self.GroupHelp())
        self.codigo_grupo_entry.bind("<Control-S>",lambda event: self.GroupHelp())
        self.codigo_grupo_entry.focus()
        # ENTRADA DESCRIPCION
        self.grupo_entry_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.grupo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.grupo_entry.grid(row=9,column=2,columnspan=2,sticky='we',padx=5)
        self.grupo_entry.bind("<Return>",lambda event: self.PorV1_entry.focus())
        self.grupo_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.grupo_entry.bind("<Control-BackSpace>",lambda event: self.LimpiarGrupo())
        # PORCENTAJE 1
        validar_pctj = self.register(self.ValidarPorcentajes)
        self.PorV1_entry_var = tk.StringVar()
        self.PorV1_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV1_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV1_entry.grid(row=10,column=2,columnspan=2,sticky='we',padx=5)
        self.PorV1_entry.bind("<Return>",lambda event: self.PorV2_entry.focus())
        self.PorV1_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV1_entry.bind("<Control-BackSpace>",lambda event: self.LimpiarGrupo())
        # PORCENTAJE 2
        self.PorV2_entry_var = tk.StringVar()
        self.PorV2_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV2_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV2_entry.grid(row=11,column=2,columnspan=2,sticky='we',padx=5)
        self.PorV2_entry.bind("<Return>",lambda event: self.PorV3_entry.focus())
        self.PorV2_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV2_entry.bind("<Control-BackSpace>",lambda event: self.LimpiarGrupo())
        # PORCENTAJE 3
        self.PorV3_entry_var = tk.StringVar()
        self.PorV3_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV3_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV3_entry.grid(row=12,column=2,columnspan=2,sticky='we',padx=5)
        self.PorV3_entry.bind("<Return>",lambda event: self.AgregarGrupo())
        self.PorV3_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV3_entry.bind("<Control-BackSpace>",lambda event: self.LimpiarGrupo())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # CODIGO
        self.codigoGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de grupo',
                                    font=FONT['text_light'])
        self.codigoGrupo_label.grid(row=8,column=4,columnspan=2,sticky='w')
        # DESCRIPCION
        self.nombreGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONT['text_light'])
        self.nombreGrupo_label.grid(row=9,column=4,columnspan=2,sticky='w')
        # PDV1
        self.pdv1_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 1',
                                    font=FONT['text_light'])
        self.pdv1_label.grid(row=10,column=4,columnspan=2,sticky='w')
        # PDV2
        self.pdv2_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 2',
                                    font=FONT['text_light'])
        self.pdv2_label.grid(row=11,column=4,columnspan=2,sticky='w')
        # PDV3
        self.pdv3_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 3',
                                    font=FONT['text_light'])
        self.pdv3_label.grid(row=12,column=4,columnspan=2,sticky='w')
        # GROUP HELP BUTTON - GROUP HELP BUTTON - GROUP HELP BUTTON - GROUP HELP BUTTON -  
        self.find_group_btn = ctk.CTkButton(self.main_frame,
                                     text='Grupos',
                                     command=self.GroupHelp,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.find_group_btn.grid(row=8,column=1,sticky='we',padx=5)
    # BOTONES
        # BOTON AGREGAR
        self.agregar_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Agregar',
                                     command=self.AgregarGrupo,
                                     state='enabled',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.agregar_grupo_btn.grid(row=13,column=2,sticky='we',padx=5,pady=5)
        # BOTON MODIFICAR
        self.modificar_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Modificar',
                                     command=self.ModificarGrupo,
                                     state='disabled',
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.modificar_grupo_btn.grid(row=14,column=2,sticky='we',padx=5,pady=5)
        # BOTON ELIMINAR
        self.eliminar_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Eliminar',
                                     command=self.EliminarGrupo,
                                     state='disabled',
                                     fg_color=APP_COLORS[10],
                                     hover_color=APP_COLORS[10])
        self.eliminar_grupo_btn.grid(row=13,column=3,sticky='we',padx=5,pady=5)
        # BOTON CANCELAR
        self.cancel_grupo_btn_active = True
        self.cancel_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Cancelar',
                                     command=self.LimpiarGrupo,
                                     state='enabled',
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        self.cancel_grupo_btn.grid(row=7,column=3,sticky='we',padx=5,pady=5)
    # BLOQUEO DE LINEAS
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.nombre_entry.configure(state='disabled',fg_color=APP_COLORS[4])
        self.addgrupo_btn.destroy()
# MODO EDICION LINEA
    def ModoEdicion(self):
        # BOTON AGREGAR GRUPO
        if  self.addgrupo_btn_active == False:
            self.addgrupo_btn = ctk.CTkButton(self.main_frame,
                                         text='Agregar-Modificar grupo',
                                         command=self.ModoAgregarGrupo,
                                         state='enabled',
                                         fg_color=APP_COLORS[2],
                                         hover_color=APP_COLORS[3])
            self.addgrupo_btn.grid(row=1,column=3,sticky='we',padx=5,pady=5)
            self.addgrupo_btn_active = True
        self.nombre_entry.unbind("<Return>")
        self.nombre_entry.bind("<Return>",lambda event:self.ModificarLinea())
        # BOTON CANCELAR
        self.cancel_btn = ctk.CTkButton(self.main_frame,
                                     text='Cancelar',
                                     command=self.Restablecer,
                                     state='enabled',
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        self.cancel_btn.grid(row=1,column=4,sticky='we',padx=5,pady=5)
        self.add_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[9])
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.codigo_entry.configure(state='disabled',fg_color=APP_COLORS[4])
# MODO EDICION GRUPO
    def ModoEdicionGrupo(self):
        self.PorV3_entry.unbind("<Return>")
        self.PorV3_entry.bind("<Return>",lambda event:self.ModificarGrupo())
        # ENTRADA
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.codigo_grupo_entry.configure(state='disabled',fg_color=APP_COLORS[4])
        # BOTONES
        self.agregar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modificar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.eliminar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[9])
# LIMPIAR GRUPO
    def LimpiarGrupo(self):
        self.PorV3_entry.unbind("<Return>")
        self.PorV3_entry.bind("<Return>",lambda event:self.AgregarGrupo())
        # BOTONES
        self.codigo_grupo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.agregar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.modificar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.find_group_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        # ENTRADAS
        self.codigo_grupo_entry_var.set('')
        self.grupo_entry_var.set('')
        self.PorV1_entry_var.set('')
        self.PorV2_entry_var.set('')
        self.PorV3_entry_var.set('')
        self.codigo_grupo_entry.focus()
# RESTABLECER LOS CAMPOS DE GRUPO
    def RestablecerGrupo(self):
        # LABELS
        self.titulo_grupo_label.destroy()
        self.codigoGrupo_label.destroy()
        self.nombreGrupo_label.destroy()
        self.pdv1_label.destroy()
        self.pdv2_label.destroy()
        self.pdv3_label.destroy()
        # ENTRADAS
        self.grupo_entry.destroy()
        self.codigo_grupo_entry.destroy()
        self.PorV1_entry.destroy()
        self.PorV2_entry.destroy()
        self.PorV3_entry.destroy()
        self.nombre_entry.configure(state='normal',fg_color=APP_COLORS[6])
        # BOTONES
        self.find_group_btn.destroy()
        self.agregar_grupo_btn.destroy()
        self.modificar_grupo_btn.destroy()
        self.eliminar_grupo_btn.destroy()
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[9])
# RESTABLECER LOS CAMPOS
    def Restablecer(self):
        self.nombre_entry.unbind("<Return>")
        self.nombre_entry.bind("<Return>",lambda event:self.AgregarLinea())
        if self.modo_agregar_grupo_activo == True:
            self.RestablecerGrupo()
            self.modo_agregar_grupo_activo = False
        if self.cancel_grupo_btn_active == True:
            self.cancel_grupo_btn.destroy()
            self.cancel_grupo_btn_active = False
        if self.addgrupo_btn_active == True:
            self.addgrupo_btn.destroy()
            self.addgrupo_btn_active = False
        self.cancel_btn.destroy()
        self.codigo_entry_var.set('')
        self.nombre_entry_var.set('')
        self.add_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[10])
        self.find_line_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.codigo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.codigo_entry.focus()
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# FRAME DEL TREEVIEW
    def LineHelp(self):
        self.line_help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[5])
        self.line_help_frame.geometry('600x400')
        self.line_help_frame.title('Ayuda de lineas')
        self.line_help_frame.transient(self)
    # GRID SETUP
        for rows in range(10):
            self.line_help_frame.rowconfigure(rows, weight=1,uniform='row')
        for columns in range(10):
            self.line_help_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
        title_frame = ctk.CTkFrame(self.line_help_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
        title = ctk.CTkLabel(title_frame,
                             text='Ayuda de líneas',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['text'])
        title.pack(pady=10)   
    # BARRA DE BUSQUEDA
        self.search_line_bar_var = tk.StringVar()
        self.search_line_bar = ctk.CTkEntry(self.line_help_frame,
                                       width=200,
                                       textvariable=self.search_line_bar_var)
        self.search_line_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
        self.search_line_bar.after(100,lambda:self.search_line_bar.focus())
        self.search_line_bar.bind("<Return>",lambda event:self.SearchLine())
        self.search_line_bar.bind("<Control-BackSpace>", lambda event: self.ListLines())
    # BOTONES TREEVIEW
        # BUSCAR
        search_btn = ctk.CTkButton(self.line_help_frame,
                                   text='Buscar',
                                   command=self.SearchLine,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
        # CANCELAR
        cancel_btn = ctk.CTkButton(self.line_help_frame,
                                   text='Cancelar',
                                   command=self.ListLines,
                                   fg_color=APP_COLORS[9],
                                   hover_color=APP_COLORS[10])
        cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
        self.line_help_treeview = ttk.Treeview(self.line_help_frame,
                                     style='Custom.Treeview',
                                     columns=('Linea'))
        self.line_help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
        # EVENTO DE SELECCIONAR PRODUCTO
        self.line_help_treeview.bind("<<TreeviewSelect>>",self.SelectLine)
        # CODIGO
        self.line_help_treeview.heading('#0',text='Codigo')
        self.line_help_treeview.column('#0',width=25,anchor='center')
        # LINEA
        self.line_help_treeview.heading('Linea',text='Linea')
        self.line_help_treeview.column('Linea',width=100,anchor='center')
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
        scrollbar = ctk.CTkScrollbar(self.line_help_frame,
                                     orientation='vertical',
                                     command=self.line_help_treeview.yview)
        scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
        self.line_help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        self.ListLines()
# BUSCAR LINEAS POR NOMBRE
    def SearchLine(self):
        for item in self.line_help_treeview.get_children():
            self.line_help_treeview.delete(item)
        search = self.search_line_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchLineByName(search)
        for line in outcome:
            self.line_help_treeview.insert("", 'end',
                                 text=line['codigo'],
                                 values=(line['linea']))
# LISTAR LINEAS
    def ListLines(self):
        self.search_line_bar.focus()
        self.search_line_bar_var.set('')
        lines = LINE_MANAGER.GetLineNames()
        for item in self.line_help_treeview.get_children():
                self.line_help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.line_help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(line.split(' - ')[1].strip(),),
                                       tags=(tag,))  # Asignar el tag a la fila

        # Configurar colores para los tags
        self.line_help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.line_help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UNA LINEA Y AGREGARLA AL CAMPO DE LINEA
    def SelectLine(self,event):
        item_id = self.line_help_treeview.selection()
        info = self.line_help_treeview.item(item_id)
        self.codigo_entry_var.set(info['text'])
        self.nombre_entry_var.set(info['values'][0])
        self.ModoEdicion()
        self.line_help_frame.destroy()
        self.nombre_entry.after(100,self.nombre_entry.focus())
    def GetLineByCode(self):
        line_search = self.codigo_entry_var.get().strip()
        try:
            line_search = int(line_search)
        except Exception as e:
            messagebox.showerror('Error','Error de entrada en línea')
            self.codigo_entry_var.set('')
            self.nombre_entry_var.set('')
            return
        line = LINE_MANAGER.GetLine(line_search)
        if line:
            self.ModoEdicion()
            self.nombre_entry_var.set(line[1])
            self.nombre_entry.after(100,self.nombre_entry.focus())
        else:
            self.nombre_entry.focus()
            return
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
    def GroupHelp(self):
        try:
            self.current_line = int(self.codigo_entry_var.get().split(' - ')[0].strip())
            if not LINE_MANAGER.CheckLine(self.current_line):
                messagebox.showerror('Error','Seleccione una línea válida.')
                return
            self.help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[5])
            self.help_frame.geometry('600x400')
            self.help_frame.title('Ayuda de Grupos')
            self.help_frame.transient(self)
        # GRID SETUP
            for rows in range(10):
                self.help_frame.rowconfigure(rows, weight=1,uniform='row')
            for columns in range(10):
                self.help_frame.columnconfigure(columns,weight=1,uniform='column')
        # TITULO
            title_frame = ctk.CTkFrame(self.help_frame,corner_radius=0,fg_color=APP_COLORS[3])
            title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
            title = ctk.CTkLabel(title_frame,
                                 text='Ayuda de Grupos',
                                 bg_color='transparent',
                                 text_color=APP_COLORS[0],
                                 height=50,
                                 font=FONT['text'])
            title.pack(pady=10)   
        # BARRA DE BUSQUEDA
            self.search_help_bar_var = tk.StringVar()
            self.search_help_bar = ctk.CTkEntry(self.help_frame,
                                           width=200,
                                           textvariable=self.search_help_bar_var)
            self.search_help_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
            self.search_help_bar.after(100,lambda:self.search_help_bar.focus())
            self.search_help_bar.bind("<Return>",lambda event:self.SearchGroup())
            self.search_help_bar.bind("<Control-BackSpace>", lambda event: self.ListGroups())
        # BOTONES TREEVIEW
            # BUSCAR
            search_btn = ctk.CTkButton(self.help_frame,
                                       text='Buscar',
                                       command=self.SearchGroup,
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3])
            search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
            # CANCELAR
            cancel_btn = ctk.CTkButton(self.help_frame,
                                       text='Cancelar',
                                       command=self.ListGroups,
                                       fg_color=APP_COLORS[9],
                                       hover_color=APP_COLORS[10])
            cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
        # TREEVIEW
            self.help_treeview = ttk.Treeview(self.help_frame,
                                         style='Custom.Treeview',
                                         columns=('Linea','Grupo'))
            self.help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
            # EVENTO DE SELECCIONAR PRODUCTO
            self.help_treeview.bind("<<TreeviewSelect>>",self.SelectGroup)
            # CODIGO
            self.help_treeview.heading('#0',text='Código')
            self.help_treeview.column('#0',width=25,anchor='center')
            # LINEA
            self.help_treeview.heading('Linea',text='Línea')
            self.help_treeview.column('Linea',width=100,anchor='center')
            # GRUPO
            self.help_treeview.heading('Grupo',text='Grupo')
            self.help_treeview.column('Grupo',width=100,anchor='center')
        # CONFIGURACION VISUAL DEL TV
            style = ttk.Style()
            style.configure(
                'Custom.Treeview',
                background = APP_COLORS[0],
                foreground = APP_COLORS[1],
                rowheight = 30,
                fieldbackground = APP_COLORS[0],
                font = FONT['text_small'])
            style.configure(
                'Custom.Treeview.Heading',
                background = APP_COLORS[1],
                foreground = APP_COLORS[1],
                font = FONT['text_light'])
        # SCROLLBAR DEL TV
            scrollbar = ctk.CTkScrollbar(self.help_frame,
                                         orientation='vertical',
                                         command=self.help_treeview.yview)
            scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
            self.help_treeview.configure(yscrollcommand=scrollbar.set)
        # LISTAR LOS PROVEEDORES
            self.ListGroups()
        except ValueError:
            messagebox.showerror('Error','Seleccione una línea válida.')
# BUSCAR PROVEEDORES POR NOMBRE
    def SearchGroup(self):
        for item in self.help_treeview.get_children():
            self.help_treeview.delete(item)
        search = self.search_help_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchGroupByName(search,line=self.current_line)
        for group in outcome:
            self.help_treeview.insert("", 'end',
                                 text=group['codigo'],
                                 values=(group['linea'],
                                         group['grupo']))
# LISTAR PROVEEDORES
    def ListGroups(self):
        self.search_help_bar.focus()
        self.search_help_bar_var.set('')
        lines = LINE_MANAGER.GetGroupNames(self.current_line)
        for item in self.help_treeview.get_children():
                self.help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(self.current_line,
                                                line.split(' - ')[1].strip()),
                                       tags=(tag,))
        self.help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UN PROVEEDOR Y AGREGARLO AL CAMPO DE PROVEEEDOR
    def SelectGroup(self,event):
        item_id = self.help_treeview.selection()
        info = self.help_treeview.item(item_id)
        group = LINE_MANAGER.GetGroup(self.current_line,info['text'])
        self.codigo_grupo_entry_var.set(group[0])
        self.grupo_entry_var.set(group[1])
        self.PorV1_entry_var.set(group[2])
        self.PorV2_entry_var.set(group[3])
        self.PorV3_entry_var.set(group[4])
        self.ModoEdicionGrupo()
        self.help_frame.destroy()
# BUSCAR UN GRUPO EN LA ENTRADA
    def GetGroupByCode(self):
        line_search = self.codigo_entry_var.get()
        if line_search:
            line = LINE_MANAGER.GetLine(int(line_search))
            if not line:
                messagebox.showerror("Error", f"Seleccione una linea válida.")
                return
        else:
            messagebox.showerror("Error", f"Seleccione una linea válida.")
            return
        group_search = self.codigo_grupo_entry_var.get()
        group_code = str(str(line[0]) + '.' + group_search)
        group = LINE_MANAGER.GetGroup(line_search,group_code)
        if group:
            self.codigo_grupo_entry_var.set(group[0])
            self.grupo_entry_var.set(group[1])
            self.PorV1_entry_var.set(group[2])
            self.PorV2_entry_var.set(group[3])
            self.PorV3_entry_var.set(group[4])
            self.ModoEdicionGrupo()
        else:
            self.grupo_entry.focus()
            return
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - 
# VALIDAR LAS CARGAS DE CODIGO 
    def ValidarCodigoLinea(self,texto):
        if len(texto) > 3:
            return False
        if texto == '':
            return True
        return texto.isdigit()
    def ValidarCodigoGrupo(self,texto):
        if len(texto) > 2:
            return False
        if texto == '':
            return True
        return texto.isdigit()
    def ValidarPorcentajes(self,text):
        text = text.replace(".", "", 1)
        if text == '':
            return True
        return text.isdigit()