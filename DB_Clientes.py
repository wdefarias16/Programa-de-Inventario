import psycopg2
from tkinter import messagebox

class Clientes:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.dbuser = user
        self.dbpassword = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()
        # CREATE DEFAULT CLIENT
        self.CreateDefaultClient()
    # CONECTARSE A LA BASE DE DATOS
    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.dbuser,
                password=self.dbpassword,
                host=self.host,
                port=self.port)
        except Exception as e:
            messagebox.showerror("Base de datos", f"Error al conectarse a la base de datos: {e}")
# CREAR CLIENTE POR DEFECTO - CREAR CLIENTE POR DEFECTO - CREAR CLIENTE POR DEFECTO -
# CREAR CLIENTE POR DEFECTO - CREAR CLIENTE POR DEFECTO - CREAR CLIENTE POR DEFECTO -
    def CreateDefaultClient(self):
        """
        Crea un cliente por defecto sin datos específicos.
        Útil para ventas rápidas o cuando no se requiere información del cliente.
        """
        default_codigo = 999
        default_nombre = "CLIENTE GENERAL"
        default_id_fiscal = "000000000"
        default_telefono = "000-0000000"
        default_direccion1 = "SIN DIRECCIÓN"
        default_direccion2 = ""
        default_ciudad = "CIUDAD"
        default_email = "cliente@general.com"
        
        try:
            with self.conn.cursor() as cur:
                # Verificar si ya existe el cliente general
                cur.execute("SELECT 1 FROM clientes WHERE nombre = %s;", (default_nombre,))
                if cur.fetchone() is None:
                    # Si no existe, se crea el cliente por defecto
                    cur.execute("""
                        INSERT INTO clientes (codigo,nombre, id_fiscal, telefono, direccion1, 
                                            direccion2, ciudad, email, activo)
                        VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s);
                    """, (default_codigo,default_nombre, default_id_fiscal, default_telefono,
                          default_direccion1, default_direccion2, default_ciudad, 
                          default_email, True))
                    self.conn.commit()
                    messagebox.showinfo("Base de Datos", "Cliente general creado correctamente.")
                    return True
                else:
                    messagebox.showinfo("Base de Datos", "El cliente general ya existe.")
                    return False
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Base de datos", f"Error creando cliente por defecto: {e}")
            return False

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -
    # CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD -

    # AGREGAR NUEVO CLIENTE - AGREGAR NUEVO CLIENTE - AGREGAR NUEVO CLIENTE -
    # AGREGAR NUEVO CLIENTE - AGREGAR NUEVO CLIENTE - AGREGAR NUEVO CLIENTE -
    def AddClient(self, nombre, id_fiscal, telefono="", direccion1="", direccion2="", 
                 ciudad="", email="", activo=True):
        """
        Agrega un nuevo cliente a la base de datos.
        
        Args:
            nombre (str): Nombre completo del cliente
            id_fiscal (str): Identificación fiscal (RUC, Cédula, etc.)
            telefono (str): Número de teléfono
            direccion1 (str): Dirección principal
            direccion2 (str): Dirección secundaria (opcional)
            ciudad (str): Ciudad
            email (str): Correo electrónico
            activo (bool): Estado del cliente (activo/inactivo)
        """
        try:
            # Validaciones básicas
            if not nombre or not id_fiscal:
                raise ValueError("El nombre y la identificación fiscal son obligatorios.")
            
            if len(id_fiscal) < 3:
                raise ValueError("La identificación fiscal debe tener al menos 3 caracteres.")

            with self.conn.cursor() as cur:
                # Verificar si el cliente ya existe usando id_fiscal
                cur.execute("SELECT 1 FROM clientes WHERE id_fiscal = %s;", (id_fiscal,))
                if cur.fetchone():
                    raise ValueError("Ya existe un cliente con esta identificación fiscal.")

                # Insertar nuevo cliente
                cur.execute("""
                    INSERT INTO clientes (nombre, id_fiscal, telefono, direccion1, 
                                        direccion2, ciudad, email, activo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (nombre, id_fiscal, telefono, direccion1, direccion2, ciudad, email, activo))
                
                self.conn.commit()
                messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
                return True
                
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error al agregar el cliente: {e}")
            return False

    # ELIMINAR CLIENTE - ELIMINAR CLIENTE - ELIMINAR CLIENTE - ELIMINAR CLIENTE -
    # ELIMINAR CLIENTE - ELIMINAR CLIENTE - ELIMINAR CLIENTE - ELIMINAR CLIENTE -
    def DeleteClient(self, codigo):
        """
        Elimina un cliente de la base de datos.
        
        Args:
            codigo (int): Código único del cliente
        """
        try:
            with self.conn.cursor() as cur:
                # Verificar si el cliente existe
                cur.execute("SELECT nombre FROM clientes WHERE codigo = %s;", (codigo,))
                cliente = cur.fetchone()
                
                if not cliente:
                    raise ValueError("El cliente no existe.")
                
                # Confirmar eliminación
                confirmar = messagebox.askyesno(
                    "Confirmar Eliminación", 
                    f"¿Está seguro de eliminar al cliente: {cliente[0]}?"
                )
                
                if confirmar:
                    cur.execute("DELETE FROM clientes WHERE codigo = %s;", (codigo,))
                    self.conn.commit()
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                    return True
                else:
                    return False
                    
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error al eliminar el cliente: {e}")
            return False

    # ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE -
    # ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE - ACTUALIZAR CLIENTE -
    def UpdateClient(self, codigo, nombre, id_fiscal, telefono, direccion1, 
                    direccion2, ciudad, email, activo):
        """
        Actualiza la información de un cliente existente.
        
        Args:
            codigo (int): Código único del cliente
            nombre (str): Nombre completo del cliente
            id_fiscal (str): Identificación fiscal
            telefono (str): Número de teléfono
            direccion1 (str): Dirección principal
            direccion2 (str): Dirección secundaria
            ciudad (str): Ciudad
            email (str): Correo electrónico
            activo (bool): Estado del cliente
        """
        try:
            # Validaciones básicas
            if not nombre or not id_fiscal:
                raise ValueError("El nombre y la identificación fiscal son obligatorios.")

            with self.conn.cursor() as cur:
                # Verificar si el id_fiscal ya existe en otro cliente
                cur.execute("""
                    SELECT 1 FROM clientes 
                    WHERE id_fiscal = %s AND codigo != %s;
                """, (id_fiscal, codigo))
                
                if cur.fetchone():
                    raise ValueError("Ya existe otro cliente con esta identificación fiscal.")

                # Actualizar cliente
                cur.execute("""
                    UPDATE clientes
                    SET nombre = %s, id_fiscal = %s, telefono = %s, 
                        direccion1 = %s, direccion2 = %s, ciudad = %s, 
                        email = %s, activo = %s
                    WHERE codigo = %s;
                """, (nombre, id_fiscal, telefono, direccion1, direccion2, 
                      ciudad, email, activo, codigo))
                
                if cur.rowcount == 0:
                    raise ValueError("El cliente no existe.")
                
                self.conn.commit()
                messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
                return True
                
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error al actualizar el cliente: {e}")
            return False

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS -
    # OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS - OBTENCIÓN DE DATOS -

    # OBTENER TODOS LOS CLIENTES - OBTENER TODOS LOS CLIENTES - OBTENER TODOS LOS CLIENTES -
    # OBTENER TODOS LOS CLIENTES - OBTENER TODOS LOS CLIENTES - OBTENER TODOS LOS CLIENTES -
    def GetAllClients(self, solo_activos=False):
        """
        Obtiene todos los clientes de la base de datos.
        
        Args:
            solo_activos (bool): Si es True, solo devuelve clientes activos
            
        Returns:
            list: Lista de diccionarios con información de clientes
        """
        clients = []
        try:
            with self.conn.cursor() as cur:
                if solo_activos:
                    cur.execute("""
                        SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                               direccion2, ciudad, email, activo 
                        FROM clientes 
                        WHERE activo = TRUE 
                        ORDER BY nombre;
                    """)
                else:
                    cur.execute("""
                        SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                               direccion2, ciudad, email, activo 
                        FROM clientes 
                        ORDER BY nombre;
                    """)
                
                rows = cur.fetchall()
                for row in rows:
                    client = {
                        'codigo': row[0],
                        'nombre': row[1],
                        'id_fiscal': row[2],
                        'telefono': row[3],
                        'direccion1': row[4],
                        'direccion2': row[5],
                        'ciudad': row[6],
                        'email': row[7],
                        'activo': row[8]
                    }
                    clients.append(client)
                    
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener los clientes: {e}")
            
        return clients

    # OBTENER CLIENTE POR CÓDIGO - OBTENER CLIENTE POR CÓDIGO - OBTENER CLIENTE POR CÓDIGO -
    # OBTENER CLIENTE POR CÓDIGO - OBTENER CLIENTE POR CÓDIGO - OBTENER CLIENTE POR CÓDIGO -
    def GetClientByCode(self, codigo):
        """
        Obtiene un cliente específico por su código.
        
        Args:
            codigo (int): Código del cliente
            
        Returns:
            dict: Información del cliente o None si no existe
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                           direccion2, ciudad, email, activo
                    FROM clientes 
                    WHERE codigo = %s;
                """, (codigo,))
                
                row = cur.fetchone()
                if row:
                    client_data = {
                        'codigo': row[0],
                        'nombre': row[1],
                        'id_fiscal': row[2],
                        'telefono': row[3],
                        'direccion1': row[4],
                        'direccion2': row[5],
                        'ciudad': row[6],
                        'email': row[7],
                        'activo': row[8]
                    }
                    return client_data
                else:
                    return None
                    
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el cliente: {e}")
            return None

    # OBTENER CLIENTE POR ID FISCAL - OBTENER CLIENTE POR ID FISCAL - OBTENER CLIENTE POR ID FISCAL -
    # OBTENER CLIENTE POR ID FISCAL - OBTENER CLIENTE POR ID FISCAL - OBTENER CLIENTE POR ID FISCAL -
    def GetClientByFiscalId(self, id_fiscal):
        """
        Obtiene un cliente por su identificación fiscal.
        
        Args:
            id_fiscal (str): Identificación fiscal del cliente
            
        Returns:
            dict: Información del cliente o None si no existe
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                           direccion2, ciudad, email, activo
                    FROM clientes 
                    WHERE id_fiscal = %s;
                """, (id_fiscal,))
                
                row = cur.fetchone()
                if row:
                    client_data = {
                        'codigo': row[0],
                        'nombre': row[1],
                        'id_fiscal': row[2],
                        'telefono': row[3],
                        'direccion1': row[4],
                        'direccion2': row[5],
                        'ciudad': row[6],
                        'email': row[7],
                        'activo': row[8]
                    }
                    return client_data
                else:
                    return None
                    
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el cliente: {e}")
            return None

    # BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES -
    # BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES - BUSCAR CLIENTES -
    def SearchClients(self, search_term, solo_activos=True):
        """
        Busca clientes por nombre o identificación fiscal.
        
        Args:
            search_term (str): Término de búsqueda
            solo_activos (bool): Si es True, solo busca en clientes activos
            
        Returns:
            list: Lista de clientes que coinciden con la búsqueda
        """
        clients = []
        try:
            with self.conn.cursor() as cur:
                search_pattern = f"%{search_term}%"
                
                if solo_activos:
                    cur.execute("""
                        SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                               direccion2, ciudad, email, activo
                        FROM clientes 
                        WHERE activo = TRUE AND 
                              (nombre ILIKE %s OR id_fiscal ILIKE %s)
                        ORDER BY nombre;
                    """, (search_pattern, search_pattern))
                else:
                    cur.execute("""
                        SELECT codigo, nombre, id_fiscal, telefono, direccion1, 
                               direccion2, ciudad, email, activo
                        FROM clientes 
                        WHERE nombre ILIKE %s OR id_fiscal ILIKE %s
                        ORDER BY nombre;
                    """, (search_pattern, search_pattern))
                
                rows = cur.fetchall()
                for row in rows:
                    client = {
                        'codigo': row[0],
                        'nombre': row[1],
                        'id_fiscal': row[2],
                        'telefono': row[3],
                        'direccion1': row[4],
                        'direccion2': row[5],
                        'ciudad': row[6],
                        'email': row[7],
                        'activo': row[8]
                    }
                    clients.append(client)
                    
        except Exception as e:
            messagebox.showerror("Error", f"Error en la búsqueda: {e}")
            
        return clients

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS -
    # GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS - GESTIÓN DE ESTADOS -

    # CAMBIAR ESTADO DEL CLIENTE - CAMBIAR ESTADO DEL CLIENTE - CAMBIAR ESTADO DEL CLIENTE -
    # CAMBIAR ESTADO DEL CLIENTE - CAMBIAR ESTADO DEL CLIENTE - CAMBIAR ESTADO DEL CLIENTE -
    def ChangeClientStatus(self, codigo, activo):
        """
        Cambia el estado activo/inactivo de un cliente.
        
        Args:
            codigo (int): Código del cliente
            activo (bool): Nuevo estado (True = activo, False = inactivo)
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE clientes 
                    SET activo = %s 
                    WHERE codigo = %s;
                """, (activo, codigo))
                
                if cur.rowcount == 0:
                    raise ValueError("El cliente no existe.")
                
                self.conn.commit()
                
                estado_texto = "activado" if activo else "desactivado"
                messagebox.showinfo("Éxito", f"Cliente {estado_texto} correctamente.")
                return True
                
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"Error al cambiar el estado: {e}")
            return False

    # OBTENER CLIENTES ACTIVOS - OBTENER CLIENTES ACTIVOS - OBTENER CLIENTES ACTIVOS -
    # OBTENER CLIENTES ACTIVOS - OBTENER CLIENTES ACTIVOS - OBTENER CLIENTES ACTIVOS -
    def GetActiveClients(self):
        """
        Obtiene solo los clientes activos.
        
        Returns:
            list: Lista de clientes activos
        """
        return self.GetAllClients(solo_activos=True)

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # VALIDAR DATOS DEL CLIENTE - VALIDAR DATOS DEL CLIENTE - VALIDAR DATOS DEL CLIENTE -
    # VALIDAR DATOS DEL CLIENTE - VALIDAR DATOS DEL CLIENTE - VALIDAR DATOS DEL CLIENTE -
    def ValidateClientData(self, nombre, id_fiscal, email=""):
        """
        Valida los datos básicos de un cliente antes de insertar o actualizar.
        
        Args:
            nombre (str): Nombre del cliente
            id_fiscal (str): Identificación fiscal
            email (str): Correo electrónico (opcional)
            
        Returns:
            tuple: (bool, str) - (True/False, mensaje de error)
        """
        try:
            # Validar nombre
            if not nombre or len(nombre.strip()) < 2:
                return False, "El nombre debe tener al menos 2 caracteres."
            
            # Validar identificación fiscal
            if not id_fiscal or len(id_fiscal.strip()) < 3:
                return False, "La identificación fiscal debe tener al menos 3 caracteres."
            
            # Validar email si se proporciona
            if email and '@' not in email:
                return False, "El formato del correo electrónico no es válido."
            
            return True, "Datos válidos."
            
        except Exception as e:
            return False, f"Error en validación: {e}"

    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------

    # CIERRA LA CONEXIÓN CUANDO EL OBJETO SE DESTRUYA
    def __del__(self):
        if self.conn:
            self.conn.close()