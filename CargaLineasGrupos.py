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
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0])
        self.modo_agregar_grupo_activo = False
        self.cancel_grupo_btn_active = False
        # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(title_frame,
                             text='Carga de líneas y grupos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[0])
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
        # NOMBRE - DESCRIPCION
        self.nombre_entry_var = tk.StringVar()
        self.nombre_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.nombre_entry_var,
                                         fg_color=APP_COLORS[6])
        self.nombre_entry.grid(row=3,column=2,columnspan=2,sticky='we',padx=5)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # TITULO LINEAS
        self.titulo_line = ctk.CTkLabel(self.main_frame,
                                        text='Cargar una línea',
                                        font=FONTS[1])
        self.titulo_line.grid(row=1,column=2,sticky='w')
        # CODIGO
        codigo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de línea',
                                    font=FONTS[1])
        codigo_label.grid(row=2,column=4,columnspan=2,sticky='w')
        # NOMBRE - DESCRIPCION
        descrip_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONTS[1])
        descrip_label.grid(row=3,column=4,columnspan=2,sticky='w')
    # OPTION MENU - OPTION MENU - OPTION MENU - OPTION MENU - OPTION MENU - OPTION MENU - OPTION MENU - 
        self.line_menu = ctk.CTkOptionMenu(self.main_frame,
                                           command=self.ClickOnMenu,
                                           values=LINE_MANAGER.GetLineNames())
        self.line_menu.grid(row=2,column=1,sticky='we')
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
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.del_btn.grid(row=5,column=3,sticky='we',padx=5,pady=5)
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
                self.line_menu.configure(values=LINE_MANAGER.GetLineNames())
                self.Restablecer()
    # ELIMINAR LINEA
    def EliminarLinea(self):
        codigo = self.codigo_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar la línea {codigo}?'
                                     '\nEsto Eliminará tambien todos sus grupos.')
        if answer:
            LINE_MANAGER.Del_Linea(codigo)
            self.line_menu.configure(values=LINE_MANAGER.GetLineNames())
            self.Restablecer()
    # MODIFICAR LINEA
    def ModificarLinea(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea modificar la línea {codigo}?')
        if answer:
            LINE_MANAGER.Mod_Linea(codigo,nombre)
            self.line_menu.configure(values=LINE_MANAGER.GetLineNames())
            self.Restablecer()
# FUNCIONES DE GRUPO
    # AGREGAR GRUPO
    def AgregarGrupo(self):
        codigo = self.codigo_entry_var.get()
        codigo_grupo = self.codigo_grupo_entry_var.get()
        nombre_grupo = self.grupo_entry_var.get()
        p1 = self.PorV1_entry_var.get()
        p2 = self.PorV2_entry_var.get()
        p3 = self.PorV3_entry_var.get()
        if codigo_grupo == '' or nombre_grupo == '':
            messagebox.showerror('Error de carga','Debe rellenar todos los campos')
        elif p1 <= 0 or p2 <= 0 or p3 <= 0:
            messagebox.showerror('Error de carga','Debe cargar los porcentajes.'
                                 '\nNinguno puede ser menor o igual a 0')
        else:
            LINE_MANAGER.Add_Group(codigo,codigo_grupo,nombre_grupo,p1,p2,p3)
        self.grupos_menu.configure(values=LINE_MANAGER.GetGroupNames(codigo))
        self.LimpiarGrupo()
    # MODIFICAR GRUPO
    def ModificarGrupo(self):
        linea = self.codigo_entry_var.get()
        grupo = self.codigo_grupo_entry_var.get()
        nombre_grupo = self.grupo_entry_var.get()
        p1 = self.PorV1_entry_var.get()
        p2 = self.PorV2_entry_var.get()
        p3 = self.PorV3_entry_var.get()
        LINE_MANAGER.Mod_Grupo(linea,grupo,nombre_grupo,p1,p2,p3)
        self.grupos_menu.configure(values=LINE_MANAGER.GetGroupNames(linea))
        self.LimpiarGrupo()
    # ELIMINAR GRUPO
    def EliminarGrupo(self):
        linea = self.codigo_entry_var.get()
        grupo = self.codigo_grupo_entry_var.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar el grupo {grupo}?')
        if answer:
            LINE_MANAGER.Del_Group(linea,grupo)
        self.grupos_menu.configure(values=LINE_MANAGER.GetGroupNames(linea))
        self.LimpiarGrupo()

# CLICK MENU
    def ClickOnMenu(self,opcion):
        self.ModoEdicion()
        self.codigo_entry_var.set(opcion.split(' - ')[0])
        self.nombre_entry_var.set(opcion.split(' - ')[1])
    def ClickOnMenuGrupo(self,opcion):
        self.ModoEdicionGrupo()
        linea = self.codigo_entry_var.get()
        grupo = opcion.split(' - ')[0]
        porcentajes = LINE_MANAGER.GetPorcentajes(linea,grupo)
        self.codigo_grupo_entry_var.set(opcion.split(' - ')[0])
        self.grupo_entry_var.set(opcion.split(' - ')[1])
        self.PorV1_entry_var.set(porcentajes['porcentaje1'])
        self.PorV2_entry_var.set(porcentajes['porcentaje2'])
        self.PorV3_entry_var.set(porcentajes['porcentaje3'])
# MODO AGREGAR GRUPO
    def ModoAgregarGrupo(self):
        self.modo_agregar_grupo_activo = True
        self.addgrupo_btn.destroy()
        # TITULO CARGA GRUPO
        self.titulo_grupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Carga de grupo',
                                    font=FONTS[1])
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
        # ENTRADA DESCRIPCION
        self.grupo_entry_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.grupo_entry_var,
                                         fg_color=APP_COLORS[6])
        self.grupo_entry.grid(row=9,column=2,columnspan=2,sticky='we',padx=5)
        # PORCENTAJE 1
        self.PorV1_entry_var = tk.DoubleVar()
        self.PorV1_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.PorV1_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV1_entry.grid(row=10,column=2,columnspan=2,sticky='we',padx=5)
        # PORCENTAJE 2
        self.PorV2_entry_var = tk.DoubleVar()
        self.PorV2_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.PorV2_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV2_entry.grid(row=11,column=2,columnspan=2,sticky='we',padx=5)
        # PORCENTAJE 3
        self.PorV3_entry_var = tk.DoubleVar()
        self.PorV3_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.PorV3_entry_var,
                                         fg_color=APP_COLORS[6])
        self.PorV3_entry.grid(row=12,column=2,columnspan=2,sticky='we',padx=5)
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # CODIGO
        self.codigoGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de grupo',
                                    font=FONTS[1])
        self.codigoGrupo_label.grid(row=8,column=4,columnspan=2,sticky='w')
        # DESCRIPCION
        self.nombreGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONTS[1])
        self.nombreGrupo_label.grid(row=9,column=4,columnspan=2,sticky='w')
        # PDV1
        self.pdv1_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 1',
                                    font=FONTS[1])
        self.pdv1_label.grid(row=10,column=4,columnspan=2,sticky='w')
        # PDV2
        self.pdv2_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 2',
                                    font=FONTS[1])
        self.pdv2_label.grid(row=11,column=4,columnspan=2,sticky='w')
        # PDV3
        self.pdv3_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 3',
                                    font=FONTS[1])
        self.pdv3_label.grid(row=12,column=4,columnspan=2,sticky='w')
    # MENU DE GRUPOS
        self.grupos_menu = ctk.CTkOptionMenu(self.main_frame,
                                           command=self.ClickOnMenuGrupo,
                                           values=LINE_MANAGER.GetGroupNames(self.codigo_entry.get()))
        self.grupos_menu.grid(row=8,column=1,sticky='we')
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
                                     fg_color=APP_COLORS[3],
                                     hover_color=APP_COLORS[3])
        self.eliminar_grupo_btn.grid(row=14,column=3,sticky='we',padx=5,pady=5)
    # BLOQUEO DE LINEAS
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.nombre_entry.configure(state='disabled',fg_color=APP_COLORS[4])
        self.line_menu.configure(state='disabled')
        self.addgrupo_btn.destroy()
