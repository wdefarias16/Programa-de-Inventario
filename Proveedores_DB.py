from tkinter import messagebox
import psycopg2

class Proveedores:
    def __init__(self,dbname,user,password,host,port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        # ABRE UNA CONEXION CON LA BASE DE DATOS
        self.conn = None
        self.connect_db()
# CONECTARSE A LA BASE DE DATOS
    def connect_db(self):
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

# DEVUELVE UNA LISTA CON EL FORMATO CODIGO-NOMBRE
    def GetProvNames(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, nombre FROM proveedores ORDER BY codigo;")
                rows = cur.fetchall()
                return [f"{codigo} - {nombre}" for codigo, nombre in rows]
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching provider names: {str(e)}")
            return []

# DEVUELVE TODOS LOS PROVEEDORES EN UN DICCIONARIO CON CODIGO DE LLAVE
    def GetProv(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo,nombre,contacto,
                           direccion1,direccion2,ciudad,
                           telefono,celular,email,rif 
                    FROM proveedores;
                """)
                rows = cur.fetchall()
                proveedores = {}
                for row in rows:
                    codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif = row
                    proveedores[codigo] = {
                        'codigo': codigo,
                        'nombre': nombre,
                        'contacto': contacto,
                        'direccion1': direccion1,
                        'direccion2': direccion2,
                        'ciudad': ciudad,
                        'telefono': telefono,
                        'celular': celular,
                        'email': email,
                        'rif': rif
                    }
                return proveedores
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al leer los proveedores: {str(e)}")
            return {}
# DEVUELVE UN PROVEEDOR BUSCADO POR CODIGO
    def BuscarProv(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif 
                    FROM proveedores 
                    WHERE codigo = %s;
                """, (codigo,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror('Base de datos', f'El proveedor con codigo {codigo} no existe')
                    return None
                else:
                    codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif = row
                    proveedor = {
                        'codigo': codigo,
                        'nombre': nombre,
                        'contacto': contacto,
                        'direccion1': direccion1,
                        'direccion2': direccion2,
                        'ciudad': ciudad,
                        'telefono': telefono,
                        'celular': celular,
                        'email': email,
                        'rif': rif
                    }
                    return proveedor
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al buscar el codigo de proveedor: {str(e)}")
            return None
# DEVUELVE PROVEEDORES BUSCADOS POR NOMBRE
    def SearchProvByName(self, search):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif 
                    FROM proveedores 
                    WHERE nombre ILIKE %s;
                """, ('%' + search + '%',))
                rows = cur.fetchall()
                outcome = []
                for row in rows:
                    codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif = row
                    proveedor = {
                        'codigo': codigo,
                        'nombre': nombre,
                        'contacto': contacto,
                        'direccion1': direccion1,
                        'direccion2': direccion2,
                        'ciudad': ciudad,
                        'telefono': telefono,
                        'celular': celular,
                        'email': email,
                        'rif': rif
                    }
                    outcome.append(proveedor)
                return outcome
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar nombre del proveedor: {str(e)}")
            return []
# AGREGAR UN PROVEEDOR
    def Add_Prov(self, codigo, nombre, contacto='', direccion1='', direccion2='',
                 ciudad='', telefono='', celular='', email='', rif=''):
        try:
            with self.conn.cursor() as cur:
                # CHEQUEAR SI EL PROVEEDOR YA EXISTE
                cur.execute("SELECT 1 FROM proveedores WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror('Error', f'El proveedor {codigo} ya se encuentra en la base de datos')
                    return False
                # GUARDAR EL PROVEEDOR
                cur.execute("""
                    INSERT INTO proveedores (codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (codigo, nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif))
                self.conn.commit()
                messagebox.showinfo('Info', f'El proveedor {codigo} - {nombre} se ha cargado correctamente')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar el proveedor: {str(e)}")
            return False
# MODIFICAR UN PROVEEDOR
    def Mod_Prov(self, codigo, nombre, contacto='', direccion1='', direccion2='',
                 ciudad='', telefono='', celular='', email='', rif=''):
        try:
            answer = messagebox.askyesno('¡Atención!', f'¿Está seguro que desea modificar el proveedor {codigo} con estos datos?')
            if answer:
                with self.conn.cursor() as cur:
                    cur.execute("""
                        UPDATE proveedores SET
                            nombre = %s,
                            contacto = %s,
                            direccion1 = %s,
                            direccion2 = %s,
                            ciudad = %s,
                            telefono = %s,
                            celular = %s,
                            email = %s,
                            rif = %s
                        WHERE codigo = %s;
                    """, (nombre, contacto, direccion1, direccion2, ciudad, telefono, celular, email, rif, codigo))
                    self.conn.commit()
                    messagebox.showinfo('Info', f'El proveedor {codigo} ha sido modificado.')
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al modificar el proveedor: {str(e)}")
# ELIMINAR UN PROVEEDOR
    def Del_Prov(self, codigo):
        try:
            answer = messagebox.askyesno('¡Atención!', f'¿Está seguro que desea eliminar el proveedor {codigo}?')
            if answer:
                with self.conn.cursor() as cur:
                    cur.execute("DELETE FROM proveedores WHERE codigo = %s;", (codigo,))
                    self.conn.commit()
                    messagebox.showinfo('Info', f'El proveedor {codigo} ha sido eliminado.')
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al eliminar el proveedor: {str(e)}")
# CHEQUEAR EL CODIGO DE UN PROVEEDOR
    def ChechProv(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM proveedores WHERE codigo = %s;", (codigo,))
                return cur.fetchone() is not None
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al chequear codigo de proveedor: {str(e)}")
            return False
# CIERRA LA CONEXION CON LA BASE DE DATOS SI EL OBJETO SE BORRA
    def __del__(self):
        if self.conn:
            self.conn.close()