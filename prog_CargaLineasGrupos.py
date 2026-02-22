import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from style import *
from DatabaseManager import LINE_MANAGER
from Help_Funcs_LinesGroups import Lines_Help_Window,Groups_Help_Window
from Help_Functions import ValidateAmount

# PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS - PROGRAMA DE CARGA DE LINEAS Y GRUPOS
class LineasGruposProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLOR['white_m'])
        self.modo_agregar_grupo_activo = False
        self.cancel_grupo_btn_active = False
        self.addgrupo_btn_active = False
        "Verificacion de ventanas de ayuda activas"
        self.Lines_Help_Window_active = False
        self.Groups_Help_Window_active = False
    # ---------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE
    # ---------------------------------------------------------------------
        # FRAME
        title_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['sec'],
                        corner_radius=0,)
        title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
        title_label = ctk.CTkLabel(title_frame,
                        text='Carga de líneas y grupos',
                        text_color=APP_COLOR['white_m'],
                        font=FONT['title_bold'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
        home_btn = ctk.CTkButton(title_frame,
                        image=ICONS['home'],
                        text='',
                        width=30,
                        height=30,
                        fg_color=APP_COLOR['gray'],
                        hover_color=APP_COLOR['black_m'])
        home_btn.place(relx=0.05,rely=0.5,anchor='center')
        # GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON -
        self.go_back_btn = ctk.CTkButton(title_frame,
                text='',
                image=ICONS['home'],
                width=30,
                height=30,
                text_color=APP_COLOR['black_m'],
                font=FONT['text_small'],
                fg_color=APP_COLOR['gray'],
                hover_color=APP_COLOR['main'],
                command=lambda: self.GoBack_CB())
        self.go_back_btn.place(relx=0.1,rely=0.5,anchor='center')
        # ------------------------------------------------------------------------
        "Iniciar la configuracion inicial"
        self.SetInicio()
# ------------------------------------------------------------------------
# FUNCION PARA ESTABLECER LA CONFIGURACION INICIAL
# ------------------------------------------------------------------------
    def SetInicio(self):
    # ---------------------------------------------------------------------
    # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME
    # ---------------------------------------------------------------------
        self.main_frame = ctk.CTkFrame(self,fg_color=APP_COLOR['white_m'])
        self.main_frame.place(relx=0.5,rely=0.1,relwidth=1,relheight=1,anchor='n')

    # ---------------------------------------------------------------------
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS -
    # ---------------------------------------------------------------------
        # CODIGO
        validarlinea = self.register(self.ValidarCodigoLinea)  
        self.codigo_linea_entry_var = tk.StringVar()
        self.codigo_linea_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validarlinea,'%P'),
                                         textvariable=self.codigo_linea_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.codigo_linea_entry.place(relx=0.4,rely=0.2,relwidth=0.05,anchor='w')
        self.codigo_linea_entry.bind("<Return>", lambda event: self.GetLineByCode())
        self.codigo_linea_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.codigo_linea_entry.bind("<Control-s>",lambda event: self.LineHelp())
        self.codigo_linea_entry.bind("<Control-S>",lambda event: self.LineHelp())
        self.codigo_linea_entry.focus()
        # NOMBRE - DESCRIPCION
        self.nombre_linea_entry_var = tk.StringVar()
        self.nombre_linea_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.nombre_linea_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.nombre_linea_entry.place(relx=0.4,rely=0.25,relwidth=0.2,anchor='w')
        self.nombre_linea_entry.bind("<Return>", lambda event: self.AgregarLinea())
        self.nombre_linea_entry.bind("<Control-Return>", lambda event: self.ModoAgregarGrupo())
        self.nombre_linea_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
    # ---------------------------------------------------------------------
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS
    # ---------------------------------------------------------------------
        # TITULO LINEAS
        self.titulo_line = ctk.CTkLabel(self.main_frame,
                                        text='Cargar / Modificar una línea',
                                        font=FONT['text_light'])
        self.titulo_line.place(relx=0.4,rely=0.15,anchor='w')
        # CODIGO
        codigo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de línea',
                                    font=FONT['text_light'])
        codigo_label.place(relx=0.39,rely=0.2,anchor='e')
        # NOMBRE - DESCRIPCION
        descrip_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONT['text_light'])
        descrip_label.place(relx=0.39,rely=0.25,anchor='e')
    # ---------------------------------------------------------------------
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -
    # ---------------------------------------------------------------------
        # LINE HELP BUTTON
        self.find_line_btn = ctk.CTkButton(self.main_frame,
                                     text='',
                                     image=ICONS['search'],
                                     width=30,
                                     height=30,
                                     command=self.Lines_Help_Window_CB,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'])
        self.find_line_btn.place(relx=0.46,rely=0.2,anchor='w')
        # AGREGAR
        self.add_btn = ctk.CTkButton(self.main_frame,
                                     text='Agregar',
                                     command=self.AgregarLinea,
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.add_btn.place(relx=0.4,rely=0.30,relwidth=0.095,anchor='w')
        # ELIMINAR
        self.del_btn = ctk.CTkButton(self.main_frame,
                                     text='Eliminar',
                                     command=self.EliminarLinea,
                                     state='disabled',
                                     fg_color=APP_COLOR['red_m'],
                                     hover_color=APP_COLOR['red_s'])
        self.del_btn.place(relx=0.6,rely=0.30,relwidth=0.095,anchor='e')
# -------------------------------------------------------------------------
# FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES - FUNCIONES -
# -------------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # AGREGAR LINEA - AGREGAR LINEA - AGREGAR LINEA - AGREGAR LINEA - 
    # ---------------------------------------------------------------------
    def AgregarLinea(self):
        codigo = self.codigo_linea_entry.get()
        nombre = self.nombre_linea_entry.get()
        if codigo == '' or nombre == '':
            messagebox.showerror('Error','Debe rellenar los campos')
            return
        answer = messagebox.showinfo('Líneas y grupos',f'¿Está seguro que desea agregar la línea {nombre}?')
        if answer:
            if LINE_MANAGER.Add_Line(codigo,nombre):
                self.Restablecer()
    # ---------------------------------------------------------------------
    # ELIMINAR LINEA - ELIMINAR LINEA - ELIMINAR LINEA - ELIMINAR LINEA - 
    # ---------------------------------------------------------------------
    def EliminarLinea(self):
        codigo = self.codigo_linea_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar la línea {codigo}?'
                                     '\nEsto Eliminará tambien todos sus grupos.')
        if answer:
            LINE_MANAGER.Del_Linea(codigo)
            self.Restablecer()
    # ---------------------------------------------------------------------
    # MODIFICAR LINEA - MODIFICAR LINEA - MODIFICAR LINEA - MODIFICAR LINEA
    # ---------------------------------------------------------------------
    def ModificarLinea(self):
        codigo = self.codigo_linea_entry.get()
        nombre = self.nombre_linea_entry.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea modificar la línea {codigo}?')
        if answer:
            LINE_MANAGER.Mod_Linea(codigo,nombre)
            self.Restablecer()
    # ---------------------------------------------------------------------
    # AGREGAR GRUPO - AGREGAR GRUPO - AGREGAR GRUPO - AGREGAR GRUPO - 
    # ---------------------------------------------------------------------
    def AgregarGrupo(self):
        codigo = self.codigo_linea_entry_var.get()
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
        self.Clear_Group_Entry_Fields()
        self.codigo_grupo_entry.focus()
    # ---------------------------------------------------------------------
    # MODIFICAR GRUPO - MODIFICAR GRUPO - MODIFICAR GRUPO - MODIFICAR GRUPO
    # ---------------------------------------------------------------------
    def ModificarGrupo(self):
        linea = self.codigo_linea_entry_var.get()
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
        self.Clear_Group_Entry_Fields()
    # ---------------------------------------------------------------------
    # ELIMINAR GRUPO - ELIMINAR GRUPO - ELIMINAR GRUPO - ELIMINAR GRUPO
    # ---------------------------------------------------------------------
    def EliminarGrupo(self):
        linea = self.codigo_linea_entry_var.get()
        grupo = self.codigo_grupo_entry_var.get()
        answer = messagebox.askyesno('¡Atención!',f'Está seguro que desea eliminar el grupo {grupo}?')
        if answer:
            LINE_MANAGER.Del_Group(linea,grupo)
        self.Clear_Group_Entry_Fields()
    # ---------------------------------------------------------------------
    # MODO AGREGAR GRUPO - ELIMINAR GRUPO - MODO AGREGAR GRUPO -
    # ---------------------------------------------------------------------
    def ModoAgregarGrupo(self):
        self.current_line = LINE_MANAGER.CheckLine(self.codigo_linea_entry_var.get())
        if not self.current_line:
            messagebox.showerror('Error','Seleccione una línea válida.')
            return
        self.modo_agregar_grupo_activo = True
        self.addgrupo_btn.destroy()
        # CONFIGURACION DE BOTONES Y ENTRADAS DE LINEA
        self.nombre_linea_entry.configure(fg_color=APP_COLOR['gray'],border_color=APP_COLOR['gray'],
                                          state='disabled')
        self.add_btn.configure(state='disabled',fg_color=APP_COLOR['sec'])
        self.del_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
        # TITULO CARGA GRUPO
        self.titulo_grupo_label.place(relx=0.4,rely=0.4,anchor='w')
        self.titulo_grupo_label.configure(text='Cargar / Modificar un grupo')
        # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # ENTRADA CODIGO GRUPO
        validargrupo = self.register(self.ValidarCodigoGrupo)
        self.codigo_grupo_entry_var = tk.StringVar()
        self.codigo_grupo_entry = ctk.CTkEntry(self.main_frame,
                                        validate = 'key',
                                        validatecommand = (validargrupo,'%P'),
                                        textvariable=self.codigo_grupo_entry_var,
                                        fg_color=APP_COLOR['light_gray'],
                                        border_color=APP_COLOR['light_gray'])
        self.codigo_grupo_entry.place(relx=0.4,rely=0.45,relwidth=0.05,anchor='w')
        self.codigo_grupo_entry.bind("<Return>", lambda event: self.GetGroupByCode())
        self.codigo_grupo_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.codigo_grupo_entry.bind("<Control-BackSpace>",lambda event: self.Clear_Group_Entry_Fields())
        self.codigo_grupo_entry.bind("<Control-s>",lambda event: self.GroupHelp())
        self.codigo_grupo_entry.bind("<Control-S>",lambda event: self.GroupHelp())
        self.codigo_grupo_entry.focus()
        # ENTRADA DESCRIPCION
        self.grupo_entry_var = tk.StringVar()
        self.grupo_entry = ctk.CTkEntry(self.main_frame,
                                         textvariable=self.grupo_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.grupo_entry.place(relx=0.4,rely=0.50,relwidth=0.2,anchor='w')
        self.grupo_entry.bind("<Return>",lambda event: self.PorV1_entry.focus())
        self.grupo_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.grupo_entry.bind("<Control-BackSpace>",lambda event: self.Clear_Group_Entry_Fields())
        # PORCENTAJE 1
        validar_pctj = self.register(ValidateAmount)
        self.PorV1_entry_var = tk.StringVar()
        self.PorV1_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV1_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.PorV1_entry.place(relx=0.4,rely=0.55,relwidth=0.05,anchor='w')
        self.PorV1_entry.bind("<Return>",lambda event: self.PorV2_entry.focus())
        self.PorV1_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV1_entry.bind("<Control-BackSpace>",lambda event: self.Clear_Group_Entry_Fields())
        # PORCENTAJE 2
        self.PorV2_entry_var = tk.StringVar()
        self.PorV2_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV2_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.PorV2_entry.place(relx=0.4,rely=0.6,relwidth=0.05,anchor='w')
        self.PorV2_entry.bind("<Return>",lambda event: self.PorV3_entry.focus())
        self.PorV2_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV2_entry.bind("<Control-BackSpace>",lambda event: self.Clear_Group_Entry_Fields())
        # PORCENTAJE 3
        self.PorV3_entry_var = tk.StringVar()
        self.PorV3_entry = ctk.CTkEntry(self.main_frame,
                                         validate = 'key',
                                         validatecommand = (validar_pctj,'%P'),
                                         textvariable=self.PorV3_entry_var,
                                         fg_color=APP_COLOR['light_gray'],
                                         border_color=APP_COLOR['light_gray'])
        self.PorV3_entry.place(relx=0.4,rely=0.65,relwidth=0.05,anchor='w')
        self.PorV3_entry.bind("<Return>",lambda event: self.AgregarGrupo())
        self.PorV3_entry.bind("<Control-Alt-BackSpace>",lambda event: self.Restablecer())
        self.PorV3_entry.bind("<Control-BackSpace>",lambda event: self.Clear_Group_Entry_Fields())
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # CODIGO
        self.codigoGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Código de grupo',
                                    font=FONT['text_light'])
        self.codigoGrupo_label.place(relx=0.39,rely=0.45,anchor='e')
        # DESCRIPCION
        self.nombreGrupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Descripción',
                                    font=FONT['text_light'])
        self.nombreGrupo_label.place(relx=0.39,rely=0.5,anchor='e')
        # PDV1
        self.pdv1_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 1',
                                    font=FONT['text_light'])
        self.pdv1_label.place(relx=0.39,rely=0.55,anchor='e')
        # PDV2
        self.pdv2_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 2',
                                    font=FONT['text_light'])
        self.pdv2_label.place(relx=0.39,rely=0.6,anchor='e')
        # PDV3
        self.pdv3_label = ctk.CTkLabel(self.main_frame,
                                    text='% Porcentaje de venta 3',
                                    font=FONT['text_light'])
        self.pdv3_label.place(relx=0.39,rely=0.65,anchor='e')
        # BOTONES
        # GROUP HELP BUTTON - GROUP HELP BUTTON - GROUP HELP BUTTON - GROUP HELP BUTTON -  
        # LINE HELP BUTTON
        self.find_group_btn = ctk.CTkButton(self.main_frame,
                                     text='',
                                     image=ICONS['search'],
                                     width=30,
                                     height=30,
                                     command=self.Groups_Help_Window_CB,
                                     fg_color=APP_COLOR['black_m'],
                                     hover_color=APP_COLOR['black'])
        self.find_group_btn.place(relx=0.46,rely=0.45,anchor='w')
        # BOTON AGREGAR
        self.agregar_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Agregar',
                                     command=self.AgregarGrupo,
                                     state='enabled',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.agregar_grupo_btn.place(relx=0.4,rely=0.70,relwidth=0.095,anchor='w')
        # BOTON ELIMINAR
        self.eliminar_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='Eliminar',
                                     command=self.EliminarGrupo,
                                     state='disabled',
                                     fg_color=APP_COLOR['red_s'],
                                     hover_color=APP_COLOR['red_s'])
        self.eliminar_grupo_btn.place(relx=0.6,rely=0.70,relwidth=0.095,anchor='e')
        # BOTON CANCELAR
        self.cancel_grupo_btn_active = True
        self.cancel_grupo_btn = ctk.CTkButton(self.main_frame,
                                     text='',
                                     image=ICONS['refresh'],
                                     width=30,
                                     height=30,
                                     command=self.Clear_Group_Entry_Fields,
                                     state='enabled',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.cancel_grupo_btn.place(relx=0.50,rely=0.45,anchor='w')
    # ---------------------------------------------------------------------
    # MODO EDICION LINEA - MODO EDICION LINEA - MODO EDICION LINEA - 
    # ---------------------------------------------------------------------
    def Modo_Edicion_lineas(self):
        "Boton 'agregar' pasa a llamarse 'modificar'"
        self.add_btn.configure(text='Modificar',command=self.ModificarLinea)
        self.del_btn.configure(state='disabled',fg_color=APP_COLOR['red_s'])
        self.codigo_linea_entry.configure(state='disabled',)
        "Boton y label agregar grupo"
        self.titulo_grupo_label = ctk.CTkLabel(self.main_frame,
                                    text='Cargar / Modificar un grupo',
                                    font=FONT['text_light'])
        self.titulo_grupo_label.place(relx=0.43,rely=0.4,anchor='w')
        self.nombre_linea_entry.unbind("<Return>")
        self.nombre_linea_entry.bind("<Return>",lambda event:self.ModificarLinea())
        "Evitar que el boton grupo active la funcion varias veces"
        if  self.addgrupo_btn_active == False:
            self.addgrupo_btn = ctk.CTkButton(self.main_frame,
                                         text='+',
                                         width=30,
                                         height=30,
                                         command=self.ModoAgregarGrupo,
                                         state='enabled',
                                         fg_color=APP_COLOR['main'],
                                         hover_color=APP_COLOR['sec'])
            self.addgrupo_btn.place(relx=0.4,rely=0.4,anchor='w')
            self.addgrupo_btn_active = True
        "Crear boton refrescar para volver a la configuracion inicial"
        self.cancel_btn = ctk.CTkButton(self.main_frame,
                                     text='',
                                     image=ICONS['refresh'],
                                     width=30,
                                     height=30,
                                     command=self.Restablecer,
                                     state='enabled',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'])
        self.cancel_btn.place(relx=0.50,rely=0.2,anchor='w')
        "Bloqueo y configuracion de botones"
        self.del_btn.configure(state='enabled',fg_color=APP_COLOR['red_m'])
        self.codigo_linea_entry.configure(state='disabled',fg_color=APP_COLOR['gray'],
                                     border_color=APP_COLOR['gray'])
    # ----------------------------------------------------------------
    # LIMPIAR LOS CAMPOS DE GRUPO - LIMPIAR LOS CAMPOS DE GRUPO - LIMP
    # ----------------------------------------------------------------
    def Clear_Group_Entry_Fields(self):
        self.codigo_grupo_entry_var.set('')
        self.grupo_entry_var.set('')
        self.PorV1_entry_var.set('')
        self.PorV2_entry_var.set('')
        self.PorV3_entry_var.set('')
        "Desactivar modo edicion"
        self.PorV3_entry.unbind("<Return>")
        self.PorV3_entry.bind("<Return>",lambda event:self.AgregarGrupo())
        # ENTRADA
        self.find_line_btn.configure(state='enabled',fg_color=APP_COLOR['black_m'])
        self.codigo_grupo_entry.configure(state='normal',fg_color=APP_COLOR['light_gray'],
                                                border_color=APP_COLOR['light_gray'])
        self.codigo_grupo_entry.focus()
        # BOTONES
        self.agregar_grupo_btn.configure(text='Agregar',command = self.ModificarGrupo)
        self.eliminar_grupo_btn.configure(state='enabled',fg_color=APP_COLOR['red_m'])
    # ----------------------------------------------------------------
    # LLENAR LOS CAMPOS DE GRUPO - LLENAR LOS CAMPOS DE GRUPO - LLENAR
    # ----------------------------------------------------------------
    def Fill_Group_Entry_Fields(self,group):
        self.codigo_grupo_entry_var.set(group['codigo'])
        self.grupo_entry_var.set(group['nombre'])
        self.PorV1_entry_var.set(group['precio1'])
        self.PorV2_entry_var.set(group['precio2'])
        self.PorV3_entry_var.set(group['precio3'])
        "Activar modo edicion"
        self.PorV3_entry.unbind("<Return>")
        self.PorV3_entry.bind("<Return>",lambda event:self.ModificarGrupo())
        # ENTRADA
        self.find_line_btn.configure(state='disabled',fg_color=APP_COLOR['black'])
        self.codigo_grupo_entry.configure(state='disabled',fg_color=APP_COLOR['gray'],
                                                border_color=APP_COLOR['gray'])
        self.grupo_entry.focus()
        # BOTONES
        self.agregar_grupo_btn.configure(text='Modificar',command = self.ModificarGrupo)
        self.eliminar_grupo_btn.configure(state='enabled',fg_color=APP_COLOR['red_m'])
    # RESTABLECER LOS CAMPOS
    def Restablecer(self):
        self.main_frame.destroy()
        self.addgrupo_btn_active = False
        self.SetInicio()
    # ----------------------------------------------------------------
    # LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE
    # ----------------------------------------------------------------
    # FRAME DEL TREEVIEW
    def Lines_Help_Window_CB(self):
        "Evitar que se abra la ventana varias veces"
        if self.Lines_Help_Window_active:
            return
        "Si la ventana no esta abierta la abre"
        self.Lines_Help_Window_active = True
        line = Lines_Help_Window(self)
        if not line:
            self.Lines_Help_Window_active = False
            self.Restablecer()
            return
        "Al seleccionar la linea, rellena los campos"
        self.codigo_linea_entry_var.set(line['codigo'])
        self.nombre_linea_entry_var.set(line['nombre'])
        "Activa el modo edicion de linea"
        self.Modo_Edicion_lineas()
        "Permite abrir la ventana de nuevo despues de cerrarla"
        self.Lines_Help_Window_active = False
    # ----------------------------------------------------------------
    # GET LINE BY ID CODE - GET LINE BY ID CODE - GET LINE BY ID CODE
    # ----------------------------------------------------------------
    def GetLineByCode(self):
        line_search = self.codigo_linea_entry_var.get().strip()
        try:
            line_search = int(line_search)
        except Exception as e:
            messagebox.showerror('Error','Error de entrada en línea')
            self.codigo_linea_entry_var.set('')
            self.nombre_linea_entry_var.set('')
            return
        if not LINE_MANAGER.CheckLine(line_search):
            self.nombre_linea_entry.focus()
            return
        line = LINE_MANAGER.GetLine(line_search)
        self.Modo_Edicion_lineas()
        self.nombre_linea_entry_var.set(line['nombre'])
        self.nombre_linea_entry.after(100,self.nombre_linea_entry.focus())
    # ----------------------------------------------------------------
    # GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP - GROUP HELP -
    # ----------------------------------------------------------------
    def Groups_Help_Window_CB(self):
        "Evitar que se abra la ventana varias veces"
        if self.Groups_Help_Window_active:
            return
        "Si la ventana no esta abierta la abre"
        self.Groups_Help_Window_active = True
        current_line = int(self.codigo_linea_entry_var.get())
        group = Groups_Help_Window(self,current_line)
        "Si no se selecciona un grupo vacia los campos"
        if not group:
            self.Groups_Help_Window_active = False
            self.Clear_Group_Entry_Fields()
            return
        self.Fill_Group_Entry_Fields(group)
        self.Groups_Help_Window_active = False
    # ----------------------------------------------------------------
    # BUSCAR UN GRUPO EN LA ENTRADA
    # ----------------------------------------------------------------
    def GetGroupByCode(self):
        line_search = self.codigo_linea_entry_var.get()
        line = LINE_MANAGER.GetLine(int(line_search))

        group_search = self.codigo_grupo_entry_var.get()
        group_code = f'{line['codigo']}.{group_search}'
        group = LINE_MANAGER.GetGroup(line_search,group_code)
        if group:
            self.Fill_Group_Entry_Fields(group)
        else:
            self.grupo_entry.focus()
            return
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