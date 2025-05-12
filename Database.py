from InventarioProductos import Inventory
from LineasGrupos import LineasGrupos
from Proveedores_DB import Proveedores
from UsuariosDB import Users

DATABASE_INFO = ['AppDatabase','postgres','admin1234','localhost','5432']

INVENTARIO = Inventory()
LINE_MANAGER = LineasGrupos()
PROV_MANAGER = Proveedores(dbname=DATABASE_INFO[0],
                            user=DATABASE_INFO[1],
                            password=DATABASE_INFO[2],
                            host=DATABASE_INFO[3],
                            port=DATABASE_INFO[4])
USER_MANAGER = Users()
