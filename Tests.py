# Diccionario de productos
productos = {
    "001": {
        "codigo": "001",
        "linea": "001",
        "grupo": "Pantallas",
        "proveedor": "01",
        "nombre": "Pantalla 109",
        "precio": 10.0,
        "cantidad": 100
    },
    "002": {
        "codigo": "002",
        "linea": "001",
        "grupo": "Pantallas",
        "proveedor": "01",
        "nombre": "Pantalla 106",
        "precio": 15.0,
        "cantidad": 50
    }
}

# Función para buscar productos por nombre
def buscar_productos(productos, consulta):
    consulta = consulta.lower()  # Convertir la consulta a minúsculas para búsqueda sin distinción de mayúsculas/minúsculas
    resultados = [
        producto for producto in productos.values()
        if consulta in producto["nombre"].lower()
    ]
    return resultados

# Ejemplo de uso
consulta = "pan"
resultados = buscar_productos(productos, consulta)

# Imprimir resultados
for producto in resultados:
    print(f'Código: {producto["codigo"]}, Nombre: {producto["nombre"]}, Precio: {producto["precio"]}, Cantidad: {producto["cantidad"]}')