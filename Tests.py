import tkinter as tk

def validar_input(texto):
    """
    Esta función comprueba que:
      - La longitud del texto no sea mayor a 3.
      - El texto esté vacío o sea numérico.
    """
    if len(texto) > 3:
        return False
    if texto == "":  # Permite borrar el contenido
        return True
    return texto.isdigit()  # Solo acepta si el texto contiene dígitos únicamente

root = tk.Tk()
root.title("Entrada numérica limitada a 3 dígitos")

# Registra la función de validación para que Tkinter la reconozca
vcmd = root.register(validar_input)

# La opción validate="key" hace que la validación se ejecute en cada pulsación de tecla.
# "%P" es un parámetro especial que representa el contenido del Entry si se acepta el cambio.
entry = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry.pack(padx=20, pady=20)

root.mainloop()