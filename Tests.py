import tkinter as tk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Inicialmente, el bind está ligado a la primera función
        self.entry.bind("<Return>", lambda event: self.funcion1())

        # Botón para cambiar la función asociada al <Return>
        self.boton_cambiar = tk.Button(root, text="Cambiar función", command=self.cambiar_bind)
        self.boton_cambiar.pack()

    def funcion1(self):
        print("Función 1 ejecutada")

    def funcion2(self):
        print("Función 2 ejecutada")

    def cambiar_bind(self):
        # Elimina el bind anterior y establece el nuevo
        self.entry.unbind("<Return>")
        self.entry.bind("<Return>", lambda event: self.funcion2())

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()