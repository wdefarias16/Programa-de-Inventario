import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

# Configuración de estilo
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ImageResizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Redimensionar Imágenes 500×500")
        self.geometry("600x550")
        
        self.btn_load = ctk.CTkButton(self, text="Cargar imagen", command=self.load_image)
        self.btn_load.pack(pady=20)
        
        self.preview_label = ctk.CTkLabel(self, text="Aquí se mostrará la vista previa")
        self.preview_label.pack(pady=10)
        
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if not file_path:
            return
        
        img = Image.open(file_path)
        w, h = img.size
        
        max_size = 500
        scale = min(max_size / w, max_size / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        
        # Filtro compatible según versión de Pillow
        try:
            resample_filter = Image.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image.LANCZOS
        
        img_resized = img.resize((new_w, new_h), resample_filter)
        
        output_dir = "imagenes"
        os.makedirs(output_dir, exist_ok=True)
        
        base_name = os.path.basename(file_path)
        save_path = os.path.join(output_dir, base_name)
        img_resized.save(save_path)
        
        tk_img = ImageTk.PhotoImage(img_resized)
        self.preview_label.configure(image=tk_img, text="")
        self.preview_label.image = tk_img  # Evitar que Python elimine la referencia

if __name__ == "__main__":
    app = ImageResizerApp()
    app.mainloop()
