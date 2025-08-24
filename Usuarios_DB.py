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
    # CREAR USUARIO ADMINISTRADOR - CREAR USUARIO ADMINISTRADOR - CREAR USUARIO ADMINISTRADOR -
    # CREAR USUARIO ADMINISTRADOR - CREAR USUARIO ADMINISTRADOR - CREAR USUARIO ADMINISTRADOR -
    def CreateAdminUser(self):
        default_nombre = "William De Farias"
        default_usuario = "a"
        default_password = "a"
        default_opcode = "0000"
        default_correo = "admin@example.com"
        default_rol = 1                 
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM usuarios WHERE usuario = %s;", (default_usuario,))
                if cur.fetchone() is None:
                    # Si no existe, se crea el usuario por defecto
                    hashed_password = self.HashPassword(default_password)
                    cur.execute("""
                        INSERT INTO usuarios (nombre,usuario,clave,clave_nohash,opcode,correo,rol,estado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """, (default_nombre, default_usuario, hashed_password,
                          default_password, default_opcode, default_correo, default_rol, False))
                    self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error agregando usuario por defecto: {e}")
    # ENCRIPTAR CONTRASEÑA - ENCRIPTAR CONTRASEÑA - ENCRIPTAR CONTRASEÑA -
    # ENCRIPTAR CONTRASEÑA - ENCRIPTAR CONTRASEÑA - ENCRIPTAR CONTRASEÑA -
    def HashPassword(self, plain_text_password):
        password_bytes = plain_text_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')
    # COMPARAR CONTRASEÑA PLANA CON EL HASH ALMACENADO - COMPARAR CONTRASEÑA PLANA CON EL HASH ALMACENADO -
    # COMPARAR CONTRASEÑA PLANA CON EL HASH ALMACENADO - COMPARAR CONTRASEÑA PLANA CON EL HASH ALMACENADO -
    def CheckPassword(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            hashed_password.encode('utf-8'))
    # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN -
    # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN -
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
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
    # AGREGA UN NUEVO USUARIO - AGREGA UN NUEVO USUARIO - AGREGA UN NUEVO USUARIO - 
    # AGREGA UN NUEVO USUARIO - AGREGA UN NUEVO USUARIO - AGREGA UN NUEVO USUARIO - 
    def AddUser(self, nombre,usuario, password,cod_op,correo,rol, estado=False):
        try:
            with self.conn.cursor() as cur:
                # Verificar si el usuario ya existe usando la columna "usuario"
                cur.execute("SELECT 1 FROM usuarios WHERE usuario = %s;", (usuario,))
                if cur.fetchone():
                    raise ValueError("El usuario ya existe.")
                hashed_password = self.HashPassword(password)
                cur.execute("""
                    INSERT INTO usuarios (nombre,usuario,clave,clave_nohash,opcode,correo,rol,estado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (nombre, usuario, hashed_password, password, cod_op, correo, rol, estado))
                self.conn.commit()
                messagebox.showinfo("Info", "El usuario se ha agregado correctamente.")
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar el usuario: {e}")
            return False
    
    # BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO -
    # BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO - BORRAR USUARIO -
    def DeleteUser(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM usuarios WHERE codigo = %s;", (codigo,))
                if cur.rowcount == 0:
                    raise ValueError("El usuario no existe.")
                self.conn.commit()
                messagebox.showinfo("Info", "El usuario se ha eliminado correctamente.")
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al eliminar el usuario: {e}")
            return False
    # ACTUALIZAR USUARIO - ACTUALIZAR USUARIO - ACTUALIZAR USUARIO - ACTUALIZAR USUARIO -
    # ACTUALIZAR USUARIO - ACTUALIZAR USUARIO - ACTUALIZAR USUARIO - ACTUALIZAR USUARIO -
    def UpdateUser(self, codigo, nombre, usuario, correo, opcode, rol, estado = False, password = None):
        try:
            with self.conn.cursor() as cur:
                # SI VIENE CONTRASEÑA, SE ACTUALIZA, SI NO, SE DEJA IGUAL
                if password:
                    hashed_password = self.HashPassword(password)
                    cur.execute("""
                        UPDATE usuarios
                        SET nombre = %s, usuario = %s, clave = %s, clave_nohash = %s,
                            correo = %s, opcode = %s, rol = %s, estado = %s
                        WHERE codigo = %s;
                    """, (nombre, usuario, hashed_password, password, correo, opcode, rol, estado, codigo))
                # SI NO VIENE CONTRASEÑA, NO SE ACTUALIZA
                else:
                    cur.execute("""
                        UPDATE usuarios
                        SET nombre = %s, usuario = %s,
                            correo = %s, opcode = %s, rol = %s, estado = %s
                        WHERE codigo = %s;
                    """, (nombre, usuario, correo, opcode, rol, estado, codigo))
                if cur.rowcount == 0:
                    raise ValueError("El usuario no existe.")
                self.conn.commit()
                messagebox.showinfo("Info", "El usuario se ha actualizado correctamente.")
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al actualizar el usuario: {e}")
            return False
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
    # OBTENER TODOS LOS USUARIOS - OBTENER TODOS LOS USUARIOS - OBTENER TODOS LOS USUARIOS -
    # OBTENER TODOS LOS USUARIOS - OBTENER TODOS LOS USUARIOS - OBTENER TODOS LOS USUARIOS -
    def GetAllUsers(self):
        users = []
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, nombre, usuario, clave, clave_nohash, opcode, correo, rol, estado FROM usuarios;")
                rows = cur.fetchall()
                for row in rows:
                    user = {
                        'codigo': row[0],
                        'nombre': row[1],
                        'usuario': row[2],
                        'clave': row[3],
                        'clave_nohash': row[4],
                        'opcode': row[5],
                        'correo': row[6],
                        'rol': row[7],
                        'estado': row[8]
                    }
                    users.append(user)
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener los usuarios: {e}")
        return users
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # OBTENER ROLES DE USUARIO DE LA TABLA ROLES
    """ LA TABLA ROLES ES ASI:
    CREATE TABLE IF NOT EXISTS roles (
        codigo SERIAL PRIMARY KEY,
        rol VARCHAR(50) UNIQUE NOT NULL),
    """
    # LA FUNCION DEVOLVERA UNA LISTA CON LOS ROLES EN FORMATO:['1 - Admin','2 - User'...]
    def GetRoles(self):
        roles = []
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, rol FROM roles;")
                rows = cur.fetchall()
                for row in rows:
                    role = f"{row[0]} - {row[1]}"
                    roles.append(role)
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener los roles: {e}")
        return roles
    
    # CIERRA LA CONEXIÓN CUANDO EL OBJETO SE DESTRUYA
    def __del__(self):
        if self.conn:
            self.conn.close()