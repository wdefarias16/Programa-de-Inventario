import psycopg2
import bcrypt
from tkinter import messagebox

class Users:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.dbuser = user
        self.dbpassword = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()

    # CONECTARSE A LA BASE DE DATOS
    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.dbuser,
                password=self.dbpassword,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al conectarse a la base de datos: {e}")

    def CreateAdminUser(self):
        default_nombre = "William De Farias"
        default_usuario = "a"
        default_password = "a"   # Cambia este valor por el que desees
        default_opcode = 0000
        default_correo = "admin@example.com"
        default_rol = 1                 # Por ejemplo, 1 = rol de administrador
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM usuarios WHERE usuario = %s;", (default_usuario,))
                if cur.fetchone() is None:
                    # Si no existe, se crea el usuario por defecto
                    hashed_password = self.HashPassword(default_password)
                    cur.execute("""
                        INSERT INTO usuarios (opcode,nombre,usuario, correo, clave, rol, estado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, (default_opcode,default_nombre,default_usuario, default_correo, hashed_password, default_rol, True))
                    self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error agregando usuario por defecto: {e}")




    # ENCRIPTAR CONTRASEÑA
    def HashPassword(self, plain_text_password):
        password_bytes = plain_text_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')

    # COMPARAR CONTRASEÑA PLANA CON EL HASH ALMACENADO
    def CheckPassword(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    # ACCESS: Verifica si el usuario existe (identificado por la columna "usuario")
    # y si la clave coincide, devolviendo True o False.
    def Access(self, usuario, password):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT clave FROM usuarios WHERE usuario = %s;", (usuario,))
                row = cur.fetchone()
                if row is None:
                    return False
                stored_hash = row[0]
                return self.CheckPassword(password, stored_hash)
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al verificar el acceso: {e}")
            return False

    # AGREGA UN NUEVO USUARIO.
    # Se requiere: usuario (usuario que identifica al usuario), correo, clave, rol y estado.
    # Se verifica previamente que no exista otro usuario con ese mismo usuario.
    def AddUser(self, usuario, correo, password, rol, estado=True):
        try:
            with self.conn.cursor() as cur:
                # Verificar si el usuario ya existe usando la columna "usuario"
                cur.execute("SELECT 1 FROM usuarios WHERE usuario = %s;", (usuario,))
                if cur.fetchone():
                    raise ValueError("El usuario ya existe.")
                hashed_password = self.HashPassword(password)
                cur.execute("""
                    INSERT INTO usuarios (usuario, correo, clave, rol, estado)
                    VALUES (%s, %s, %s, %s, %s);
                """, (usuario, correo, hashed_password, rol, estado))
                self.conn.commit()
                messagebox.showinfo("Info", "El usuario se ha agregado correctamente.")
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar el usuario: {e}")
            return False

    # CIERRA LA CONEXIÓN CUANDO EL OBJETO SE DESTRUYA
    def __del__(self):
        if self.conn:
            self.conn.close()