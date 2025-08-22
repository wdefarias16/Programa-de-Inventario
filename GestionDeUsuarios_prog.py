import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from style import FONT,APP_COLOR,ICONS
from DatabaseManager import USER_MANAGER

class GestionUsuariosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color = APP_COLOR['white_m'])
        self.GoBack_CB = GoBack_CB
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   height=70,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.place(relx=0.5,rely=0,relwidth=1,anchor='n')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Gestión de usuarios',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # BOTON ATRAS
        self.btn_back = ctk.CTkButton(self,
                                    text='Volver Atrás',
                                    command=self.GoBack_CB,
                                    width=40,
                                    fg_color=APP_COLOR['gray'],
                                    hover_color=APP_COLOR['sec'],
                                    font=FONT['text_light'])
        self.btn_back.place(relx=0.01,rely=0.11,anchor='nw')
        # BOTON AGREGAR USUARIO
        self.btn_add_user = ctk.CTkButton(self,
                                    text='+',
                                    command=self.AddUser,
                                    width=40,
                                    fg_color=APP_COLOR['main'],
                                    hover_color=APP_COLOR['sec'],
                                    font=FONT['text_light'])
        self.btn_add_user.place(relx=0.95,y=150,anchor='ne')


        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 40,
            font = FONT['text_light'],
            fieldbackground = APP_COLOR['gray'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_light'])
        self.treeview_main = ttk.Treeview(self,
                                    style='Custom.Treeview',
                                    columns=('Nombre','Usuario','Contrasena',
                                             'Cod_Op','Rol','Correo','Estado'))
        self.treeview_main.place(relx=0.5,y=300,relwidth=0.90,height=320,anchor='n')
        # CODIGO
        self.treeview_main.heading('#0',text='Cod.')
        self.treeview_main.column('#0', width=100, anchor='center', minwidth=30, stretch=False)
        # NOMBRE
        self.treeview_main.heading('Nombre',text='Nombre')
        self.treeview_main.column('Nombre', width=300, anchor='center', stretch=False)
        # USUARIO
        self.treeview_main.heading('Usuario',text='Usuario')
        self.treeview_main.column('Usuario', width=100, anchor='w', stretch=True)
        # CONTRASEÑA
        self.treeview_main.heading('Contrasena',text='Contraseña')
        self.treeview_main.column('Contrasena', width=100, anchor='w', stretch=True)
        # CODIGO DE OPERACION
        self.treeview_main.heading('Cod_Op',text='Cod. Op')
        self.treeview_main.column('Cod_Op', width=100, anchor='center', stretch=False)
        # ROL
        self.treeview_main.heading('Rol',text='Rol')
        self.treeview_main.column('Rol', width=100, anchor='center', stretch=False)
        # CORREO
        self.treeview_main.heading('Correo',text='Correo')
        self.treeview_main.column('Correo', width=300, anchor='w', stretch=False)
        # ESTADO
        self.treeview_main.heading('Estado',text='Estado')
        self.treeview_main.column('Estado', width=100, anchor='center', stretch=False)
        # LISTAR EL TREEVIEW
        self.ListUsers()
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # LISTAR USUARIOS - LISTAR USUARIOS - LISTAR USUARIOS - LISTAR USUARIOS -
    def ListUsers(self):
        # OBTENER LOS USUARIOS
        usuarios = USER_MANAGER.GetAllUsers()
        # LIMPIAR EL TREEVIEW
        for item in self.treeview_main.get_children():
            self.treeview_main.delete(item)
        # CARGAR LOS USUARIOS AL TREEVIEW
        for i, user in enumerate(usuarios):
            tag = "Even.Treview" if i % 2 == 0 else "Odd.Treview"
            self.treeview_main.insert(
                "",'end',
                text=str(user['codigo']),
                values=(
                    user['nombre'],
                    user['usuario'],
                    '•••••••••',
                    user['opcode'],
                    user['rol'],
                    user['correo'],
                    user['estado']),
                    tag=(tag,))
        self.treeview_main.tag_configure('Odd.Treeview', background="#ffffff")
        self.treeview_main.tag_configure('Even.Treeview', background="#eaeaea")
    # AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO -
    def AddUser(self):
        
        # ---------------------------------------------- 
        # ---------------------------------------------- 
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME -
        add_user_window = ctk.CTkToplevel(self,
                                   fg_color=APP_COLOR['white_m'])
        add_user_window.geometry('600x350')
        add_user_window.title('Agregar Usuario')
        add_user_window.protocol("WM_DELETE_WINDOW", lambda: None)
        add_user_window.transient(self)
        add_user_window.grab_set()
        add_user_frame = ctk.CTkFrame(add_user_window,
                                corner_radius=0,
                                fg_color=APP_COLOR['white_m'])
        add_user_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # FRAME TITLE
        title_frame = ctk.CTkFrame(add_user_frame,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.10,anchor='n')
        # LABEL TITLE
        title_label = ctk.CTkLabel(title_frame,
                                   text='Agregar Usuario',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['subtitle_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS -
        # NOMBRE
        name_entry_var = tk.StringVar()
        name_entry = ctk.CTkEntry(add_user_frame,
                                  placeholder_text='Nombre',
                                  textvariable=name_entry_var,
                                  width=300,
                                  height=40,
                                  font=FONT['text_light'],
                                  fg_color=APP_COLOR['white_m'],
                                  border_color=APP_COLOR['gray'])
        name_entry.place(relx=0.5,rely=0.15,anchor='n')
        # USUARIO
        user_entry_var = tk.StringVar()
        user_entry = ctk.CTkEntry(add_user_frame,
                                  placeholder_text='Usuario',
                                  textvariable=user_entry_var,
                                  width=300,
                                  height=40,
                                  font=FONT['text_light'],
                                  fg_color=APP_COLOR['white_m'],
                                  border_color=APP_COLOR['gray'])
        user_entry.place(relx=0.5,rely=0.25,anchor='n')
        # CONTRASEÑA
        password_entry_var = tk.StringVar()
        password_entry = ctk.CTkEntry(add_user_frame,
                                      placeholder_text='Contraseña',
                                      textvariable=password_entry_var,
                                      width=300,
                                      height=40,
                                      font=FONT['text_light'],
                                      fg_color=APP_COLOR['white_m'],
                                      border_color=APP_COLOR['gray'],
                                      show='*')
        password_entry.place(relx=0.5,rely=0.35,anchor='n')
        # CODIGO DE OPERACION
        cod_op_entry_var = tk.StringVar()
        cod_op_entry = ctk.CTkEntry(add_user_frame,
                                    placeholder_text='Código de Operación',
                                    textvariable=cod_op_entry_var,
                                    width=300,
                                    height=40,
                                    font=FONT['text_light'],
                                    fg_color=APP_COLOR['white_m'],
                                    border_color=APP_COLOR['gray'])
        cod_op_entry.place(relx=0.5,rely=0.45,anchor='n')
        # CORREO
        email_entry_var = tk.StringVar()
        email_entry = ctk.CTkEntry(add_user_frame,
                                   placeholder_text='Correo Electrónico',
                                   textvariable=email_entry_var,
                                   width=300,
                                   height=40,
                                   font=FONT['text_light'],
                                   fg_color=APP_COLOR['white_m'],
                                   border_color=APP_COLOR['gray'])
        email_entry.place(relx=0.5,rely=0.55,anchor='n')
        # ROL
        role_entry_var = tk.StringVar()
        role_entry = ctk.CTkOptionMenu(add_user_frame,
                                       variable=role_entry_var,
                                       values=['Administrador', 'Usuario'],
                                       width=300,
                                       height=40,
                                       font=FONT['text_light'],
                                       fg_color=APP_COLOR['white_m'],
                                       border_color=APP_COLOR['gray'])
        role_entry.place(relx=0.5,rely=0.65,anchor='n')
       
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # EXIT
        exit_button = ctk.CTkButton(add_user_frame,
                                    text='',
                                    image= ICONS['cancel'],
                                    command=add_user_window.destroy,
                                    width=40,
                                    fg_color=APP_COLOR['red_m'],
                                    hover_color=APP_COLOR['red_s'])
        exit_button.place(relx=0.98,rely=0.12,anchor='ne')

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------