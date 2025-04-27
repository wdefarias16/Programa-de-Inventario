import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json,os
from style import FONTS, APP_COLORS, APPEARANCE_MODE
from Database import LINE_MANAGER

# PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS
class LineasGruposProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.nombre_grupo = ''
        self.GoBack_CB = GoBack_CB
    # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de líneas y grupos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
        title.pack(pady=5)
    # LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS - LINEAS
    # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME -  
        lines_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        lines_frame.pack(expand=True,fill='both',side='left')
    # GRID CONFIG
        for rows in range(5):
            lines_frame.rowconfigure(rows, weight=1)
        for columns in range(4):
            lines_frame.columnconfigure(columns,weight=1)
    #  LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
    # TITULO DE LINEA
        label_lin = ctk.CTkLabel(lines_frame,
                                 text='Líneas',
                                 corner_radius=5,
                                 fg_color=APP_COLORS[4],
                                 text_color=APP_COLORS[0],
                                 font=FONTS[0])
        label_lin.grid(row=0,column=0,columnspan=3,sticky='nwe',pady=20,padx=5)
    # LABEL BUSCADOR DE LINEAS
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Buscador de líneas',font=FONTS[1])
        label_lin_cod.grid(row=1,column=0,sticky='n',padx=5)
    # LABEL CODIGO DE LINEA
        label_lin_cod = ctk.CTkLabel(lines_frame,text='Código de línea',font=FONTS[1])
        label_lin_cod.grid(row=1,column=2,sticky='sw',padx=5)
    # LABEL NOMBRE DE LINEA
        label_lin_nom = ctk.CTkLabel(lines_frame,text='Nombre de línea',font=FONTS[1])
        label_lin_nom.grid(row=2,column=2,sticky='nw',padx=5)
    # MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - 
        self.lin_menu = ctk.CTkOptionMenu(lines_frame,
                                          command=self.SelectLinea,
                                          values=LINE_MANAGER.GetLineNames())
        self.lin_menu.grid(row=1,column=0,sticky='swe',pady=5)
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
    # ENTRADA CODIGO DE LINEAS
        self.codigo_lin_var = tk.StringVar()
        self.lin_entry = ctk.CTkEntry(lines_frame,
                                 textvariable=self.codigo_lin_var)
        self.lin_entry.grid(row=1,column=1,sticky='swe',pady=5)
    # ENTRADA NOMBRE DE LINEA
        self.nombre_lin_var = tk.StringVar()
        lin_entry_nom = ctk.CTkEntry(lines_frame,
                                     textvariable=self.nombre_lin_var)
        lin_entry_nom.grid(row=2,column=1,sticky='nwe')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
    # AGREGAR GRUPO
        self.addl_btn = ctk.CTkButton(lines_frame,
                                      command=self.AgregarLinea,
                                      fg_color=APP_COLORS[2],
                                      hover_color=APP_COLORS[3],
                                      state='enabled',
                                      text='Agregar',font=FONTS[1])
        self.addl_btn.grid(row=3,column=0,columnspan=4,sticky='nswe',padx=5,pady=5)
    # MODIFICAR
        self.modl_btn = ctk.CTkButton(lines_frame,
                                 command=self.ModificarLinea,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Modificar',font=FONTS[1])
        self.modl_btn.grid(row=4,column=0,columnspan=1,sticky='nsew',padx=5,pady=5)
    # ELIMINAR
        self.dell_btn = ctk.CTkButton(lines_frame,
                                 command=self.EliminarLinea,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Eliminar',font=FONTS[1])
        self.dell_btn.grid(row=4,column=1,columnspan=1,sticky='nsew',padx=5,pady=5)
    # CANCELAR
        self.cancel_btn = ctk.CTkButton(lines_frame,
                                 command=self.Restablecer,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Cancelar',font=FONTS[1])
        self.cancel_btn.grid(row=4,column=2,columnspan=2,sticky='nsew',padx=5,pady=5)
    # GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS - GRUPOS -
    # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME -
        group_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        group_frame.pack(expand=True,fill='both',side='left')
    # GRID CONFIG
        for rows in range(5):
            group_frame.rowconfigure(rows, weight=1)
        for columns in range(4):
            group_frame.columnconfigure(columns,weight=1)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
    # TITULO DE GRUPO
        label_grupo = ctk.CTkLabel(group_frame,
                                 text='Grupos',
                                 corner_radius=5,
                                 fg_color=APP_COLORS[4],
                                 text_color=APP_COLORS[0],
                                 font=FONTS[0])
        label_grupo.grid(row=0,column=0,columnspan=3,sticky='nwe',pady=20,padx=5)
    # LABEL CODIGO DE LINEA
        label_grup_nom = ctk.CTkLabel(group_frame,text='Línea',font=FONTS[1])
        label_grup_nom.grid(row=1,column=2,sticky='sw',pady=5,padx=5)
    # LABEL NOMBRE DE GRUPO
        label_grup_nom = ctk.CTkLabel(group_frame,text='Nombre de grupo',font=FONTS[1])
        label_grup_nom.grid(row=2,column=2,sticky='nw',padx=5)
    # MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU - MENU -
        self.lineas = LINE_MANAGER.GetLineNames()
        self.codigoActualLinea = self.lineas[0].split(" - ")[0]
        self.grup_menu = ctk.CTkOptionMenu(group_frame,
                                           command=self.SelectGrupo,
                                           values=LINE_MANAGER.GetGroupNames(self.codigoActualLinea))
        self.grup_menu.grid(row=1,column=0,sticky='swe',pady=5)
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS -
    # ENTRADA DE LINEA
        lin_grup_entry = ctk.CTkEntry(group_frame,
                                      state='disabled',
                                      fg_color=APP_COLORS[7],
                                      textvariable=self.codigo_lin_var)
        lin_grup_entry.grid(row=1,column=1,sticky='swe',pady=5)
    # ENTRADA DE GRUPO
        self.nombre_grupo_var = tk.StringVar()
        grup_entry = ctk.CTkEntry(group_frame,textvariable=self.nombre_grupo_var)
        grup_entry.grid(row=2,column=1,sticky='nwe')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
    # AGREGAR GRUPO
        self.addg_btn = ctk.CTkButton(group_frame,
                                 command=self.AgregarGrupo,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Agregar',font=FONTS[1])
        self.addg_btn.grid(row=3,column=0,columnspan=4,sticky='nswe',padx=10,pady=5)
    # MODIFICAR
        self.modg_btn = ctk.CTkButton(group_frame,
                                 command=self.ModificarGrupo,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Modificar',font=FONTS[1])
        self.modg_btn.grid(row=4,column=0,columnspan=2,sticky='nsew',padx=10,pady=5)
    # ELIMINAR
        self.delg_btn = ctk.CTkButton(group_frame,
                                 command=self.EliminarGrupo,
                                 state='disabled',
                                 fg_color=APP_COLORS[3],
                                 hover_color=APP_COLORS[3],
                                 text='Eliminar',font=FONTS[1])
        self.delg_btn.grid(row=4,column=2,columnspan=2,sticky='nsew',padx=10,pady=5)
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - 
# COMANDO BOTON AGREGAR LINEA
    def AgregarLinea(self):
    # OBTENER VALORES DE ENTRADA
        codigo = self.codigo_lin_var.get()
        nombre = self.nombre_lin_var.get()
    # CHEQUEAR VALORES
        if not codigo or not nombre:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        if LINE_MANAGER.Add_Line(codigo,nombre):
            nuevas_lineas = LINE_MANAGER.GetLineNames()
            self.lin_menu.configure(values=nuevas_lineas)
        else:
            messagebox.showerror('Error','No se pudo agregar la linea')
# COMANDO MODIFICAR LINEA
    def ModificarLinea(self):
        codigo = self.codigo_lin_var.get()
        linea = self.nombre_lin_var.get()
        LINE_MANAGER.Mod_Linea(codigo,linea)
        self.lin_menu.configure(values=LINE_MANAGER.GetLineNames())
        self.Restablecer()
# COMANDO ELIMINAR LINEA
    def EliminarLinea(self):
        codigo = self.codigo_lin_var.get()
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea eliminar la linea {codigo}?'
                                     '\nEsto Eliminará tambien todos sus grupos.')
        if answer:
            LINE_MANAGER.Del_Linea(codigo)
            self.lin_menu.configure(values=LINE_MANAGER.GetLineNames())
            self.Restablecer()


# AL SELECCIONAR LINEA
    def SelectLinea(self,opcion):
        codigo = opcion.split(' - ')[0]
        self.codigo_lin_var.set(opcion.split(' - ')[0])
        self.nombre_lin_var.set(opcion.split(' - ')[1])
        nuevos_grupos = LINE_MANAGER.GetGroupNames(codigo)
        self.grup_menu.configure(values=nuevos_grupos)
    # MODO EDICION
        # LINEAS
        self.addl_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modl_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.dell_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.cancel_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.lin_entry.configure(state='disabled',fg_color=APP_COLORS[7])
        # GRUPOS
        self.addg_btn.configure(state='enabled',fg_color=APP_COLORS[2],hover_color=APP_COLORS[3])
        self.modg_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.delg_btn.configure(state='enabled',fg_color=APP_COLORS[2])
# AL SELECCIONAR GRUPO
    def SelectGrupo(self,opcion):
        self.nombre_grupo = opcion
        self.nombre_grupo_var.set(opcion)
# COMANDO BOTON AGREGAR GRUPO
    def AgregarGrupo(self):
    # OBTENER VALORES DE ENTRADA
        codigo = self.codigo_lin_var.get()
        grupo = self.nombre_grupo_var.get()
    # CHEQUEAR VALORES
        if not codigo or not grupo:
            messagebox.showerror('Error','Debe ingresar un codigo y nombre validos')
            return
        LINE_MANAGER.Add_Group(codigo,grupo)
        nuevos_grupos = LINE_MANAGER.GetGroupNames(codigo)
        self.grup_menu.configure(values=nuevos_grupos)
# COMANDO MODIFICAR GRUPO
    def ModificarGrupo(self):
        codigo = self.codigo_lin_var.get()
        nuevo_grupo = self.nombre_grupo_var.get()
        antiguo_grupo = self.nombre_grupo
        if not nuevo_grupo:
            messagebox.showerror('Error','Debe ingresar un grupo valido')
        else:
            LINE_MANAGER.Mod_Grupo(codigo,nuevo_grupo,antiguo_grupo)
            nuevos_grupos = LINE_MANAGER.GetGroupNames(codigo)
            self.grup_menu.configure(values=nuevos_grupos)
            self.nombre_grupo_var.set('')
# COMANDO ELIMINAR GRUPO
    def EliminarGrupo(self):
        codigo = self.codigo_lin_var.get()
        grupo = self.nombre_grupo_var.get()
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea eliminar el grupo {grupo}?')
        if answer:
            LINE_MANAGER.Eliminar_Grupo(codigo,grupo)
            nuevos_grupos = LINE_MANAGER.GetGroupNames(codigo)
            self.grup_menu.configure(values=nuevos_grupos)
            self.nombre_grupo_var.set('')
# RESTABLECER A MODO AGREGAR LINEA
    def Restablecer(self):
        # LINEAS
        self.lin_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.addl_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.modl_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.dell_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.cancel_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.codigo_lin_var.set('')
        self.nombre_lin_var.set('')
        # GRUPOS
        self.addg_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.modg_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.delg_btn.configure(state='disaled',fg_color=APP_COLORS[3])
        self.nombre_grupo_var.set('')
