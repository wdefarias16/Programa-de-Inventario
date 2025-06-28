# ———————————————————————————————————————————————————————————————————————————————
# 2) En tu clase de acceso a datos (DatabaseManager.py), actualiza 
#    GuardarEntradaInventario() para recibir y almacenar los campos nuevos:
# ———————————————————————————————————————————————————————————————————————————————
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
