import tkinter as tk
import customtkinter as ctk
from tkinter import ttk,messagebox
from style import FONT,APP_COLOR,ICONS
from DatabaseManager import USER_MANAGER,GetCurrentUser
from Help_Functions import VerifyOpCode
class GestionUsuariosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.GoBack_CB = GoBack_CB
        self.CurrentUser = GetCurrentUser()
        # -------------------------------------------------------------------------------
        # PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE -
        # -------------------------------------------------------------------------------
        self.title_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['main'],
                        corner_radius=0,)
        self.title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
        self.title_label = ctk.CTkLabel(self.title_frame,
                        text='Gestión de usuarios',
                        text_color=APP_COLOR['black_m'],
                        font=FONT['subtitle_bold'])
        self.title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # -----------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # -------------------------------------------------------------------------------
        # GO BACK BUTTON
        self.go_back_btn = ctk.CTkButton(self,
                text='Volver',
                text_color=APP_COLOR['black_m'],
                font=FONT['text_small'],
                fg_color=APP_COLOR['gray'],
                hover_color=APP_COLOR['main'],
                command=lambda: self.GoBack_CB())
        self.go_back_btn.place(relx=0,rely=0.1,relwidth=0.1,relheight=0.05,anchor='nw')
        # BOTON AGREGAR USUARIO
        self.btn_add_user = ctk.CTkButton(self,
                text='+',
                command=lambda: self.AddUserWindow(0),
                width=40,
                fg_color=APP_COLOR['main'],
                hover_color=APP_COLOR['sec'],
                font=FONT['text_light'])
        self.btn_add_user.place(relx=0.95,y=150,anchor='ne')
        # -------------------------------------------------------------------------------
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW
        # -------------------------------------------------------------------------------
        # CONFIGURACION VISUAL DEL TV
        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 50,
            font = FONT['text'],
            bordercolor=APP_COLOR['black_m'],
            relief="solid",
            fieldbackground = APP_COLOR['white_m'],)
        self.style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['main'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_bold'])
        self.treeview_main = ttk.Treeview(self,
                                    style='Custom.Treeview',
                                    columns=('Nombre','Usuario','Contrasena',
                                             'Cod_Op','Rol','Correo','Estado'))
        self.treeview_main.place(relx=0.5,y=300,relwidth=0.90,height=320,anchor='n')
        self.treeview_main.bind("<<TreeviewSelect>>",self.OnClickTreeView)
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
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # LISTAR USUARIOS - LISTAR USUARIOS - LISTAR USUARIOS - LISTAR USUARIOS -
    # -----------------------------------------------------------------------------------------------
    def ListUsers(self):
        # OBTENER LOS USUARIOS
        usuarios = USER_MANAGER.GetAllUsers()
        # LIMPIAR EL TREEVIEW
        for item in self.treeview_main.get_children():
            self.treeview_main.delete(item)
        # CARGAR LOS USUARIOS AL TREEVIEW
        for i, user in enumerate(usuarios):
            if user['usuario'] == self.CurrentUser:
                continue
            tag = 'Even.Treeview' if i % 2 == 0 else 'Odd.Treeview'
            if not user['estado']:
                tag = 'Incomplete.Treeview'
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
        self.treeview_main.tag_configure('Even.Treeview', background=APP_COLOR['white_m'])
        self.treeview_main.tag_configure('Odd.Treeview', background=APP_COLOR['gray'])
        self.treeview_main.tag_configure('Incomplete.Treeview', background=APP_COLOR['sec'])
    # -----------------------------------------------------------------------------------------------
    # CLICK ON TREEVIEW TO VIEW USER - CLICK ON TREEVIEW TO VIEW USER - CLICK ON TREEVIEW TO VIEW USER -
    # -----------------------------------------------------------------------------------------------
    def OnClickTreeView(self,event):
        selected_item = self.treeview_main.focus()
        if not selected_item:
            return
        user_data = {
            'codigo': self.treeview_main.item(selected_item)['text'],
            'nombre': self.treeview_main.item(selected_item)['values'][0],
            'usuario': self.treeview_main.item(selected_item)['values'][1],
            'opcode': self.treeview_main.item(selected_item)['values'][3],
            'rol': self.treeview_main.item(selected_item)['values'][4],
            'correo': self.treeview_main.item(selected_item)['values'][5],
            'estado': self.treeview_main.item(selected_item)['values'][6],
        }
        user_data = USER_MANAGER.GetUser(user_data['usuario'])
        if not user_data:
            messagebox.showerror("Error", "No se pudo obtener la información del usuario seleccionado.")
            return
        else:
            self.AddUserWindow(1,user_data)
        
    # -----------------------------------------------------------------------------------------------
    # AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO - AGREGAR USUARIO -
    # -----------------------------------------------------------------------------------------------
    def AddUserWindow(self,id,user_data=None):
        # VALIDATE OPCODE
        def ValidateOpcode(text):
            if len(text) > 4:
                return False
            if text == '':
                return True
            return text.isdigit()
        # SHOW PASSWORD
        def ShowPassword():
            if self.SHOW_PASS_COD == 0:  
                result = VerifyOpCode(self)
                if result:
                    password_entry.configure(show='')
                    self.SHOW_PASS_COD = 1
                    return
            password_entry.configure(show='•')
            self.SHOW_PASS_COD = 0
        # AGREGAR USUARIO AL TREEVIEW
        def fill_entries():
            name_entry_var.set(user_data['nombre'])
            user_entry_var.set(user_data['usuario'])
            password_entry_var.set(user_data['clave_nohash'])
            opcode_entry_var.set(str(user_data['opcode']))
            email_entry_var.set(user_data['correo'])
            roles_menu_var.set(user_data['rol'])
        # ADD USER
        def AddUserToDB():
            name = name_entry_var.get().strip()
            user = user_entry_var.get().strip()
            password = password_entry_var.get().strip()
            opcode = str(opcode_entry_var.get().strip())
            email = email_entry_var.get().strip()
            rol = int(roles_menu.get().split(' - ')[0].strip())
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
            user_data = {
                'nombre': name,
                'usuario': user,
                'password': password,
                'opcode': opcode,
                'correo': email,
                'rol': rol,
                'estado': True
            }
            USER_MANAGER.AddUser(user_data)
            add_user_window.destroy()
            self.ListUsers()
        # -------------------------------------------------------------------------------
        # MODIFY USER - MODIFY USER - MODIFY USER - MODIFY USER - MODIFY USER - MODIFY USER - 
        # -------------------------------------------------------------------------------
        def ModUser():
            name = name_entry_var.get().strip()
            user = user_entry_var.get().strip()
            password = password_entry_var.get().strip()
            opcode = str(opcode_entry_var.get().strip())
            email = email_entry_var.get().strip()
            rol = int(roles_menu.get().split(' - ')[0].strip())
            user = USER_MANAGER.GetUser(user)
            estado = True
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
            user_data = {
                'nombre': name,
                'usuario': user['usuario'],
                'password': password,
                'opcode': opcode,
                'correo': email,
                'rol': rol,
                'estado': estado
            }
            USER_MANAGER.UpdateUser(user_data)
            add_user_window.destroy()
            self.ListUsers()
        # -------------------------------------------------------------------------------
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME -
        # -------------------------------------------------------------------------------
        add_user_window = ctk.CTkToplevel(self,
                                   fg_color=APP_COLOR['white_m'])
        add_user_window.geometry('600x350')
        add_user_window.title('Agregar Usuario')
        add_user_window.protocol("WM_DELETE_WINDOW", lambda: None)
        add_user_window.transient(self)
        add_user_window.grab_set()
        add_user_frame = ctk.CTkFrame(add_user_window,
                                corner_radius=0)
        add_user_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # VARIABLES
        self.SHOW_PASS_COD = 0
        # -------------------------------------------------------------------------------
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # -------------------------------------------------------------------------------
        # FRAME TITLE
        title_frame = ctk.CTkFrame(add_user_frame,
                fg_color=APP_COLOR['main'],
                corner_radius=0)
        title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.12,anchor='n')
        # LABEL TITLE
        title_label = ctk.CTkLabel(title_frame,
                text='Agregar Usuario',
                bg_color='transparent',
                text_color=APP_COLOR['black_m'],
                font=FONT['text_bold'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
        # -------------------------------------------------------------------------------
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS -
        # -------------------------------------------------------------------------------
        # NOMBRE
        name_entry_var = tk.StringVar()
        name_entry = ctk.CTkEntry(add_user_frame,
                textvariable=name_entry_var,
                border_color=APP_COLOR['white'])
        name_entry.place(relx=0.325, rely=0.20, relwidth=0.35,anchor='w')
        name_entry.bind("<Return>", lambda event: user_entry.focus())
        name_entry.focus()
        # USUARIO
        user_entry_var = tk.StringVar()
        user_entry = ctk.CTkEntry(add_user_frame,
                textvariable=user_entry_var,
                border_color=APP_COLOR['white'])
        user_entry.place(relx=0.325, rely=0.30, relwidth=0.35,anchor='w')
        user_entry.bind("<Return>", lambda event: password_entry.focus())
        # CONTRASEÑA
        password_entry_var = tk.StringVar()
        password_entry = ctk.CTkEntry(add_user_frame,
                textvariable=password_entry_var,
                show = '•',
                border_color=APP_COLOR['white'])
        password_entry.place(relx=0.325, rely=0.40, relwidth=0.35,anchor='w')
        password_entry.bind("<Return>", lambda event: opcode_entry.focus())
        # CODIGO DE OPERACION
        validate_opcode = self.register(ValidateOpcode)
        opcode_entry_var = tk.StringVar()
        opcode_entry = ctk.CTkEntry(add_user_frame,
                textvariable=opcode_entry_var,
                validate = 'key',
                validatecommand=(validate_opcode,'%P'),
                border_color=APP_COLOR['white'])
        opcode_entry.place(relx=0.325, rely=0.50, relwidth=0.35,anchor='w')
        opcode_entry.bind("<Return>", lambda event: email_entry.focus())
        # CORREO
        email_entry_var = tk.StringVar()
        email_entry = ctk.CTkEntry(add_user_frame,
                textvariable=email_entry_var,
                border_color=APP_COLOR['white'])
        email_entry.place(relx=0.325, rely=0.60, relwidth=0.35,anchor='w')
        email_entry.bind("<Return>", lambda event: AddUserToDB())
        # -------------------------------------------------------------------------------
        # OPTION MENU ROLES
        # -------------------------------------------------------------------------------
        roles = USER_MANAGER.GetRoles()
        roles.pop()
        roles_menu_var = tk.StringVar()
        roles_menu = ctk.CTkComboBox(add_user_frame,
                state='readonly',
                values=roles,
                variable=roles_menu_var,
                fg_color=APP_COLOR['main'],
                border_color=APP_COLOR['main'],
                button_color=APP_COLOR['sec'],
                button_hover_color=APP_COLOR['main'],
                dropdown_fg_color=APP_COLOR['black_m'],
                dropdown_hover_color=APP_COLOR['gray'],
                text_color=APP_COLOR['black_m'],
                font=FONT['text_small'])
        roles_menu.place(relx=0.325,rely=0.70,relwidth=0.35,anchor='w')
        # -------------------------------------------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # -------------------------------------------------------------------------------
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
        # -------------------------------------------------------------------------------
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # -------------------------------------------------------------------------------
        # EXIT
        exit_button = ctk.CTkButton(add_user_frame,
                text='',
                image= ICONS['cancel'],
                command=add_user_window.destroy,
                width=40,
                fg_color=APP_COLOR['red_m'],
                hover_color=APP_COLOR['red_s'])
        exit_button.place(relx=0.98,rely=0.15,anchor='ne')
        # SHOW PASSWORD
        show_pass_button = ctk.CTkButton(add_user_frame,
                text='',
                image= ICONS['eye'],
                command=ShowPassword,
                width=40,
                fg_color=APP_COLOR['main'],
                hover_color=APP_COLOR['sec'])
        show_pass_button.place(relx=0.70,rely=0.40,anchor='w')
        # SAVE 
        save_button = ctk.CTkButton(add_user_frame,
                text='Guardar',
                command=AddUserToDB,
                fg_color=APP_COLOR['main'],
                text_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['sec'])
        save_button.place(relx=0.325, rely=0.85,anchor='w')
        # -------------------------------------------------------------------------------
        # SET UP FILL ENTRIES IF ID IS PROVIDED TO ACTIVATE USER
        # -------------------------------------------------------------------------------
        if id == 1:
            # CHANGE TITLES TO MODIFY USER
            add_user_window.title('Modificar usuario')
            title_label.configure(text='Modificar Usuario')
            user_entry.configure(state='disabled')
            save_button.configure(command=ModUser)
            email_entry.unbind("<Return>")
            email_entry.bind("<Return>", lambda event: ModUser())
            # FILL ENTRIES
            fill_entries()
