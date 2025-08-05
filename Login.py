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
    # GRID SETUP
        for rows in range(20):
            self.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(6):
            self.columnconfigure(columns,weight=1,uniform='columns')
    # LOGIN
    def Login(self):
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # ENTRADA USUARIO
        self.user_var = tk.StringVar()
        self.login_entry = ctk.CTkEntry(self,placeholder_text='Usuario',
                                   width=280,
                                   textvariable=self.user_var,
                                   corner_radius=5,
                                   border_color='#fff')
        self.login_entry.grid(row=7,column=2,columnspan=2,sticky='we')
        self.login_entry.bind("<Control-a>",self.AdminUser)
        self.login_entry.bind("<Return>",lambda event: self.password_entry.focus())
        # INICIAR EL PROGRAMA CON LA ENTRADA DE USUARIO ACTIVA
        self.login_entry.after(100, lambda: self.login_entry.focus_set())
        # ENTRADA CONTRASENA
        self.password_var = tk.StringVar()
        self.password_entry = ctk.CTkEntry(self,placeholder_text='Contraseña',
                                      width=280,
                                      textvariable=self.password_var,
                                      corner_radius=5,
                                      show='•',
                                      border_color='#fff')
        self.password_entry.grid(row=9,column=2,columnspan=2,sticky='we')
        self.password_entry.bind("<Return>",lambda event:self.Access())
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # MENSAJE BIENVENIDO
        label_wc = ctk.CTkLabel(self,
                                text='Bienvenido',
                                font=FONT['title_light'],
                                text_color=APP_COLOR['gray'])
        label_wc.grid(row=3,column=2,columnspan=2,sticky='we')
        # USUARIO
        user_label = ctk.CTkLabel(self,
                                text='Usuario',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        user_label.grid(row=6,column=2,columnspan=1,sticky='ws')
        # CONTRASENA
        password_label = ctk.CTkLabel(self,
                                text='Contraseña',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        password_label.grid(row=8,column=2,columnspan=1,sticky='ws')
        # MENSAJE INFERIOR
        self.label_var = tk.StringVar(value='Ingresa tus credenciales')
        label_accses = ctk.CTkLabel(self,
                                textvariable=self.label_var,
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        label_accses.grid(row=13,column=2,columnspan=2,sticky='we')
    # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -  
        # BOTON ENTRAR
        enter_button = ctk.CTkButton(self,
                                     text='Entrar',
                                     fg_color=APP_COLOR['main'],
                                     hover_color=APP_COLOR['sec'],
                                     command=self.Access)
        enter_button.grid(row=11,column=2,columnspan=1,sticky='we',padx=5)
        

        
        

        

        
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