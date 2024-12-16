import customtkinter as ctk

# Configuración de la ventana principal
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

root = ctk.CTk()
root.title("Gestión de Estudiantes")
root.geometry("500x400")

def agregar_estudiante():
    nombre = entry_nombre.get()
    grado = entry_grado.get()
    dni = entry_dni.get()
    if nombre and grado and dni:
        tree.insert("", "end", values=(nombre, grado, dni))
        entry_nombre.delete(0, ctk.END)
        entry_grado.delete(0, ctk.END)
        entry_dni.delete(0, ctk.END)

def eliminar_estudiante():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item[0])

# Formulario de registro
frame_registro = ctk.CTkFrame(root)
frame_registro.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_registro, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nombre = ctk.CTkEntry(frame_registro, width=200)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

ctk.CTkLabel(frame_registro, text="Grado:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_grado = ctk.CTkEntry(frame_registro, width=200)
entry_grado.grid(row=1, column=1, padx=5, pady=5)

ctk.CTkLabel(frame_registro, text="DNI:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_dni = ctk.CTkEntry(frame_registro, width=200)
entry_dni.grid(row=2, column=1, padx=5, pady=5)

ctk.CTkButton(frame_registro, text="Agregar Estudiante", command=agregar_estudiante).grid(row=3, column=0, columnspan=2, pady=10)

# Listado de estudiantes
tree_frame = ctk.CTkFrame(root)
tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

from tkinter import ttk
cols = ("Nombre", "Grado", "DNI")
tree = ttk.Treeview(tree_frame, columns=cols, show='headings', height=8)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

tree.pack(fill="both", expand=True, padx=5, pady=5)

ctk.CTkButton(root, text="Eliminar Estudiante", command=eliminar_estudiante).pack(pady=10)

root.mainloop()
