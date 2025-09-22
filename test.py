from DatabaseManager import INVENTARIO

code = '96350161'
user = INVENTARIO.SellProduct(code,9)

if user:
    print("Venta realizada con éxito")
else:
    print("Error en la venta")