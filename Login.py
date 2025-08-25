# CREAR FRAME LOGIN
import customtkinter as ctk
import tkinter as tk
from style import *
from DatabaseManager import USER_MANAGER

# LOGIN FRAME
class LoginFrame(ctk.CTkFrame):
    def __init__(self,parent,success_callback):
        super().__init__(parent,bg_color=APP_COLOR['white_m'])
        self.success_callback = success_callback
        self.Login()
    # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - 
    # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - 
    def Login(self):
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # ENTRADA USUARIO
        self.user_var = tk.StringVar()
        self.login_entry = ctk.CTkEntry(self,placeholder_text='Usuario',
                                height=30,
                                textvariable=self.user_var,
                                corner_radius=5,
                                border_color='#fff')
        self.login_entry.place(relx=0.5, rely=0.35, relwidth = 0.30, anchor='center')
        self.login_entry.bind("<Control-a>",self.AdminUser)
        self.login_entry.bind("<Return>",lambda event: self.password_entry.focus())
        # INICIAR EL PROGRAMA CON LA ENTRADA DE USUARIO ACTIVA
        self.login_entry.after(100, lambda: self.login_entry.focus_set())
        # ENTRADA CONTRASENA
        self.password_var = tk.StringVar()
        self.password_entry = ctk.CTkEntry(self,placeholder_text='Contraseña',
                                width=30,
                                textvariable=self.password_var,
                                corner_radius=5,
                                show='•',
                                border_color='#fff')
        self.password_entry.place(relx=0.5, rely=0.45, relwidth = 0.30, anchor='center')
        self.password_entry.bind("<Return>",lambda event:self.Access())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # MENSAJE BIENVENIDO
        label_wc = ctk.CTkLabel(self,
                                text='Bienvenido',
                                font=FONT['title_light'],
                                text_color=APP_COLOR['gray'])
        label_wc.place(relx=0.5, rely=15, anchor='center')
        # USUARIO
        user_label = ctk.CTkLabel(self,
                                text='Usuario',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        user_label.place(relx=0.35, rely=0.30, anchor='w')
        # CONTRASENA
        password_label = ctk.CTkLabel(self,
                                text='Contraseña',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        password_label.place(relx=0.35, rely=0.40, anchor='w')
        # MENSAJE INFERIOR
        self.label_var = tk.StringVar(value='Ingresa tus credenciales')
        label_accses = ctk.CTkLabel(self,
                                textvariable=self.label_var,
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        label_accses.place(relx=0.5, rely=0.70, anchor='center')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -  
        # BOTON ENTRAR
        enter_button = ctk.CTkButton(self,
                                text='Entrar',
                                height=35,
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'],
                                command=self.Access)
        enter_button.place(relx=0.35, rely=0.53, relwidth=0.13,anchor='w')
        # BOTON REGISTRAR
        register_button = ctk.CTkButton(self,
                                text='Registrarse',
                                height=35,
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'],
                                command=self.Access)
        register_button.place(relx=0.65, rely=0.53, relwidth=0.13,anchor='e')
        

        
        

        

        
    # ACCESO DEL LOGIN
    def Access(self):
        user = self.user_var.get()
        password = self.password_var.get()
        if USER_MANAGER.Access(user,password):
            self.label_var.set('Bienvenido')
            self.after(500,self.success_callback)
        else:
            self.label_var.set('Acceso denegado')

    def AddUser(self):
        user = self.user_var.get()
        password = self.password_var.get()
        if USER_MANAGER.AddUser(user,password):
            self.label_var.set('Usuario agregado')

    def AdminUser(self,event):
        USER_MANAGER.CreateAdminUser()