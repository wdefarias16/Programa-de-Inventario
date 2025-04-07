# CREAR FRAME LOGIN
import customtkinter as ctk
import tkinter as tk
import json, os, bcrypt

fonts = [('Roboto light',25),('Roboto light',15)]
app_colors = ['#eaeaea','#1d1d1d','#1c9bac','#166c78','#5d5d5d']

# LEER EL ARCHIVO DE USUARIOS   
def ReadUsersData():
    global users_database
    if not os.path.exists('Data'):
        os.makedirs('Data')
    try:
        with open('Data/UsersData.json','r') as UsersData_JsonFile:
            users_database=json.load(UsersData_JsonFile)
    except FileNotFoundError:
        users_database = {}
        SaveUsersData()

# SALVAR EL ARCHIVO DE USUARIOS
def SaveUsersData():
    with open('Data/UsersData.json','w') as UsersData_JsonFile:
        json.dump(users_database,UsersData_JsonFile,indent=4)

# CLASE USUARIOS
class Users():
    def __init__(self,user,password):

        self.user = user
        self.password = self.HashPassword(password)

    def HashPassword(self, plain_text_password):
        password_bytes = plain_text_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes,salt)
        return hashed_password.decode('utf-8')
    
    def CheckPassword(self, plain_text_password):
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            self.password.encode('utf-8')
        )

# LOGIN FRAME
class LoginFrame(ctk.CTkFrame):
    def __init__(self,parent,success_callback):
        super().__init__(parent,bg_color=app_colors[0])
        self.success_callback = success_callback
        self.CreateWidgets()
        
    # WIDGETS
    def CreateWidgets(self):
        label_wc = ctk.CTkLabel(self,text='Bienvenido',font=fonts[0],text_color=app_colors[4])
        label_wc.place(anchor='center',relx=0.5,rely=0.3)
        
        self.user_var = tk.StringVar()
        login_entry = ctk.CTkEntry(self,placeholder_text='Usuario',
                                   width=280,
                                   textvariable=self.user_var,
                                   corner_radius=5,
                                   border_color='#fff')
        login_entry.place(anchor='center',relx=0.5,rely=0.4)

        self.password_var = tk.StringVar()
        password_entry = ctk.CTkEntry(self,placeholder_text='Contraseña',
                                      width=280,
                                      textvariable=self.password_var,
                                      corner_radius=5,
                                      show='•',
                                      border_color='#fff')
        password_entry.place(anchor='center',relx=0.5,rely=0.48)

        enter_button = ctk.CTkButton(self,text='Entrar',command=self.Access)
        enter_button.place(anchor='center',relx=0.425,rely=0.6)

        add_button = ctk.CTkButton(self,text='Agregar usuario',command=self.AddUser)
        add_button.place(anchor='center',relx=0.575,rely=0.6)
        
        self.label_var = tk.StringVar(value='Ingresa tus credenciales')
        label_accses = ctk.CTkLabel(self,textvariable=self.label_var,font=fonts[1],text_color=app_colors[4])
        label_accses.place(anchor='center',relx=0.5,rely=0.7)
        
    # ACCESO DEL LOGIN
    def Access(self):
        user = self.user_var.get()
        password = self.password_var.get()

        # CHEQUEAR SI EL USUARIO ESTA EN LA BASE DE DATOS
        if user in users_database:
            stored_hash = users_database[user]
            #SI ESTA EL USUARIO, SE PASA LA FUNCION SUCCESS_CALLBACK
            if bcrypt.checkpw(password.encode('utf-8'),stored_hash.encode('utf-8')):
                self.label_var.set('Bienvenido')
                self.after(500,self.success_callback)
                return
        self.label_var.set('Acceso denegado')

    # AÑADIR UN USUARIO
    def AddUser(self):
        user = self.user_var.get()
        password = self.password_var.get()
        if user in users_database:
            self.label_var.set(f'El usuario {user}, ya esta registrado')
        else:
            
            new_user = Users(user,password)
            users_database[user] = new_user.password
            self.label_var.set('Usuario agregado')
            SaveUsersData()