from InventarioProductos_DB import Inventory
from LineasGrupos_DB import LineasGrupos
from Proveedores_DB import Proveedores
from Usuarios_DB import Users

DATABASE_INFO = ['AppDatabase','postgres','admin1234','localhost','5432']
CLIENT_INFO = ['Mercaduo C.A.']

INVENTARIO = Inventory(dbname=DATABASE_INFO[0],
                            user=DATABASE_INFO[1],
                            password=DATABASE_INFO[2],
                            host=DATABASE_INFO[3],
                            port=DATABASE_INFO[4])

LINE_MANAGER = LineasGrupos(dbname=DATABASE_INFO[0],
                            user=DATABASE_INFO[1],
                            password=DATABASE_INFO[2],
                            host=DATABASE_INFO[3],
                            port=DATABASE_INFO[4])

PROV_MANAGER = Proveedores(dbname=DATABASE_INFO[0],
                            user=DATABASE_INFO[1],
                            password=DATABASE_INFO[2],
                            host=DATABASE_INFO[3],
                            port=DATABASE_INFO[4])

USER_MANAGER = Users(dbname=DATABASE_INFO[0],
                            user=DATABASE_INFO[1],
                            password=DATABASE_INFO[2],
                            host=DATABASE_INFO[3],
                            port=DATABASE_INFO[4])



def UpdateDolarValue():
    dolar = INVENTARIO.GetLastDolar()
    if dolar is None:
        print("No se encontró tasa de dólar.")
        VALOR_DOLAR = 0.0
    else:
        try:
            VALOR_DOLAR = dolar['tasa']
        except KeyError:
            print("La clave 'tasa' no existe en el resultado.")
            VALOR_DOLAR = 0.0
            
dolar = INVENTARIO.GetLastDolar()
if dolar is None:
    print("No se encontró tasa de dólar.")
    VALOR_DOLAR = 0.0
else:
    try:
        VALOR_DOLAR = dolar['tasa']
    except KeyError:
        print("La clave 'tasa' no existe en el resultado.")
        VALOR_DOLAR = 0.0
# FUNCIONES CALLBACK

FUNCIONES = {
        'UpdateDolarValue':UpdateDolarValue
    }
