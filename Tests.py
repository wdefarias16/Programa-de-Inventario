def check_bom(filepath = 'C:\\Users\\Alejandro\\Desktop\\Programa-de-Inventario-master'):
    with open(filepath, "rb") as f:
        first_bytes = f.read(3)
        if first_bytes == b'\xef\xbb\xbf':
            print("El archivo tiene BOM.")
        else:
            print("El archivo no tiene BOM.")

# Reemplaza 'tu_archivo.txt' por el nombre de tu archivo
check_bom("Main.py")
