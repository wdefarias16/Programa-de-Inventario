import tkinter as tk
import customtkinter as ctk
from tkinter import ttk,messagebox
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
                                    command=self.AddUserWindow,
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
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO -
    # AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO -
    # AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO -
    def AddUserWindow(self):
        def AddUser():
            name = name_entry_var.get().strip()
            user = user_entry_var.get().strip()
            password = password_entry_var.get().strip()
            opcode = opcode_entry_var.get().strip()
            email = email_entry_var.get().strip()
            rol = role_entry_var.get().strip()
            if not name:
                messagebox.showerror("Error", "El campo 'Nombre' no puede estar vacío.")
                name_entry.focus()
                return
            if not user:
                messagebox.showerror("Error", "El campo 'Usuario' no puede estar vacío.")
                user_entry.focus()
                return
            if not password:
                messagebox.showerror("Error", "El campo 'Contraseña' no puede estar vacío.")
                password_entry.focus()
                return
            if not opcode:
                messagebox.showerror("Error", "El campo 'Cod. Op.' no puede estar vacío.")
                opcode_entry.focus()
                return
            if not rol:
                messagebox.showerror("Error", "Seleccione un rol de usuario.")
                return
            try:
                opcode = int(opcode)
            except ValueError:
                messagebox.showerror("Error", "El campo 'Cod. Op.' debe ser uicamente numérico.")
                opcode_entry_var.set('')
                opcode_entry.focus()
                return
            USER_MANAGER.AddUser(name, user, password, opcode, email, rol)
            messagebox.showinfo("Base de datos", "Usuario agregado exitosamente.")
            add_user_window.destroy()
            self.ListUsers()
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
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS -
        # NOMBRE
        name_entry_var = tk.StringVar()
        name_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=name_entry_var,
                                  width=220,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        name_entry.place(relx=0.5,rely=0.20,anchor='center')
        name_entry.bind("<Return>", lambda event: user_entry.focus())
        name_entry.focus()
        # USUARIO
        user_entry_var = tk.StringVar()
        user_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=user_entry_var,
                                  width=220,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        user_entry.place(relx=0.5,rely=0.30,anchor='center')
        user_entry.bind("<Return>", lambda event: password_entry.focus())
        # CONTRASEÑA
        password_entry_var = tk.StringVar()
        password_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=password_entry_var,
                                  width=220,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        password_entry.place(relx=0.5,rely=0.40,anchor='center')
        password_entry.bind("<Return>", lambda event: opcode_entry.focus())
        # CODIGO DE OPERACION
        opcode_entry_var = tk.StringVar()
        opcode_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=opcode_entry_var,
                                  width=220,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        opcode_entry.place(relx=0.5,rely=0.50,anchor='center')
        opcode_entry.bind("<Return>", lambda event: email_entry.focus())
        # CORREO
        email_entry_var = tk.StringVar()
        email_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=email_entry_var,
                                  width=220,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        email_entry.place(relx=0.5,rely=0.60,anchor='center')
        email_entry.bind("<Return>", lambda event: AddUser())
        # ROL
        role_entry_var = tk.StringVar()
        role_entry = ctk.CTkEntry(add_user_frame,
                                  textvariable=role_entry_var,
                                  state='disabled',
                                  width=63,
                                  height=20,
                                  fg_color=APP_COLOR['white'],
                                  border_color=APP_COLOR['white'])
        role_entry.place(relx=0.58,rely=0.70,anchor='w')
        # -----------------------------------------------
        # -----------------------------------------------
        # OPTION MENU ROLES
        # OPTION MENU ROLES
        roles_menu = ctk.CTkOptionMenu(add_user_frame,
                                        values=USER_MANAGER.GetRoles(),
                                        command=lambda opcion: role_entry_var.set(opcion.split(" - ")[0]),
                                        width=145,
                                        height=22,
                                        fg_color=APP_COLOR['main'],
                                        button_color=APP_COLOR['sec'],
                                        button_hover_color=APP_COLOR['main'],
                                        dropdown_fg_color=APP_COLOR['white_m'],
                                        dropdown_hover_color=APP_COLOR['gray'],
                                        text_color=APP_COLOR['white'],
                                        font=FONT['text_small'])
        roles_menu.place(relx=0.32,rely=0.70,anchor='w')
        # -----------------------------------------------
        # -----------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # NOMBRE
        name_label = ctk.CTkLabel(add_user_frame,
                                  text='Nombre:',
                                  text_color=APP_COLOR['gray'],
                                  font=FONT['text'])
        name_label.place(relx=0.30,rely=0.20,anchor='e')
        # USUARIO
        user_label = ctk.CTkLabel(add_user_frame,
                                  text='Usuario:',
                                  text_color=APP_COLOR['gray'],
                                  font=FONT['text'])
        user_label.place(relx=0.30,rely=0.30,anchor='e')
        # CONTRASEÑA
        password_label = ctk.CTkLabel(add_user_frame,
                                  text='Contraseña:',
                                  text_color=APP_COLOR['gray'],
                                  font=FONT['text'])
        password_label.place(relx=0.30,rely=0.40,anchor='e')
        # CODIGO DE OPERACION
        opcode_label = ctk.CTkLabel(add_user_frame,
                                  text='Cod. Op.:',
                                  text_color=APP_COLOR['gray'],
                                  font=FONT['text'])
        opcode_label.place(relx=0.30,rely=0.50,anchor='e')
        # CORREO
        email_label = ctk.CTkLabel(add_user_frame,
                                  text='Correo:',
                                  text_color=APP_COLOR['gray'],
                                  font=FONT['text'])
        email_label.place(relx=0.30,rely=0.60,anchor='e')
        # ROL
        role_label = ctk.CTkLabel(add_user_frame,
                                    text='Rol:',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'])
        role_label.place(relx=0.30,rely=0.70,anchor='e')
        
        # -----------------------------------------------
        # -----------------------------------------------
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
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
