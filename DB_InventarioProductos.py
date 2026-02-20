import psycopg2
from tkinter import messagebox
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - 
# PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - PRODUCT CLASS - 
class Product:
    def __init__(self, codigo, linea, grupo, proveedor,
                 nombre, costo, ubicacion1, ubicacion2,
                 pv1, pv2, pv3, existencia=0,image='Recursos/Imagenes/Productos/Default.png'):
        self.codigo = codigo
        self.linea = linea
        self.grupo = grupo
        self.proveedor = proveedor
        self.nombre = nombre
        self.costo = costo
        self.ubicacion1 = ubicacion1
        self.ubicacion2 = ubicacion2
        self.precio_venta_1 = pv1
        self.precio_venta_2 = pv2
        self.precio_venta_3 = pv3
        self.existencia = existencia
        self.image = image
    # REGRESA EL DICCIONARIO DE UN PRODUCTO
    # REGRESA EL DICCIONARIO DE UN PRODUCTO
    def ToDict(self):
        return {
            'codigo': self.codigo,
            'linea': self.linea,
            'grupo': self.grupo,
            'proveedor': self.proveedor,
            'nombre': self.nombre,
            'costo': self.costo,
            'ubicacion1': self.ubicacion1,
            'ubicacion2': self.ubicacion2,
            'precio1': self.precio_venta_1,
            'precio2': self.precio_venta_2,
            'precio3': self.precio_venta_3,
            'existencia': self.existencia,
            'image':self.image}
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - 
# CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - 
class Inventory:
    def __init__(self, dbname,user,password,host,port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()
    # CONNECT TO DATABASE - CONNECT TO DATABASE - CONNECT TO DATABASE - CONNECT TO DATABASE - 
    # CONNECT TO DATABASE - CONNECT TO DATABASE - CONNECT TO DATABASE - CONNECT TO DATABASE - 
    def connect_db(self):
        # CONNECT TO DATABASE
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port)
        except Exception as e:
            messagebox.showerror("Database Connection Error", f"Error conectando a la base de datos: {str(e)}")
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
# CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - CRUD - 
    # ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - 
    # ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - ADD PRODUCT - 
    def AddProduct(self, product):
        try:
            with self.conn.cursor() as cur:
                # VALIDATE PRODUCT
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s;", (product['codigo'],))
                if cur.fetchone():
                    messagebox.showinfo('Producto existente', f"El producto con el código {product['codigo']} ya existe.")
                    return
                if product['codigo'] == '':
                    messagebox.showerror('Error', "Agregue un código de producto.")
                    return
                # INSERT NEW PRODUCT
                cur.execute("""
                    INSERT INTO productos 
                        (codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia,image)
                    VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    product['codigo'], product['linea'], product['grupo'], product['proveedor'],
                    product['nombre'], product['costo'], product['ubicacion1'], product['ubicacion2'],
                    product['precio1'], product['precio2'], product['precio3'], product.get('existencia', 0),
                    product['image']
                ))
                self.conn.commit()
                messagebox.showinfo('Producto agregado', f"El producto {product['codigo']} ha sido agregado.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error agregando producto: {str(e)}")
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - 
    # MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - MOD PRODUCT - 
    def EditProduct(self, product):
        """
        Modifica los datos del producto utilizando su código.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE productos SET
                        linea = %s,
                        grupo = %s,
                        proveedor = %s,
                        nombre = %s,
                        costo = %s,
                        ubicacion1 = %s,
                        ubicacion2 = %s,
                        precio1 = %s,
                        precio2 = %s,
                        precio3 = %s,
                        image = %s
                    WHERE codigo = %s;
                """, (
                    product['linea'], product['grupo'], product['proveedor'],
                    product['nombre'], product['costo'], product['ubicacion1'], product['ubicacion2'],
                    product['precio1'], product['precio2'], product['precio3'],
                    product['image'],product['codigo']
                ))
                self.conn.commit()
                messagebox.showinfo('Producto modificado', f"El producto {product['codigo']} ha sido modificado.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error modificando producto: {str(e)}")
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - 
    # EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - EDIT PRICE - 
    def EditPrecio(self, codigo, p1, p2, p3):
        """
        Modifica únicamente los precios de un producto existente.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE productos SET
                        precio1 = %s,
                        precio2 = %s,
                        precio3 = %s
                    WHERE codigo = %s;
                """, (p1, p2, p3, codigo))
                self.conn.commit()
                messagebox.showinfo('Producto modificado', f"Los precios del producto {codigo} han sido modificados.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error modificando precios del producto: {str(e)}")
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - 
    # DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - DEL PRODUCT - 
    def DelProduct(self, codigo):
        """Eliminación LÓGICA del producto (marca como inactivo en lugar de eliminar)."""
        try:
            with self.conn.cursor() as cur:
                # Verificar si el producto existe
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s;", (codigo,))
                if not cur.fetchone():
                    messagebox.showerror('Error', f"El producto {codigo} no existe.")
                    return
                # Marcar como inactivo en lugar de eliminar
                cur.execute("UPDATE productos SET activo = FALSE WHERE codigo = %s;", (codigo,))
                self.conn.commit()
                messagebox.showinfo('Producto Desactivado', f"El producto {codigo} ha sido marcado como inactivo.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error desactivando producto: {str(e)}")
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
# GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - 
# GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - J
# GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - 
# GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - GET INFO - 
    # GET WHOLE INVENTORY - GET WHOLE INVENTORY - GET WHOLE INVENTORY - GET WHOLE INVENTORY
    # GET WHOLE INVENTORY - GET WHOLE INVENTORY - GET WHOLE INVENTORY - GET WHOLE INVENTORY
    def GetInventory(self):
       # GET ALL PRODUCTS AND RETURN A DICTIONARY
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image
                    FROM productos WHERE activo = TRUE;
                """)
                rows = cur.fetchall()
                inventory = {}
                for r in rows:
                    codigo, linea, grupo, proveedor, nombre, costo,ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image = r
                    inventory[codigo] = {
                        'codigo': codigo,
                        'linea': linea,
                        'grupo': grupo,
                        'proveedor': proveedor,
                        'nombre': nombre,
                        'costo': costo,
                        'ubicacion1': ubicacion1,
                        'ubicacion2': ubicacion2,
                        'precio1': precio1,
                        'precio2': precio2,
                        'precio3': precio3,
                        'existencia': existencia,
                        'image': image
                    }
                return inventory
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return {}
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - 
    # GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - GET INACTIVES - 
    def GetInactives(self):
       # GET ALL INACTIVE PRODUCTS AND RETURN A DICTIONARY
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image
                    FROM productos WHERE activo = FALSE;
                """)
                rows = cur.fetchall()
                inventory = {}
                for r in rows:
                    codigo, linea, grupo, proveedor, nombre, costo,ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image = r
                    inventory[codigo] = {
                        'codigo': codigo,
                        'linea': linea,
                        'grupo': grupo,
                        'proveedor': proveedor,
                        'nombre': nombre,
                        'costo': costo,
                        'ubicacion1': ubicacion1,
                        'ubicacion2': ubicacion2,
                        'precio1': precio1,
                        'precio2': precio2,
                        'precio3': precio3,
                        'existencia': existencia,
                        'image': image
                    }
                return inventory
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return {}
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # GET ALL INVENTORY CODES - GET ALL INVENTORY CODES - GET ALL INVENTORY CODES
    # GET ALL INVENTORY CODES - GET ALL INVENTORY CODES - GET ALL INVENTORY CODES
    def GetCodigos(self):
        # RETURN A LIST OF ALL THE INVENTORY CODES
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo FROM productos WHERE activo = TRUE;
                """)
                rows = cur.fetchall()
                inventory = [r[0] for r in rows]
                return inventory
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return {}
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - 
    # GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - GET PRODUCT - 
    def GetProducto(self,codigo):
        # RETURN A DICT OF A PRODUCT
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image
                    FROM productos WHERE codigo = %s AND activo = TRUE;""", (codigo,))
                row = cur.fetchone()
                producto = {}
                codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image = row
                producto = {
                    'codigo': codigo,
                    'linea': linea,
                    'grupo': grupo,
                    'proveedor': proveedor,
                    'nombre': nombre,
                    'costo': costo,
                    'ubicacion1': ubicacion1,
                    'ubicacion2': ubicacion2,
                    'precio1': precio1,
                    'precio2': precio2,
                    'precio3': precio3,
                    'existencia': existencia,
                    'image': image
                }
                return producto
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return None
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - 
    # SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - SEARCH NY NAME - 
    def BuscarNombres(self, busqueda):
        # SEARCH PRODUCTS BY NAME USING A STRIGN
        try: 
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image
                    FROM productos
                    WHERE nombre ILIKE %s AND activo = TRUE;
                """, ('%' + busqueda + '%',))
                rows = cur.fetchall()
                resultados = []
                for r in rows:
                    codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia, image = r
                    resultados.append({
                        'codigo': codigo,
                        'linea': linea,
                        'grupo': grupo,
                        'proveedor': proveedor,
                        'nombre': nombre,
                        'costo': costo,
                        'ubicacion1': ubicacion1,
                        'ubicacion2': ubicacion2,
                        'precio1': precio1,
                        'precio2': precio2,
                        'precio3': precio3,
                        'existencia': existencia,
                        'image': image
                    })
                return resultados
        except Exception as e:
            messagebox.showerror('Error', f"Error buscando producto: {str(e)}")
            return []
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
# VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - 
# VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - 
# VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - 
# VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - VALIDATE INFO - 
    # CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - 
    # CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - CHECK A PRODUCT CODE - 
    def CheckCode(self, codigo):
        # CHECKS IF A CODE ALREADY EXISTS IN THE DATABASE AND IF SO, SHOWS ERROR
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s AND activo = TRUE;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror('Error', f'El código {codigo} ya se encuentra en la base de datos.')
                    return False
                else:
                    return True
        except Exception as e:
            return False
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - 
    # CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - CHECK INACTIVE - 
    def CheckInactive(self, codigo):
        # CHECKS IF A CODE IS INACTIVE
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s AND activo = FALSE;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror('Base de datos', f"El código {codigo} está en la base de datos pero se encuentra inactivo.")
                    return True
                else:
                    return False
        except Exception as e:
            return False
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - 
    # VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - VALIDATE PRODUCT CODE - 
    def CheckCodeValidate(self, codigo):
        # CHECKS IF A CODE ALREADY EXISTS IN THE DATABASE AND IF DONT, SHOWS ERROR
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s AND activo = TRUE;", (codigo,))
                if cur.fetchone():
                    return True
                else:
                    messagebox.showerror('Error', f'El código {codigo} no se encuentra en la base de datos.')
                    return False
        except Exception as e:
            messagebox.showerror('Error', f"Error verificando código: {str(e)}")
            return False
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
# DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - 
# DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - 
# DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - 
# DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - DATA ENTRY - 
    # SAVES A ENTRY TO INVENTORY - SAVES A ENTRY TO INVENTORY - SAVES A ENTRY TO INVENTORY - SAVES A ENTRY TO INVENTORY - 
    
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------

    def __del__(self):
        """Cierra la conexión a la base de datos cuando el objeto se destruye."""
        if self.conn:
            self.conn.close()
