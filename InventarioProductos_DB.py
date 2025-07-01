import psycopg2
from tkinter import messagebox

# CLASE PRODUCTO (la dejamos igual, ya que solo es un contenedor de datos)
class Product:
    def __init__(self, codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, pv1, pv2, pv3, existencia=0):
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
            'existencia': self.existencia
        }

# CLASE INVENTARIO (ahora utilizando PostgreSQL en lugar de JSON)
class Inventory:
    def __init__(self, dbname,user,password,host,port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.connect_db()

    def connect_db(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            messagebox.showerror("Database Connection Error", f"Error conectando a la base de datos: {str(e)}")

    def AddProduct(self, product):
        """
        Agrega un producto nuevo a la tabla 'productos'.
        Primero se verifica si ya existe el código. 
        """
        try:
            with self.conn.cursor() as cur:
                # Verificar si el producto ya existe
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s;", (product['codigo'],))
                if cur.fetchone():
                    messagebox.showinfo('Producto existente', f"El producto con el código {product['codigo']} ya existe.")
                    return
                if product['codigo'] == '':
                    messagebox.showerror('Error', "Agregue un código de producto.")
                    return

                # Insertar el nuevo producto
                cur.execute("""
                    INSERT INTO productos 
                        (codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia)
                    VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    product['codigo'], product['linea'], product['grupo'], product['proveedor'],
                    product['nombre'], product['costo'], product['ubicacion1'], product['ubicacion2'],
                    product['precio1'], product['precio2'], product['precio3'], product.get('existencia', 0)
                ))
                self.conn.commit()
                messagebox.showinfo('Producto agregado', f"El producto {product['codigo']} ha sido agregado.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error agregando producto: {str(e)}")

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
                        existencia = %s
                    WHERE codigo = %s;
                """, (
                    product['linea'], product['grupo'], product['proveedor'],
                    product['nombre'], product['costo'], product['ubicacion1'], product['ubicacion2'],
                    product['precio1'], product['precio2'], product['precio3'], product.get('existencia', 0),
                    product['codigo']
                ))
                self.conn.commit()
                messagebox.showinfo('Producto modificado', f"El producto {product['codigo']} ha sido modificado.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error modificando producto: {str(e)}")

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

    def DelProduct(self, codigo):
        """
        Elimina el producto de la base de datos utilizando su código.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM productos WHERE codigo = %s;", (codigo,))
                self.conn.commit()
                messagebox.showinfo('Producto Eliminado', "El producto ha sido eliminado.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error eliminando producto: {str(e)}")

    def GetInventory(self):
        """
        Obtiene todos los productos de la tabla 'productos' y los devuelve en forma de diccionario.
        Cada clave es el 'codigo' del producto.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia 
                    FROM productos;
                """)
                rows = cur.fetchall()
                inventory = {}
                for r in rows:
                    codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia = r
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
                        'existencia': existencia
                    }
                return inventory
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return {}
    def GetCodigos(self):
        """
        Obtiene todos los codigos de producto productos de la tabla 'productos' y los devuelve en forma de lista.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo FROM productos;
                """)
                rows = cur.fetchall()
                inventory = [r[0] for r in rows]
                return inventory
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return {}
        
    def GetProducto(self,codigo):
        """
        Obtiene un  producto de la tabla 'productos' y los devuelve en forma de diccionario.
        Cada clave es el 'codigo' del producto.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia 
                    FROM productos WHERE codigo = %s;""", (codigo,))
                row = cur.fetchone()
                producto = {}
                codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia = row
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
                    'existencia': existencia
                }
                return producto
        except Exception as e:
            messagebox.showerror('Error', f"Error obteniendo el inventario: {str(e)}")
            return None

    def BuscarNombres(self, busqueda):
        """
        Busca productos cuyo nombre contenga la cadena de búsqueda (sin importar mayúsculas/minúsculas).
        Devuelve una lista de diccionarios con los productos encontrados.
        """
        try: 
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia 
                    FROM productos
                    WHERE nombre ILIKE %s;
                """, ('%' + busqueda + '%',))
                rows = cur.fetchall()
                resultados = []
                for r in rows:
                    codigo, linea, grupo, proveedor, nombre, costo, ubicacion1, ubicacion2, precio1, precio2, precio3, existencia = r
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
                        'existencia': existencia
                    })
                return resultados
        except Exception as e:
            messagebox.showerror('Error', f"Error buscando producto: {str(e)}")
            return []

    # VERIFICAR SI UN CODIGO YA EXISTE PARA EVITAR DOBLE CARGA DE CODIGO
    def CheckCode(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    messagebox.showerror('Error', f'El código {codigo} ya se encuentra en la base de datos.')
                    return False
                else:
                    return True
        except Exception as e:
            return False
    # VERIFICAR SI UN CODIGO DE PRODUCTO
    def CheckCodeValidate(self, codigo):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM productos WHERE codigo = %s;", (codigo,))
                if cur.fetchone():
                    return True
                else:
                    messagebox.showerror('Error', f'El código {codigo} no se encuentra en la base de datos.')
                    return False
        except Exception as e:
            messagebox.showerror('Error', f"Error verificando código: {str(e)}")
            return False

    def CheckName(self, name):
        """
        Valida que se haya ingresado un nombre para el producto.
        """
        if name == '':
            messagebox.showerror('Error', 'Ingrese un nombre de producto')
            return False
        return True

    def GuardarEntradaInventario(self,
                                 num_factura: str,
                                 proveedor: int,
                                 fecha: str,
                                 total: float,
                                 detalle_entrada: list):
        """
        Inserta en entradas_inventario y detalle_entrada.
        Cada línea en detalle_entrada debe contener:
          codigo, cantidad, costo, descuento1, descuento2, descuento3,
          flete, iva, neto, neto_iva, subtotal
        """
        try:
            with self.conn.cursor() as cur:
                # Cabecera
                cur.execute("""
                    INSERT INTO entradas_inventario
                      (num_factura, proveedor, fecha, total)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (num_factura, proveedor, fecha, total))
                entrada_id = cur.fetchone()[0]

                # Detalle por línea
                for item in detalle_entrada:
                    cur.execute("""
                        INSERT INTO detalle_entrada
                          (entrada_id, codigo, cantidad, costo,
                           descuento1, descuento2, descuento3,
                           flete, iva, neto, neto_iva, subtotal)
                        VALUES (%s, %s, %s, %s,  %s, %s, %s,  %s, %s, %s, %s, %s);
                    """, (
                        entrada_id,
                        item['codigo'],
                        item['cantidad'],
                        item['costo'],
                        item['descuento1'],
                        item['descuento2'],
                        item['descuento3'],
                        item['flete'],
                        item['iva'],
                        item['neto'],
                        item['neto_iva'],
                        item['subtotal'],
                    ))

                    # Actualizar stock
                    cur.execute("""
                        UPDATE productos
                        SET existencia = existencia + %s
                        WHERE codigo = %s;
                    """, (item['cantidad'], item['codigo']))

                self.conn.commit()
                messagebox.showinfo("Éxito", "Entrada guardada correctamente.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error BD",
                                  f"Al guardar la entrada: {str(e)}")
            raise

    def ObtenerEntrada(self, num_factura: str) -> dict | None:
        """
        Devuelve None si no existe. Si existe, retorna:
        {
          'id': int,
          'num_factura': str,
          'proveedor': int,
          'nombre_proveedor': str,
          'fecha': date,
          'total': float,
          'detalle': [
              {
                'codigo': str,
                'nombre': str,
                'cantidad': int,
                'costo': float,
                'descuento1': float,
                'descuento2': float,
                'descuento3': float,
                'flete': float,
                'iva': float,
                'neto': float,
                'neto_iva': float,
                'subtotal': float
              }, …
          ]
        }
        """
        with self.conn.cursor() as cur:
            # 1) Cabecera
            cur.execute("""
                SELECT e.id, e.proveedor, p.nombre, e.fecha, e.total
                  FROM entradas_inventario e
                  JOIN proveedores p ON p.codigo = e.proveedor
                 WHERE e.num_factura = %s;
            """, (num_factura,))
            row = cur.fetchone()
            if not row:
                return None
            entrada_id, prov, nombre_prov, fecha, total = row

            # 2) Detalle
            cur.execute("""
                SELECT d.codigo, pr.nombre, d.cantidad, d.costo,
                       d.descuento1, d.descuento2, d.descuento3,
                       d.flete, d.iva, d.neto, d.neto_iva, d.subtotal
                  FROM detalle_entrada d
                  JOIN productos pr ON pr.codigo = d.codigo
                 WHERE d.entrada_id = %s;
            """, (entrada_id,))
            detalles = []
            for (codigo, nombre, cantidad, costo,
                 d1, d2, d3, flete, iva, neto, neto_iva, subtotal) in cur.fetchall():
                detalles.append({
                    'codigo':     codigo,
                    'nombre':     nombre,
                    'cantidad':   cantidad,
                    'costo':      float(costo),
                    'descuento1': float(d1),
                    'descuento2': float(d2),
                    'descuento3': float(d3),
                    'flete':      float(flete),
                    'iva':        float(iva),
                    'neto':       float(neto),
                    'neto_iva':   float(neto_iva),
                    'subtotal':   float(subtotal)
                })

            return {
                'id':               entrada_id,
                'num_factura':      num_factura,
                'proveedor':        prov,
                'nombre_proveedor': nombre_prov,
                'fecha':            fecha,
                'total':            float(total),
                'detalle':          detalles
            }





    def __del__(self):
        """Cierra la conexión a la base de datos cuando el objeto se destruye."""
        if self.conn:
            self.conn.close()
