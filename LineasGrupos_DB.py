import tkinter as tk
import customtkinter as ctk
import psycopg2
from style import*
from tkinter import messagebox

class LineasGrupos:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()
        self.initialize_default()

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

    # INICIALIZAR DATOS POR DEFECTO (si no existe la línea '001')
    def initialize_default(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo FROM lineas WHERE codigo = %s;", ("1",))
                if cur.fetchone() is None:
                    # Insertar línea por defecto
                    cur.execute("INSERT INTO lineas (codigo, nombre) VALUES (%s, %s);", ("1", "Linea 1"))

                    cur.execute("""
                        INSERT INTO grupos (codigo, linea, nombre, porcentaje1, porcentaje2, porcentaje3)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """, ("1.1", "1", "Grupo 1", 0.0, 0.0, 0.0))
                    self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al inicializar datos: {str(e)}")

    # RETORNA LOS NOMBRES DE LÍNEA EN FORMATO (CÓDIGO - NOMBRE)
    def GetLineNames(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, nombre FROM lineas ORDER BY codigo;")
                rows = cur.fetchall()
                return [f"{codigo} - {nombre}" for codigo, nombre in rows]
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener nombres de líneas: {str(e)}")
            return []

    # RETORNA LOS NOMBRES DE GRUPO DE UNA LÍNEA
    def GetGroupNames(self, linea):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo, nombre FROM grupos WHERE linea = %s ORDER BY codigo;", (linea,))
                rows = cur.fetchall()
                # Opcional: Si deseas mostrar solo la parte después del guion,
                # usa: codigo.split('-')[1] en lugar de codigo
                return [f"{codigo} - {nombre}" for codigo, nombre in rows]
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener nombres de grupos: {str(e)}")
            return []

    # RETORNA LOS PORCENTAJES DE UN GRUPO; se espera que se pase el código interno del grupo (sin el prefijo de línea)
    def GetPorcentajes(self, linea, grupo):
        
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT porcentaje1, porcentaje2, porcentaje3 
                    FROM grupos 
                    WHERE linea = %s AND codigo = %s;
                """, (linea, grupo))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Base de datos", f"No se encontró el grupo {grupo} en la línea {linea}")
                    return {}
                porcentaje1, porcentaje2, porcentaje3 = row
                return {
                    "porcentaje1": float(porcentaje1),
                    "porcentaje2": float(porcentaje2),
                    "porcentaje3": float(porcentaje3)
                }
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al obtener porcentajes: {str(e)}")
            return {}

    # CALCULA Y RETORNA LOS PRECIOS BASADOS EN LOS PORCENTAJES Y UN COSTO DADO
    def GetPrecios(self, linea, grupo, costo):
        porcentajes = self.GetPorcentajes(linea, grupo)
        if not porcentajes:
            return []
        try:
            # Convertir porcentajes a coeficientes: p = (100 - porcentaje) / 100
            p1 = (100 - porcentajes["porcentaje1"]) / 100
            p2 = (100 - porcentajes["porcentaje2"]) / 100
            p3 = (100 - porcentajes["porcentaje3"]) / 100
            # Evitar división por cero
            precios = [round(costo / p, 2) for p in [p1, p2, p3] if p != 0]
            return precios
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular precios: {str(e)}")
            return []

    # AGREGA UNA LÍNEA. Si se proporciona el diccionario 'grupos', se insertan también los grupos asociados.
    # En 'grupos' se espera que la clave sea el código interno del grupo (por ejemplo "1", "2", etc.),
    # y se combinará con el código de línea para generar el código único.
    def Add_Line(self, codigo, nombre, grupos=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror('Error', f'El código de línea {codigo} ya se encuentra en la base de datos')
                    return False
                
                cur.execute("INSERT INTO lineas (codigo, nombre) VALUES (%s, %s);", (codigo, nombre))
                
                if grupos:
                    # Se espera que 'grupos' sea un diccionario del tipo:
                    # { codigo_interno: { "nombre_grupo": ..., "porcentaje1": ..., "porcentaje2": ..., "porcentaje3": ... }, ... }
                    for codigo_interno, data in grupos.items():
                        full_codigo = f"{codigo}-{codigo_interno}"
                        cur.execute("""
                            INSERT INTO grupos (codigo, linea, nombre, porcentaje1, porcentaje2, porcentaje3)
                            VALUES (%s, %s, %s, %s, %s, %s);
                        """, (
                            full_codigo,
                            codigo,
                            data.get("nombre_grupo", ""),
                            data.get("porcentaje1", 0.0),
                            data.get("porcentaje2", 0.0),
                            data.get("porcentaje3", 0.0)
                        ))
                self.conn.commit()
                messagebox.showinfo('Info', f'La línea {codigo} se ha cargado correctamente')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar la línea: {str(e)}")
            return False

    # MODIFICA EL NOMBRE DE UNA LÍNEA
    def Mod_Linea(self, codigo, nuevo_nombre):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'No se encontró la línea {codigo}.')
                    return False
                cur.execute("UPDATE lineas SET nombre = %s WHERE codigo = %s;", (nuevo_nombre, codigo))
                self.conn.commit()
                messagebox.showinfo('Info', f'La línea {codigo} se ha editado correctamente')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al modificar la línea: {str(e)}")
            return False

    # ELIMINA UNA LÍNEA Y SUS GRUPOS ASOCIADOS
    def Del_Linea(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'No se encontró la línea {codigo}.')
                    return False
                # Eliminar grupos asociados a esa línea
                cur.execute("DELETE FROM grupos WHERE linea = %s;", (codigo,))
                cur.execute("DELETE FROM lineas WHERE codigo = %s;", (codigo,))
                self.conn.commit()
                messagebox.showinfo('Info', f'La línea {codigo} ha sido eliminada')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al eliminar la línea: {str(e)}")
            return False

    def SearchLineByName(self,search):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre FROM lineas
                    WHERE nombre ILIKE %s;
                """, ('%' + search + '%',))
                rows = cur.fetchall()
                outcome = []
                for row in rows:
                    codigo, nombre = row
                    outcome.append(
                        {'codigo':codigo,
                         'linea':nombre})
                return outcome
        except Exception as e:
            messagebox.showerror('Error', f"Error buscando líneas: {str(e)}")
            return []
    
    def SearchGroupByName(self,search,line):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre, linea FROM grupos
                    WHERE nombre ILIKE %s AND linea = %s;
                """, ('%' + search + '%',line))
                rows = cur.fetchall()
                outcome = []
                for row in rows:
                    codigo, linea, grupo = row
                    outcome.append(
                        {'codigo':codigo,
                         'linea':linea,
                         'grupo':grupo})
                return outcome
        except Exception as e:
            messagebox.showerror('Error', f"Error buscando líneas: {str(e)}")
            return []
            

    # AGREGA UN GRUPO A UNA LÍNEA EXISTENTE.
    # Aquí se recibe el *código interno del grupo* (por ejemplo, "1" o "2") 
    # y se concatena con el código de la línea para formar el código único.
    def Add_Group(self, linea, codigo_interno, nombre_grupo, porcentaje1, porcentaje2, porcentaje3):
        full_codigo = f"{linea}.{codigo_interno}"
        try:
            with self.conn.cursor() as cur:
                # Verificar que la línea exista
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (linea,))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'La línea con código {linea} no existe')
                    return False

                # Verificar si el grupo ya existe en esa línea (usando el código concatenado)
                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, full_codigo))
                if cur.fetchone():
                    messagebox.showerror('Error', f'El grupo con código {full_codigo} ya existe en la línea {linea}')
                    return False

                cur.execute("""
                    INSERT INTO grupos (codigo, linea, nombre, porcentaje1, porcentaje2, porcentaje3)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (full_codigo, linea, nombre_grupo, porcentaje1, porcentaje2, porcentaje3))
                self.conn.commit()
                messagebox.showinfo('Info', f'El grupo {full_codigo} - {nombre_grupo} se ha agregado correctamente a la línea {linea}')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar el grupo: {str(e)}")
            return False

    # MODIFICA LOS DATOS DE UN GRUPO EXISTENTE.
    # Se utiliza el código interno (concatenado con la línea) para identificar el grupo.
    def Mod_Grupo(self, linea, codigo_grupo, nuevo_nombre, porcentaje1, porcentaje2, porcentaje3):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, codigo_grupo))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'El grupo con código {codigo_grupo} no existe en la línea {linea}')
                    return False

                cur.execute("""
                    UPDATE grupos SET
                        nombre = %s,
                        porcentaje1 = %s,
                        porcentaje2 = %s,
                        porcentaje3 = %s
                    WHERE linea = %s AND codigo = %s;
                """, (nuevo_nombre, porcentaje1, porcentaje2, porcentaje3, linea, codigo_grupo))
                self.conn.commit()
                messagebox.showinfo('Info', f'El grupo {codigo_grupo} ha sido modificado correctamente en la línea {linea}')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al modificar el grupo: {str(e)}")
            return False

    # ELIMINA UN GRUPO DE UNA LÍNEA.
    # Se identifica el grupo por medio de la concatenación del código de línea y el código interno.
    def Del_Group(self, linea, codigo_grupo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (linea,))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'La línea con código {linea} no existe')
                    return False

                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, codigo_grupo))
                if not cur.fetchone():
                    messagebox.showerror('Error', f'El grupo con código {codigo_grupo} no existe en la línea {linea}')
                    return False

                cur.execute("DELETE FROM grupos WHERE linea = %s AND codigo = %s;", (linea, codigo_grupo))
                self.conn.commit()
                messagebox.showinfo('Info', f'El grupo {codigo_grupo} ha sido eliminado correctamente de la línea {linea}')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al eliminar el grupo: {str(e)}")
            return False

    # CHEQUEA SI LA LÍNEA EXISTE
    def CheckLine(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    return True
                else:
                    messagebox.showerror('Error de Línea', f'El código {codigo} no pertenece a ninguna línea cargada.')
                    return False
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al chequear la línea: {str(e)}")
            return False

    # CHEQUEA SI UN GRUPO PERTENECE A LA LÍNEA usando el código interno
    def CheckGrupo(self, linea, grupo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, grupo))
                if cur.fetchone():
                    return True
                else:
                    messagebox.showerror('Error de carga', f'El grupo {grupo} no pertenece a la línea {linea}.')
                    return False
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al chequear el grupo: {str(e)}")
            return False

    # CIERRA LA CONEXIÓN AL DESTRUIR EL OBJETO
    def __del__(self):
        if self.conn:
            self.conn.close()