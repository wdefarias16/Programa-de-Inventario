import json
import os
import bcrypt

# CLASE USUARIOS
class Users:
    def __init__(self, file_name='Data/UsersData.json'):
        self.file_name = file_name
        self.UsersData = {}
        self.ReadUsersData()
    # LEER EL ARCHIVO DE USUARIOS   
    def ReadUsersData(self):
        if not os.path.exists('Data'):
            os.makedirs('Data')
        try:
            with open(self.file_name, 'r') as UsersData_JsonFile:
                self.UsersData = json.load(UsersData_JsonFile)
        except FileNotFoundError:
            self.UsersData = {}
            self.SaveUsersData()

    # SALVAR EL ARCHIVO DE USUARIOS
    def SaveUsersData(self):
        with open(self.file_name, 'w') as UsersData_JsonFile:
            json.dump(self.UsersData, UsersData_JsonFile, indent=4)

    # ENCRIPTAR CONTRASEÑA
    def HashPassword(self, plain_text_password):
        password_bytes = plain_text_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')

    # CHEQUEAR CONTRASEÑA: recibe la contraseña en claro y su hash para comparar.
    def CheckPassword(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    
    # ACCESS: verifica si el usuario existe y si la contraseña coincide.
    def Access(self, user, password):
        if user in self.UsersData:
            stored_hash = self.UsersData[user]
            if self.CheckPassword(password, stored_hash):
                return True
        return False

    def AddUser(self, user, password):
        if user in self.UsersData:
            raise ValueError("El usuario ya existe.")
        hashed_password = self.HashPassword(password)
        self.UsersData[user] = hashed_password
        self.SaveUsersData()
        return True