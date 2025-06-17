from tkinter import messagebox
import psycopg2

class Proveedores:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()

    def connect_db(self):
        """Conectarse a la base de datos."""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al conectarse a la base de datos: {str(e)}")

    def GetProvNames(self):
        """Devuelve una lista con el formato CODIGO - NOMBRE."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, nombre FROM proveedores ORDER BY codigo;")
                rows = cur.fetchall()
                return [f"{codigo} - {nombre}" for codigo, nombre in rows]
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener nombres de proveedores: {str(e)}")
            return []

    def GetProvs(self):
        """Devuelve todos los proveedores en un diccionario con CODIGO como llave."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT codigo, nombre, contacto, direccion1, direccion2, ciudad, 
                                      telefono1, telefono2, celular1, celular2, email, rif 
                               FROM proveedores;""")
                rows = cur.fetchall()
                proveedores = {codigo: {
                    'codigo': codigo, 'nombre': nombre, 'contacto': contacto,
                    'direccion1': direccion1, 'direccion2': direccion2, 'ciudad': ciudad,
                    'telefono1': telefono1, 'telefono2': telefono2, 'celular1': celular1, 'celular2': celular2,
                    'email': email, 'rif': rif
                } for codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono1, telefono2, celular1, celular2, email, rif in rows}
                return proveedores
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener proveedores: {str(e)}")
            return {}

    def GetProv(self, codigo):
        """Devuelve un proveedor específico por su código."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT codigo, nombre, contacto, direccion1, direccion2, ciudad, 
                                      telefono1, telefono2, celular1, celular2, email, rif 
                               FROM proveedores WHERE codigo = %s;""", (codigo,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Base de datos", f"El proveedor con código {codigo} no existe")
                    return None
                return {campo: valor for campo, valor in zip(
                    ['codigo', 'nombre', 'contacto', 'direccion1', 'direccion2', 'ciudad',
                     'telefono1', 'telefono2', 'celular1', 'celular2', 'email', 'rif'], row)}
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener el proveedor: {str(e)}")
            return None

    def SearchProvByName(self, search):
        """Busca proveedores por nombre."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT codigo, nombre, contacto, direccion1, direccion2, ciudad, 
                                      telefono1, telefono2, celular1, celular2, email, rif 
                               FROM proveedores WHERE nombre ILIKE %s;""", ('%' + search + '%',))
                rows = cur.fetchall()
                return [{campo: valor for campo, valor in zip(
                    ['codigo', 'nombre', 'contacto', 'direccion1', 'direccion2', 'ciudad',
                     'telefono1', 'telefono2', 'celular1', 'celular2', 'email', 'rif'], row)} for row in rows]
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al buscar proveedores por nombre: {str(e)}")
            return []

    def Add_Prov(self, codigo, nombre, contacto='', direccion1='', direccion2='',
                 ciudad='', telefono1='', telefono2='', celular1='', celular2='', email='', rif=''):
        """Agrega un nuevo proveedor."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM proveedores WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror("Error", f"El proveedor {codigo} ya existe en la base de datos")
                    return False
                cur.execute("""INSERT INTO proveedores (codigo, nombre, contacto, direccion1, direccion2, ciudad,
                                                         telefono1, telefono2, celular1, celular2, email, rif)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                            (codigo, nombre, contacto, direccion1, direccion2, ciudad,
                             telefono1, telefono2, celular1, celular2, email, rif))
                self.conn.commit()
                messagebox.showinfo("Info", f"Proveedor {codigo} - {nombre} agregado correctamente")
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar proveedor: {str(e)}")
            return False

    def Mod_Prov(self, codigo, nombre, contacto='', direccion1='', direccion2='',
                 ciudad='', telefono1='', telefono2='', celular1='', celular2='', email='', rif=''):
        """Modifica un proveedor existente."""
        try:
            answer = messagebox.askyesno("¡Atención!", f"¿Desea modificar el proveedor {codigo} con estos datos?")
            if answer:
                with self.conn.cursor() as cur:
                    cur.execute("""UPDATE proveedores SET nombre = %s, contacto = %s, direccion1 = %s, 
                                    direccion2 = %s, ciudad = %s, telefono1 = %s, telefono2 = %s, 
                                    celular1 = %s, celular2 = %s, email = %s, rif = %s WHERE codigo = %s;""",
                                (nombre, contacto, direccion1, direccion2, ciudad,
                                 telefono1, telefono2, celular1, celular2, email, rif, codigo))
                    self.conn.commit()
                    messagebox.showinfo("Info", f"Proveedor {codigo} modificado correctamente")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al modificar proveedor: {str(e)}")

    def Del_Prov(self, codigo):
        """Elimina un proveedor."""
        try:
            answer = messagebox.askyesno("¡Atención!", f"¿Desea eliminar el proveedor {codigo}?")
            if answer:
                with self.conn.cursor() as cur:
                    cur.execute("DELETE FROM proveedores WHERE codigo = %s;", (codigo,))
                    self.conn.commit()
                    messagebox.showinfo("Info", f"Proveedor {codigo} eliminado correctamente")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al eliminar proveedor: {str(e)}")

    def __del__(self):
        """Cierra la conexión al eliminar el objeto."""
        if self.conn:
            self.conn.close()
