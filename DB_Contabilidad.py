import psycopg2
from tkinter import messagebox
# --------------------------------------------------------------------------------------
class AccountingDB:
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
# ---------------------------------------------------------------------------
# ACCOUNTING - ACCOUNTING - ACCOUNTING - ACCOUNTING - ACCOUNTING - ACCOUNTING
# ---------------------------------------------------------------------------
    # ----------------------------------------------------------
    # SAVES A ENTRY TO INVENTORY - SAVES A ENTRY TO INVENTORY - 
    # ----------------------------------------------------------
    def GuardarEntradaInventario(self,num_factura: str,proveedor: int,fecha: str,
                                 total: float,detalle_entrada: list):
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
                    # UPDATE STOCK
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
    # ----------------------------------------------------------
    # GET THE DATA FROM AN ENTRY - GET THE DATA FROM AN ENTRY 
    # ----------------------------------------------------------
    def ObtenerEntrada(self, num_factura: str) -> dict | None:
        """
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
                'detalle':          detalles}
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # SAVES AN AJUSTMENT TO INVENTORY - SAVES AN AJUSTMENT TO INVENTORY - SAVES AN AJUSTMENT TO INVENTORY - 
    # SAVES AN AJUSTMENT TO INVENTORY - SAVES AN AJUSTMENT TO INVENTORY - SAVES AN AJUSTMENT TO INVENTORY - 
    def GuardarAjusteInventario(self,
                                 num_documento: str,
                                 motivo: str,
                                 fecha: str,
                                 detalle_ajuste: list):
        """
        Inserta un ajuste en 'ajustes_inventario' y su detalle en 'detalle_ajustes',
        y actualiza la existencia en 'productos'.
        Parámetros:
          - num_documento: identificador único del ajuste.
          - motivo: texto explicando la razón del ajuste.
          - fecha: cadena 'YYYY-MM-DD'.
          - detalle_ajuste: lista de dicts con claves
                'codigo'              (str),
                'cantidad'            (int) existencia anterior,
                'ajuste'              (int) unidades agregadas (+) o restadas (-),
                'final'               (int) existencia resultante.
        """
        try:

            with self.conn.cursor() as cur:
                # 2) Insertar cabecera del ajuste
                cur.execute("""
                    INSERT INTO ajustes_inventario
                      (num_documento, log, fecha)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                """, (
                    num_documento,
                    motivo,
                    fecha
                ))
                ajuste_id = cur.fetchone()[0]
                # 3) Insertar cada línea de detalle y actualizar stock
                for item in detalle_ajuste:
                    cur.execute("""
                        INSERT INTO detalle_ajustes
                          (ajuste_id, codigo, cantidad, ajuste, final)
                        VALUES (%s, %s, %s, %s, %s);
                    """, (
                        ajuste_id,
                        item['codigo'],
                        item['cantidad'],
                        item['ajuste'],
                        item['final']
                    ))
                    cur.execute("""
                        UPDATE productos
                           SET existencia = %s
                         WHERE codigo = %s;
                    """, (
                        item['final'],
                        item['codigo']
                    ))

                # 4) Confirmar transacción
                self.conn.commit()
                messagebox.showinfo(
                    "Éxito",
                    f"Ajuste {num_documento} guardado correctamente.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror(
                "Error al guardar ajuste",
                f"{str(e)}"
            )
            raise
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # GET THE DATA FROM AN ADJUSTMENT - GET THE DATA FROM AN ADJUSTMENT - GET THE DATA FROM AN ADJUSTMENT - 
    # GET THE DATA FROM AN ADJUSTMENT - GET THE DATA FROM AN ADJUSTMENT - GET THE DATA FROM AN ADJUSTMENT - 
    def ObtenerAjuste(self, num_documento: str) -> dict | None:
        """
        Recupera un ajuste por su num_documento.
        Si no existe, devuelve None. En caso contrario retorna dict:
        {
          'id': int,
          'num_documento': str,
          'motivo': str,
          'fecha': date,
          'detalle': [
            {
              'codigo': str,
              'cantidad': int,
              'ajuste': int,
              'final': int
            }, …
          ]
        }
        """
        try:
            with self.conn.cursor() as cur:
                # 1) Leer cabecera
                cur.execute("""
                    SELECT id, log, fecha
                      FROM ajustes_inventario
                     WHERE num_documento = %s;
                """, (num_documento,))
                row = cur.fetchone()
                if not row:
                    return None
                ajuste_id, motivo, fecha = row
                # 2) Leer detalle asociado
                cur.execute("""
                    SELECT codigo, cantidad, ajuste, final
                      FROM detalle_ajustes
                     WHERE ajuste_id = %s
                     ORDER BY id;
                """, (ajuste_id,))
                detalle = [{
                    'codigo': r[0],
                    'cantidad': r[1],
                    'ajuste': r[2],
                    'final': r[3]
                } for r in cur.fetchall()]
                return {
                    'id':             ajuste_id,
                    'num_documento':  num_documento,
                    'motivo':         motivo,
                    'fecha':          fecha,
                    'detalle':        detalle
                }
        except Exception as e:
            messagebox.showerror(
                "Error al obtener ajuste",
                f"{str(e)}")
            return None
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    def SaveFactura(self, factura_data):
        """
        Guarda la factura en la base de datos
        factura_data = {
            'numero_factura': str,
            'cliente_codigo': str,
            'fecha': str,
            'total_dolares': float,
            'total_bolivares': float,
            'productos': [
                {'codigo': str, 'cantidad': int, 'precio_unitario': float, 
                 'subtotal_dolares': float, 'subtotal_bolivares': float}
            ]
        }
        """
        try:
            with self.conn.cursor() as cur:
                # Insertar cabecera de factura
                cur.execute("""
                    INSERT INTO facturas (numero_factura, cliente_codigo, fecha, total_dolares, total_bolivares)
                    VALUES (%s, %s, %s, %s, %s) RETURNING id;
                """, (factura_data['numero_factura'], factura_data['cliente_codigo'], 
                      factura_data['fecha'], factura_data['total_dolares'], 
                      factura_data['total_bolivares']))
                
                factura_id = cur.fetchone()[0]
                
                # Insertar detalles de factura
                for producto in factura_data['productos']:
                    cur.execute("""
                        INSERT INTO detalle_factura 
                        (factura_id, producto_codigo, cantidad, precio_unitario, subtotal_dolares, subtotal_bolivares)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """, (factura_id, producto['codigo'], producto['cantidad'],
                          producto['precio_unitario'], producto['subtotal_dolares'],
                          producto['subtotal_bolivares']))
                
                self.conn.commit()
                return True
                
        except Exception as e:
            self.conn.rollback()
            print(f"Error guardando factura: {str(e)}")
            return False
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    def GetNextFacturaNumber(self):
        """
        Obtiene el próximo número de factura basado en el último guardado
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT numero_factura FROM facturas 
                    ORDER BY id DESC LIMIT 1;
                """)
                result = cur.fetchone()
                if result:
                    last_number = result[0]
                    # Asumiendo formato FACT-001, FACT-002, etc.
                    number = int(last_number.split('-')[1]) + 1
                    return f"FACT-{number:03d}"
                else:
                    return "FACT-001"
        except Exception as e:
            print(f"Error obteniendo número de factura: {str(e)}")
            return "FACT-001"
# UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - 
# UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - 
# UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - 
# UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA - UPDATE DATA -
    # LOCK A PRODUCT TO MODIFY STOCK WHEN SELLING
    # LOCK A PRODUCT TO MODIFY STOCK WHEN SELLING
    def SellProduct(self,code,qty):
        try:
            # START TRANSACTION
            with self.conn:
                with self.conn.cursor() as cur:
                        # LOCK ROW OR PRODUCT
                        cur.execute("""
                            SELECT existencia FROM productos
                            WHERE codigo = %s AND activo = TRUE FOR UPDATE;""",(code,))
                        # GET THE INFO
                        row = cur.fetchone()
                        # IF NOT INFO RETURN NONE
                        if not row:
                            messagebox.showerror('Base de Datos','Producto no encontrado')
                            return False
                        stock = row[0]
                        if qty > stock:
                            messagebox.showerror('Base de Datos','Cantidad excede la existencia.')
                            return False
                        newstock = stock - qty
                        # UPDATE STOCK
                        cur.execute("""
                            UPDATE productos
                            SET existencia = %s WHERE codigo = %s""",(newstock,code))
            return True
        except Exception as e:
            messagebox.showerror("Base de Datos",f"{str(e)}")
            return False
    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------
    # RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - 
    # RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - RETURN PRODUCTS - 
    def ReturnProducts(self, product_list):
        """
        Revierte el stock de una lista de productos
        product_list: lista de tuplas (codigo, cantidad)
        """
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    for codigo, cantidad in product_list:
                        # Bloquear la fila para actualización
                        cur.execute("""
                            SELECT existencia FROM productos 
                            WHERE codigo = %s AND activo = TRUE FOR UPDATE;
                        """, (codigo,))

                        row = cur.fetchone()
                        if not row:
                            print(f"Advertencia: Producto {codigo} no encontrado")
                            continue
                        
                        stock_actual = row[0]
                        nuevo_stock = stock_actual + cantidad

                        # Revertir el stock
                        cur.execute("""
                            UPDATE productos 
                            SET existencia = %s 
                            WHERE codigo = %s;
                        """, (nuevo_stock, codigo))

            return True
        except Exception as e:
            print(f"Error revirtiendo productos: {str(e)}")
            return False

# -----------------------------------------------------------------------------------
# DOLAR MANEGEMENT - DOLAR MANEGEMENT - DOLAR MANEGEMENT - DOLAR MANEGEMENT -
# -----------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------
    # SAVES DOLAR VALUE - SAVES DOLAR VALUE - SAVES DOLAR VALUE - SAVES DOLAR VALUE -
    # -------------------------------------------------------------------------------
    def GuardarDolar(self, fecha: str, tasa: float, log: str = 'Manual'):
        """
        Guarda la tasa del dólar en la tabla 'dolar'.
        Si ya existe una entrada para esa fecha, no la sobrescribe.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO dolar (fecha, tasa, log)
                    VALUES (%s, %s, %s);
                """, (fecha, tasa, log))
                self.conn.commit()
                messagebox.showinfo("Guardado", f"Tasa del dólar para {fecha} registrada correctamente.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"No se pudo guardar la tasa: {str(e)}")
            
    def GuardarDolarParalelo(self, fecha: str, tasa: float, log: str = 'Manual'):
        """
        Guarda la tasa del dólar en la tabla 'dolar'.
        Si ya existe una entrada para esa fecha, no la sobrescribe.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO paralelo (fecha, tasa, log)
                    VALUES (%s, %s, %s);
                """, (fecha, tasa, log))
                self.conn.commit()
                messagebox.showinfo("Guardado", f"Tasa del dólar para {fecha} registrada correctamente.")
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("Error", f"No se pudo guardar la tasa: {str(e)}")
    # ---------------------------------------------------------------------------------------
    # GET DOLAR WITH DATE - GET DOLAR WITH DATE - GET DOLAR WITH DATE - GET DOLAR WITH DATE - GET DOLAR WITH DATE - 
    # ---------------------------------------------------------------------------------------
    def GetDolar(self, fecha: str) -> float | None:
        """
        Devuelve la última tasa del dólar registrada para una fecha específica.
        Si no existe, retorna None.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT tasa
                      FROM dolar
                     WHERE fecha = %s
                     ORDER BY hora DESC
                     LIMIT 1;
                """, (fecha,))
                row = cur.fetchone()
                if row:
                    return float(row[0])
                else:
                    messagebox.showinfo("Sin datos", f"No hay tasa registrada para {fecha}.")
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la tasa: {str(e)}")
            return None
    def GetDolarParalelo(self, fecha: str) -> float | None:
        """
        Devuelve la última tasa del dólar registrada para una fecha específica.
        Si no existe, retorna None.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT tasa
                      FROM paralelo
                     WHERE fecha = %s
                     ORDER BY hora DESC
                     LIMIT 1;
                """, (fecha,))
                row = cur.fetchone()
                if row:
                    return float(row[0])
                else:
                    messagebox.showinfo("Sin datos", f"No hay tasa registrada para {fecha}.")
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la tasa: {str(e)}")
            return None
    # ---------------------------------------------------------------------------------------
    # GET DOLAR VALUES FROM A DATE RANGE - GET DOLAR VALUES FROM A DATE RANGE - 
    # ---------------------------------------------------------------------------------------
    def GetDolarRango(self, fecha_inicio: str, fecha_fin: str) -> list:
        """
        Devuelve una lista de registros de la tabla 'dolar' entre dos fechas.
        Cada registro es un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM dolar
                     WHERE fecha BETWEEN %s AND %s
                     ORDER BY fecha ASC;
                """, (fecha_inicio, fecha_fin))
                rows = cur.fetchall()
                resultados = []
                for fecha, tasa, log, hora in rows:
                    resultados.append({
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    })
                return resultados
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el rango: {str(e)}")
            return []
        
    def GetDolarParaleloRango(self, fecha_inicio: str, fecha_fin: str) -> list:
        """
        Devuelve una lista de registros de la tabla 'paralelo' entre dos fechas.
        Cada registro es un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM paralelo
                     WHERE fecha BETWEEN %s AND %s
                     ORDER BY fecha ASC;
                """, (fecha_inicio, fecha_fin))
                rows = cur.fetchall()
                resultados = []
                for fecha, tasa, log, hora in rows:
                    resultados.append({
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    })
                return resultados
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el rango: {str(e)}")
            return []
    # ---------------------------------------------------------------------------------------
    # GET LAST DOLAR - GET LAST DOLAR - GET LAST DOLAR - GET LAST DOLAR - GET LAST DOLAR - GET LAST DOLAR - 
    # ---------------------------------------------------------------------------------------
    def GetLastDolar(self) -> dict | None:
        """
        Devuelve el último valor de dólar cargado en la tabla.
        Retorna un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM dolar
                     ORDER BY hora DESC
                     LIMIT 1;
                """)
                row = cur.fetchone()
                if row:
                    fecha, tasa, log, hora = row
                    return {
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    }
                else:
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el último valor: {str(e)}")
            return None
        
    def GetLastDolarParalelo(self) -> dict | None:
        """
        Devuelve el último valor de dólar paralelo cargado en la tabla.
        Retorna un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM paralelo
                     ORDER BY hora DESC
                     LIMIT 1;
                """)
                row = cur.fetchone()
                if row:
                    fecha, tasa, log, hora = row
                    return {
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    }
                else:
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el último valor: {str(e)}")
            return None
    # ---------------------------------------------------------------------------------------
    # GET
    # ---------------------------------------------------------------------------------------
    def GetLastDolarValue(self) -> float | None:
        """
        Devuelve el último valor de dólar cargado en la tabla.
        Retorna un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT tasa
                      FROM dolar
                     ORDER BY hora DESC
                     LIMIT 1;
                """)
                row = cur.fetchone()
                if row:
                    return float(row[0])
                else:
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el último valor: {str(e)}")
            return None
    def GetLastDolarParaleloValue(self) -> float | None:
        """
        Devuelve el último valor de dólar paralelo cargado en la tabla.
        Retorna un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT tasa
                      FROM paralelo
                     ORDER BY hora DESC
                     LIMIT 1;
                """)
                row = cur.fetchone()
                if row:
                    return float(row[0])
                else:
                    return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el último valor: {str(e)}")
            return None

    def GetDolarLastMonth(self) -> list:
        """
        Devuelve los últimos 30 valores de dólar cargados.
        Cada elemento es un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM dolar
                     ORDER BY hora DESC
                     LIMIT 30;
                """)
                rows = cur.fetchall()
                resultados = []
                for fecha, tasa, log, hora in rows:
                    resultados.append({
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    })
                return resultados
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los últimos valores: {str(e)}")
            return []
        
    def GetDolarParaleloLastMonth(self) -> list:
        """
        Devuelve los últimos 30 valores de dólar paralelo cargados.
        Cada elemento es un diccionario con: fecha, tasa, log, hora.
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT fecha, tasa, log, hora
                      FROM paralelo
                     ORDER BY hora DESC
                     LIMIT 30;
                """)
                rows = cur.fetchall()
                resultados = []
                for fecha, tasa, log, hora in rows:
                    resultados.append({
                        'fecha': fecha,
                        'tasa': float(tasa),
                        'log': log,
                        'hora': hora
                    })
                return resultados
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los últimos valores: {str(e)}")
            return []


    def __del__(self):
        """Cierra la conexión a la base de datos cuando el objeto se destruye."""
        if self.conn:
            self.conn.close()
