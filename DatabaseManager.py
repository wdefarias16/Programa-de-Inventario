from DB_InventarioProductos import Inventory
from DB_LineasGrupos import LineasGrupos
from DB_Proveedores import Proveedores
from DB_Usuarios import Users

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

CURRENT_USER = None
def LoginUser(user):
    global CURRENT_USER
    CURRENT_USER = user['usuario']
def GetCurrentUser():
    return CURRENT_USER