# MODO EDICION LINEA
    def ModoEdicion(self):
        # BOTON CANCELAR
        self.cancel_btn = ctk.CTkButton(self.main_frame,
                                     text='Cancelar',
                                     command=self.Restablecer,
                                     state='enabled',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.cancel_btn.grid(row=4,column=3,sticky='we',padx=5,pady=5)
        # BOTON AGREGAR GRUPO
        self.addgrupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Agregar grupo',
                                     command=self.ModoAgregarGrupo,
                                     state='enabled',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.addgrupo_btn.grid(row=1,column=3,sticky='we',padx=5,pady=5)
        self.add_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.codigo_entry.configure(state='disabled',fg_color=APP_COLORS[4])
# MODO EDICION GRUPO
    def ModoEdicionGrupo(self):
        # ENTRADA
        self.codigo_grupo_entry.configure(state='disabled',fg_color=APP_COLORS[4])
        # BOTON CANCELAR
        self.cancel_grupo_btn_active = True
        self.cancel_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Cancelar',
                                     command=self.LimpiarGrupo,
                                     state='enabled',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3])
        self.cancel_grupo_btn.grid(row=13,column=3,sticky='we',padx=5,pady=5)
        # BOTONES
        self.agregar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.modificar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.eliminar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        

# LIMPIAR GRUPO
    def LimpiarGrupo(self):
        self.cancel_grupo_btn.destroy()
        self.codigo_grupo_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.agregar_grupo_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.modificar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.eliminar_grupo_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.codigo_grupo_entry_var.set('')
        self.grupo_entry_var.set('')
        self.PorV1_entry_var.set(0.0)
        self.PorV2_entry_var.set(0.0)
        self.PorV3_entry_var.set(0.0)

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
        # MENU
        self.grupos_menu.destroy()
        # BOTONES
        self.agregar_grupo_btn.destroy()
        self.modificar_grupo_btn.destroy()
        self.eliminar_grupo_btn.destroy()
        self.mod_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.del_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.nombre_entry.configure(state='normal',fg_color=APP_COLORS[6])
        self.line_menu.configure(state='enabled')
# RESTABLECER LOS CAMPOS
    def Restablecer(self):
        if self.modo_agregar_grupo_activo == True:
            self.RestablecerGrupo()
            self.modo_agregar_grupo_activo = False
        if self.cancel_grupo_btn_active == True:
            self.cancel_grupo_btn.destroy()
            self.cancel_grupo_btn_active = False
        self.cancel_btn.destroy()
        self.addgrupo_btn.destroy()
        self.codigo_entry_var.set('')
        self.nombre_entry_var.set('')
        self.add_btn.configure(state='enabled',fg_color=APP_COLORS[2])
        self.mod_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.del_btn.configure(state='disabled',fg_color=APP_COLORS[3])
        self.codigo_entry.configure(state='normal',fg_color=APP_COLORS[6])

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