import tkinter as tk
from tkinter import ttk

def show_details(info):
    details_window = tk.Toplevel(root)
    details_window.title(info)
    details_window.geometry("400x250")
    details_window.configure(bg="#e6f7ff")

    details_text = {
        "Cómo crear una cuenta.": "Paso 1: Accede a la plataforma.\nPaso 2: Haz clic en 'Crear cuenta'.\nPaso 3: Rellena el formulario y confirma.",
        "Cómo recuperar una contraseña.": "Paso 1: Haz clic en 'Olvidé mi contraseña'.\nPaso 2: Ingresa tu correo electrónico.\nPaso 3: Revisa tu correo para el enlace de recuperación.",
        "Cómo usar el panel principal.": "Paso 1: Inicia sesión.\nPaso 2: Explora el menú principal para ver tus opciones.",
        "Cómo gestionar tareas y evaluaciones.": "Paso 1: Ve a la sección de Tareas.\nPaso 2: Crea, edita y revisa tareas asignadas.",
        "Cómo contactar soporte técnico.": "Paso 1: Accede a 'Soporte'.\nPaso 2: Envía un mensaje detallado sobre tu problema."
    }

    tk.Label(details_window, text=info, font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#003366").pack(pady=15)
    tk.Message(details_window, text=details_text.get(info, "Información no disponible"), width=350, font=("Arial", 12), bg="#e6f7ff", fg="#003366").pack(pady=10)
    tk.Button(details_window, text="Cerrar", command=details_window.destroy, bg="#f44336", fg="white", font=("Arial", 12, "bold"), relief="raised", overrelief="sunken").pack(pady=10)

def open_modal():
    modal = tk.Toplevel(root)
    modal.title("Guía de Soporte Técnico")
    modal.geometry("450x350")
    modal.configure(bg="#e6f7ff")

    tk.Label(modal, text="Guía de Soporte Técnico", font=("Arial", 18, "bold"), bg="#e6f7ff", fg="#003366").pack(pady=15)
    search_input = tk.Entry(modal, width=40, font=("Arial", 12))
    search_input.pack(pady=5)

    content_frame = tk.Frame(modal, bg="#e6f7ff")
    content_frame.pack(pady=10, fill="both", expand=True)

    content = [
        "Cómo crear una cuenta.",
        "Cómo recuperar una contraseña.",
        "Cómo usar el panel principal.",
        "Cómo gestionar tareas y evaluaciones.",
        "Cómo contactar soporte técnico."
    ]

    info_labels = []
    for item in content:
        label = tk.Label(content_frame, text=item, anchor="w", font=("Arial", 12), bg="#e6f7ff", fg="#003366")
        label.pack(anchor="w", padx=10, pady=2)
        label.bind("<Button-1>", lambda e, i=item: show_details(i))
        label.bind("<Enter>", lambda e, lbl=label: lbl.config(bg="#c2f0c2"))
        label.bind("<Leave>", lambda e, lbl=label: lbl.config(bg="#e6f7ff"))
        info_labels.append(label)

    def filter_content(event):
        query = search_input.get().lower()
        for label in info_labels:
            label.pack_forget()
            if query in label.cget("text").lower():
                label.pack(anchor="w", padx=10, pady=2)

    search_input.bind("<KeyRelease>", filter_content)

    close_btn = tk.Button(modal, text="Cerrar", command=modal.destroy, bg="#f44336", fg="white", font=("Arial", 12, "bold"), relief="raised", overrelief="sunken")
    close_btn.pack(pady=10)

root = tk.Tk()
root.title("Soporte Técnico")
root.geometry("300x200")
root.configure(bg="#cce7ff")

def create_modern_button(text, command):
    return tk.Button(
        root, text=text, command=command, bg="#007acc", fg="white", font=("Arial", 14, "bold"),
        padx=20, pady=10, relief="raised", overrelief="sunken", activebackground="#005f99")

open_btn = create_modern_button("Soporte Técnico", open_modal)
open_btn.pack(pady=50)

root.mainloop()

