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
# CONECTARSE A LA BASE DE DATOS - CONECTARSE A LA BASE DE DATOS
# CONECTARSE A LA BASE DE DATOS - CONECTARSE A LA BASE DE DATOS
    # CONEXION
    # CONEXION
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
    # INICIALIZAR DATOS POR DEFECTO
    # INICIALIZAR DATOS POR DEFECTO
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
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
    # AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - 
    # AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - AGREGA UNA LÍNEA - 
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
    def Add_LineNM(self, codigo, nombre, grupos=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    print(f'El código de línea {codigo} ya se encuentra en la base de datos')
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
                print(f'La línea {codigo} se ha cargado correctamente')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar la línea: {str(e)}")
            return False
    # MODIFICA EL NOMBRE DE UNA LÍNEA - MODIFICA EL NOMBRE DE UNA LÍNEA
    # MODIFICA EL NOMBRE DE UNA LÍNEA - MODIFICA EL NOMBRE DE UNA LÍNEA
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
    # ELIMINA UNA LÍNEA Y SUS GRUPOS ASOCIADOS - ELIMINA UNA LÍNEA Y SUS GRUPOS ASOCIADOS
    # ELIMINA UNA LÍNEA Y SUS GRUPOS ASOCIADOS - ELIMINA UNA LÍNEA Y SUS GRUPOS ASOCIADOS
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
    # AGREGA UN GRUPO A UNA LÍNEA EXISTENTE - AGREGA UN GRUPO A UNA LÍNEA EXISTENTE -
    # AGREGA UN GRUPO A UNA LÍNEA EXISTENTE - AGREGA UN GRUPO A UNA LÍNEA EXISTENTE -
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
    def Add_GroupNM(self, linea, codigo_interno, nombre_grupo, porcentaje1, porcentaje2, porcentaje3):
        full_codigo = f"{linea}.{codigo_interno}"
        try:
            with self.conn.cursor() as cur:
                # Verificar que la línea exista
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (linea,))
                if not cur.fetchone():
                    print(f'La línea con código {linea} no existe')
                    return False

                # Verificar si el grupo ya existe en esa línea (usando el código concatenado)
                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, full_codigo))
                if cur.fetchone():
                    print(f'El grupo con código {full_codigo} ya existe en la línea {linea}')
                    return False

                cur.execute("""
                    INSERT INTO grupos (codigo, linea, nombre, porcentaje1, porcentaje2, porcentaje3)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (full_codigo, linea, nombre_grupo, porcentaje1, porcentaje2, porcentaje3))
                self.conn.commit()
                print(f'El grupo {full_codigo} - {nombre_grupo} se ha agregado correctamente a la línea {linea}')
                return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error al agregar el grupo: {str(e)}")
            return False
    # MODIFICA LOS DATOS DE UN GRUPO EXISTENTE - MODIFICA LOS DATOS DE UN GRUPO EXISTENTE
    # MODIFICA LOS DATOS DE UN GRUPO EXISTENTE - MODIFICA LOS DATOS DE UN GRUPO EXISTENTE
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
    # ELIMINA UN GRUPO DE UNA LÍNEA - ELIMINA UN GRUPO DE UNA LÍNEA
    # ELIMINA UN GRUPO DE UNA LÍNEA - ELIMINA UN GRUPO DE UNA LÍNEA
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
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
# OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS - OBTENCION DE DATOS -
    # RETORNA UNA LINEA - RETORNA UNA LINEA - RETORNA UNA LINEA - RETORNA UNA LINEA -
    # RETORNA UNA LINEA - RETORNA UNA LINEA - RETORNA UNA LINEA - RETORNA UNA LINEA -
    def GetLine(self,linea):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT codigo,nombre FROM lineas WHERE codigo = %s", (linea,))
                row = cur.fetchone()
                codigo, nombre = row
                linea_data = {
                    "codigo":codigo,
                    "nombre":nombre,
                }
            return linea_data
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al buscar línea: {str(e)}")
            return
    # RETORNA UN GRUPO - RETORNA UN GRUPO - RETORNA UN GRUPO - RETORNA UN GRUPO -
    # RETORNA UN GRUPO - RETORNA UN GRUPO - RETORNA UN GRUPO - RETORNA UN GRUPO -
    def GetGroup(self,linea,grupo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT codigo, nombre, porcentaje1, porcentaje2, porcentaje3 FROM grupos
                            WHERE linea = %s AND codigo = %s""", (linea,grupo))
                row = cur.fetchone()
                codigo,nombre,precio1,precio2,precio3 = row
                group_data = {
                    'codigo':codigo,
                    'nombre':nombre,
                    'precio1':precio1,
                    'precio2':precio2,
                    'precio3':precio3,
                }
            return group_data
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al buscar grupo: {str(e)}")
            return
    # RETORNA LOS NOMBRES DE LÍNEA EN FORMATO (CÓDIGO - NOMBRE)
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
    # RETORNA LOS PORCENTAJES DE UN GRUPO
    # RETORNA LOS PORCENTAJES DE UN GRUPO
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
    # BUSCAR LINEA POR NOMBRE - BUSCAR LINEA POR NOMBRE - BUSCAR LINEA POR NOMBRE -
    # BUSCAR LINEA POR NOMBRE - BUSCAR LINEA POR NOMBRE - BUSCAR LINEA POR NOMBRE -
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
    # BUSCAR GRUPO POR NOMBRE - BUSCAR GRUPO POR NOMBRE - BUSCAR GRUPO POR NOMBRE -
    # BUSCAR GRUPO POR NOMBRE - BUSCAR GRUPO POR NOMBRE - BUSCAR GRUPO POR NOMBRE -
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
    # ---------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
# VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS -
# VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS -
# VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS -
# VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS - VERIFICACION DE DATOS -
    # CHEQUEA SI LA LÍNEA EXISTE - CHEQUEA SI LA LÍNEA EXISTE - CHEQUEA SI LA LÍNEA EXISTE -
    # CHEQUEA SI LA LÍNEA EXISTE - CHEQUEA SI LA LÍNEA EXISTE - CHEQUEA SI LA LÍNEA EXISTE -
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
    def CheckLineNM(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM lineas WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    return True
                else:
                    print(f'El código {codigo} no pertenece a ninguna línea cargada.')
                    return False
        except Exception as e:
            print(f"Error al chequear la línea: {str(e)}")
            return False
    # CHEQUEA SI UN GRUPO PERTENECE A LA LÍNEA - CHEQUEA SI UN GRUPO PERTENECE A LA LÍNEA -
    # CHEQUEA SI UN GRUPO PERTENECE A LA LÍNEA - CHEQUEA SI UN GRUPO PERTENECE A LA LÍNEA -
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
    def CheckGrupoNM(self, linea, grupo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM grupos WHERE linea = %s AND codigo = %s;", (linea, grupo))
                if cur.fetchone():
                    return True
                else:
                    print(f'El grupo {grupo} no pertenece a la línea {linea}.')
                    return False
        except Exception as e:
            print(f"Error al chequear el grupo: {str(e)}")
            return False
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
# CIERRA LA CONEXIÓN AL DESTRUIR EL OBJETO
# CIERRA LA CONEXIÓN AL DESTRUIR EL OBJETO
    def __del__(self):
        if self.conn:
            self.conn.close()