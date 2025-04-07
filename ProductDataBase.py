import json,os
from tkinter import messagebox

Inventario = {}

# CARGAR EL ARCHIVO DE DATOS
def Load_Inventory():
    global Inventario
    # CREAR LA CARPETA DATA SI NO EXISTE
    if not os.path.exists('Data'):
        os.makedirs('Data')
    # VERIFICAR SI EXISTE EL ARCHIVO DE DATOS / CARGAR EL ARCHIVO DE DATOS
    try:
        with open('Data/Inventario.json','r') as InventoryData_JsonFile:
            Inventario = json.load(InventoryData_JsonFile)
    except FileNotFoundError:
        Save_Inventory()

# GUARDAR EL ARCHIVO DE DATOS
def Save_Inventory():
    with open('Data/Inventario.json','w') as InventoryData_JsonFile:
        json.dump(Inventario,InventoryData_JsonFile,indent=4)

# CLASE PRODUCTOS
class Product():
    def __init__(self,codigo,linea,grupo,nombre,precio,cantidad):

        self.codigo = codigo
        self.linea = linea
        self.grupo = grupo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def ToDict(self):
        return{
            'codigo':self.codigo,
            'linea':self.linea,
            'grupo':self.grupo,
            'nombre':self.nombre,
            'precio':self.precio,
            'cantidad':self.cantidad
        }

# CLASE INVENTARIO
class Inventory():
    def __init__(self):
            global Inventario
            self.products = Inventario

    def AddProduct(self,product):
        global Inventario
        if product.codigo in Inventario:
            messagebox.showinfo(f'El producto con el codigo {product.codigo} ya existe.')
            return
         
        Inventario[product.codigo] = product.ToDict()
        self.products =  Inventario
        Save_Inventory()
        messagebox.showinfo(f'El producto {product.nombre} agregado con exito.')