def GetLineNames(self):
    # Crear una lista con el formato 'código - nombre' para cada línea
    nombre_lineas = [f"{codigo} - {dato['linea']}" for codigo, dato in lineas_grupos.items()]
    return nombre_lineas