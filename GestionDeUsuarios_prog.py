import customtkinter as ctk
from tkinter import ttk
from style import FONT,APP_COLOR
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
    def ListUsers(self):
        # OBTENER LOS USUARIOS
        usuarios = USER_MANAGER.GetAllUsers()
        # LIMPIAR EL TREEVIEW
        for item in self.treeview_main.get_children():
            self.treeview_main.delete(item)
        # CARGAR LOS USUARIOS AL TREEVIEW
        for i, user in enumerate(usuarios.values()):
            tag = "Even.Treview" if i % 2 == 0 else "Odd.Treview"
            self.treeview_main.insert(
                "",'end',
                text=str(user['codigo']),
                values=(
                    user['nombre'],
                    user['usuario'],
                    user['clave'],
                    user['opcode'],
                    user['rol'],
                    user['correo'],
                    user['estado']),
                    tag=(tag,))
        self.treeview_main.tag_configure('Odd.Treeview', background="#ffffff")
        self.treeview_main.tag_configure('Even.Treeview', background="#eaeaea")
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------