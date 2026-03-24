# CREAR FRAME LOGIN
import customtkinter as ctk
import tkinter as tk
from style import *
from DatabaseManager import USER_MANAGER, LoginUser
from tkinter import messagebox

# LOGIN FRAME
class Login(ctk.CTkFrame):
    def __init__(self,parent,success_callback,exit_callback):
        super().__init__(parent,bg_color=APP_COLOR['white_m'])
        self.success_callback = success_callback  
        self.exit = exit_callback
        self.PASSWORD_SHOW = False
        self.PASSWORD_CONFIRM_SHOW = False
        self.Login()
    # ----------------------------------------------------------------------------
    # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - 
    # ----------------------------------------------------------------------------
    def Login(self):
    # ----------------------------------------------------------------------------
    # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME -
    # ----------------------------------------------------------------------------
        self.login_frame = ctk.CTkFrame(self,
                                corner_radius=0)
        self.login_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')
    # ----------------------------------------------------------------------------
    # LOGO FRAME - LOGO FRAME - LOGO FRAME - LOGO FRAME - LOGO FRAME - LOGO FRAME - LOGO FRAME -
    # ----------------------------------------------------------------------------
        logo = LogoLabel (self.login_frame,version=5,ancho_deseado=120)
        logo.place(relx=0.5, rely=0.1, relwidth = 0.30, anchor='n')
    # ----------------------------------------------------------------------------
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
    # ----------------------------------------------------------------------------
        # ENTRADA USUARIO
        self.user_var = tk.StringVar()
        self.login_entry = ctk.CTkEntry(self.login_frame,placeholder_text='Usuario',
                                height=30,
                                fg_color=APP_COLOR['light_gray'],
                                text_color=APP_COLOR['black_m'],
                                textvariable=self.user_var,
                                corner_radius=5,
                                border_color=APP_COLOR['light_gray'])
        self.login_entry.place(relx=0.5, rely=0.35, relwidth = 0.30, anchor='center')
        self.login_entry.bind("<Control-a>",self.AdminUser)
        self.login_entry.bind("<Return>",lambda event: self.password_entry.focus())
        # INICIAR EL PROGRAMA CON LA ENTRADA DE USUARIO ACTIVA
        self.login_entry.after(100, lambda: self.login_entry.focus_set())
        # ENTRADA CONTRASENA
        self.password_var = tk.StringVar()
        self.password_entry = ctk.CTkEntry(self.login_frame,placeholder_text='Contraseña',
                                width=30,
                                fg_color=APP_COLOR['light_gray'],
                                text_color=APP_COLOR['black_m'],
                                textvariable=self.password_var,
                                corner_radius=5,
                                show='•',
                                border_color=APP_COLOR['light_gray'])
        self.password_entry.place(relx=0.5, rely=0.45, relwidth = 0.30, anchor='center')
        self.password_entry.bind("<Return>",lambda event:self.Access())
    # ----------------------------------------------------------------------------
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
    # ----------------------------------------------------------------------------
        # MENSAJE BIENVENIDO
        #label_wc = ctk.CTkLabel(self.login_frame,
        #                        text='Bienvenido',
        #                        font=FONT['title_light'],
        #                        text_color=APP_COLOR['black_m'])
        #label_wc.place(relx=0.5, rely=15, anchor='center')
        # USUARIO
        user_label = ctk.CTkLabel(self.login_frame,
                                text='Usuario',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray_s'])
        user_label.place(relx=0.35, rely=0.30, anchor='w')
        # CONTRASENA
        password_label = ctk.CTkLabel(self.login_frame,
                                text='Contraseña',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray_s'])
        password_label.place(relx=0.35, rely=0.40, anchor='w')
        # MENSAJE INFERIOR
        self.Y_pos_label = 0.70
        self.label_var = tk.StringVar(value='Ingresa tus credenciales')
        self.label_access = ctk.CTkLabel(self.login_frame,
                                textvariable=self.label_var,
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray_s'])
        self.label_access.place(relx=0.5, rely=self.Y_pos_label, anchor='center')
    # ----------------------------------------------------------------------------
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -  
    # ----------------------------------------------------------------------------
        # BOTON ENTRAR
        self.Y_pos = 0.53
        self.enter_button = ctk.CTkButton(self.login_frame,
                                text='Entrar',
                                text_color=APP_COLOR['white_m'],
                                height=35,
                                fg_color=APP_COLOR['sec'],
                                hover_color=APP_COLOR['sec_s'],
                                command=self.Access)
        self.enter_button.place(relx=0.35, rely=self.Y_pos, relwidth=0.13,anchor='w')
        # BOTON REGISTRAR
        self.register_button = ctk.CTkButton(self.login_frame,
                                text='Registrarse',
                                text_color=APP_COLOR['white_m'],
                                height=35,
                                fg_color=APP_COLOR['sec'],
                                hover_color=APP_COLOR['sec_s'],
                                command=self.ButtonAnimated)
        self.register_button.place(relx=0.65, rely=self.Y_pos, relwidth=0.13,anchor='e')
        # BOTON SHOW PASSWORD
        self.show_password_button = ctk.CTkButton(self.login_frame,
                                text='',
                                text_color=APP_COLOR['black_m'],
                                height=35,
                                width=30,
                                image=ICONS['eye'],
                                fg_color=APP_COLOR['sec'],
                                hover_color=APP_COLOR['sec_s'],
                                command=lambda : self.ShowPassword(1))
        self.show_password_button.place(relx=0.66, rely=0.45,anchor='w')
        # BOTON SALIR
        exit_button = ctk.CTkButton(self.login_frame,
                                text='',
                                width=30,
                                height=30,
                                image=ICONS['exit'],
                                text_color=APP_COLOR['black_m'],
                                fg_color=APP_COLOR['sec'],
                                hover_color=APP_COLOR['sec_s'],
                                command=self.exit)
        exit_button.place(relx=0.92, rely=0.05,anchor='nw')
    # --------------------------------------------------------------------------
    # ACCESO DEL LOGIN
    # --------------------------------------------------------------------------
    def Access(self):
        user = self.user_var.get()
        password = self.password_var.get()
        user_confirm = USER_MANAGER.GetUser(user)
        
        if USER_MANAGER.Access(user,password):
            if user_confirm['rol'] == 5:
                messagebox.showinfo('Usuarios','Su usuario debe ser activado por un administrador para poder acceder al sistema.')
                self.RestoreLogin()
                return
            user_data = USER_MANAGER.GetUser(user)
            CURRENT_USER = user_data['usuario']
            self.label_var.set(f'Bienvenido {CURRENT_USER}')
            LoginUser(user_data)
            user_state = True
            USER_MANAGER.ChangeUserStatus(CURRENT_USER,user_state)
            self.after(500,self.success_callback)
        else:
            self.label_var.set('Acceso denegado')
    # --------------------------------------------------------------------------
    # AGREGAR USUARIO
    # --------------------------------------------------------------------------    
    def AddUser(self):
        user = self.user_var.get()
        password = self.password_var.get()
        if USER_MANAGER.AddUser(user,password):
            self.label_var.set('Usuario agregado')
    # --------------------------------------------------------------------------
    # MOVER BOTONES ABAJO
    # --------------------------------------------------------------------------
    def ButtonAnimated(self):
        # NEW SETUP
        self.enter_button.configure(text='Aceptar',command=self.SignIn)
        self.register_button.configure(text='Login',command=self.RestoreLogin)
        self.label_var.set('Registra tu usuario')
        # MOVER BOTONES
        limite = 0.65
        limite_label = 0.75
        if self.Y_pos < limite:
            self.Y_pos += 0.001
            self.Y_pos_label +=0.001
            self.enter_button.place(relx=0.35, rely=self.Y_pos, relwidth=0.13,anchor='w')
            self.register_button.place(relx=0.65, rely=self.Y_pos, relwidth=0.13,anchor='e')
            self.label_access.place(relx=0.5, rely=self.Y_pos_label, anchor='center')
            self.after(1,self.ButtonAnimated)
            if self.Y_pos > limite:
                self.SignInSetup()
    # --------------------------------------------------------------------------
    # SETUP PARA REGISTRAR UN NUEVO USUARIO
    # --------------------------------------------------------------------------
    def SignInSetup(self):
        # CONFIRMAR CONTRASENA ENTRY
        self.confirm_password_var = tk.StringVar()
        self.confirm_password_entry = ctk.CTkEntry(self.login_frame,
                                width=30,
                                fg_color=APP_COLOR['light_gray'],
                                text_color=APP_COLOR['black_m'],
                                textvariable=self.confirm_password_var,
                                corner_radius=5,
                                show='•',
                                border_color=APP_COLOR['light_gray'])
        self.confirm_password_entry.place(relx=0.5, rely=0.55, relwidth = 0.30, anchor='center')
        self.confirm_password_entry.bind('<Return>',lambda event: self.SignIn())
        # CONFIRMAR CONTRASENA LABEL
        confirm_password_label = ctk.CTkLabel(self.login_frame,
                                text='Confirmar contraseña',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray_s'])
        confirm_password_label.place(relx=0.35, rely=0.50, anchor='w')
        # BOTON SHOW PASSWORD
        self.show_password_conf_button = ctk.CTkButton(self.login_frame,
                                text='',
                                text_color=APP_COLOR['black_m'],
                                height=35,
                                width=30,
                                image=ICONS['eye'],
                                fg_color=APP_COLOR['sec'],
                                hover_color=APP_COLOR['sec_s'],
                                command=lambda: self.ShowPassword(2))
        self.show_password_conf_button.place(relx=0.66, rely=0.55,anchor='w')
        # SETUP
        self.password_entry.unbind('<Return>')
        self.password_entry.bind('<Return>',lambda event: self.confirm_password_entry.focus())
    # --------------------------------------------------------------------------
    # REGISTRAR UN NUEVO USUARIO
    # --------------------------------------------------------------------------
    def SignIn(self):
        # GET DATA
        user = self.user_var.get()
        pwd = self.password_var.get()
        conf_pwd = self.confirm_password_var.get()
        # VERIFY DATA
        if not user:
            self.label_var.set('Debe cargar un nombre de usuario.')
            self.login_entry.focus()
            return
        if not pwd:
            self.label_var.set('Debe agregar una contraseña.')
            self.password_entry.focus()
            return
        if not conf_pwd or conf_pwd != pwd:
            self.label_var.set('Las contraseñas no coinciden.')
            self.confirm_password_entry.focus()
            return
        # ADD USER
        user_data = {
            'nombre':'empty',
            'usuario':user,
            'password':pwd,
            'opcode':'0000',
            'correo':None,
            'rol':5,
            'estado':False,
        }
        USER_MANAGER.AddUser(user_data)
        self.RestoreLogin()
    # --------------------------------------------------------------------------
    # GO BACK TO LOGIN
    # --------------------------------------------------------------------------
    def RestoreLogin(self):
        self.login_frame.destroy()
        self.Login()
    # --------------------------------------------------------------------------
    # SHOW PASSWORD
    # --------------------------------------------------------------------------
    def ShowPassword(self,id):
        if id == 1:
            if self.PASSWORD_SHOW:
                self.PASSWORD_SHOW = False
                self.password_entry.configure(show='•')
            else:
                self.PASSWORD_SHOW = True
                self.password_entry.configure(show='')
        else:
            if self.PASSWORD_CONFIRM_SHOW:
                self.PASSWORD_CONFIRM_SHOW = False
                self.confirm_password_entry.configure(show='•')
            else:
                self.PASSWORD_CONFIRM_SHOW = True
                self.confirm_password_entry.configure(show='')
    # --------------------------------------------------------------------------
    # CREAR USUARIO ADMIN
    # --------------------------------------------------------------------------
    def AdminUser(self,event):
        USER_MANAGER.CreateAdminUser()