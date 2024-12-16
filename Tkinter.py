import tkinter as tk
import time

KEYS = ["/", "-", "\\"]

def loading_effect(duration):
    cont = 0
    time_elapsed = 0

    def update_label():
        nonlocal cont, time_elapsed
        if time_elapsed < duration:
            key = KEYS[cont % len(KEYS)]
            label.config(text=key)
            cont += 1
            time_elapsed += 1
            root.after(200, update_label)  # Actualiza cada 200ms
        else:
            label.config(text="El Proceso se ha completado exitosamente!")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Loading Effect")

label = tk.Label(root, text="", font=("Arial", 24))
label.pack(pady=20)

# Inicia la animación
loading_effect(100)

root.mainloop()