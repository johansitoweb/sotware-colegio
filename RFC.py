import customtkinter as ctk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración del Sistema")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Estilo general
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Frame principal
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.label_titulo = ctk.CTkLabel(self.frame, text="Configuración del Sistema", font=("Arial", 24))
        self.label_titulo.pack(pady=10)

        # Configuración del perfil
        self.crear_tab_perfil()

        # Preferencias del sistema
        self.crear_tab_preferencias()

        # Gestión de permisos y roles
        self.crear_tab_permisos()

    def crear_tab_perfil(self):
        perfil_frame = ctk.CTkFrame(self.frame)
        perfil_frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(perfil_frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nombre = ctk.CTkEntry(perfil_frame)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(perfil_frame, text="Correo Electrónico:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_correo = ctk.CTkEntry(perfil_frame)
        self.entry_correo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(perfil_frame, text="Contraseña:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_contrasena = ctk.CTkEntry(perfil_frame, show='*')
        self.entry_contrasena.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkButton(perfil_frame, text="Guardar Cambios", command=self.guardar_cambios).grid(row=3, column=0, columnspan=2, pady=10)

    def crear_tab_preferencias(self):
        preferencias_frame = ctk.CTkFrame(self.frame)
        preferencias_frame.pack(pady=10, padx=10, fill="x")

        self.var_tema = ctk.StringVar(value="Claro")
        ctk.CTkLabel(preferencias_frame, text="Tema:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        temas = ["Claro", "Oscuro"]
        for i, tema in enumerate(temas):
            ctk.CTkRadioButton(preferencias_frame, text=tema, variable=self.var_tema, value=tema).grid(row=0, column=i+1, padx=5, pady=5)

        ctk.CTkCheckBox(preferencias_frame, text="Activar Notificaciones").grid(row=1, column=0, columnspan=3, pady=10)

        ctk.CTkButton(preferencias_frame, text="Aplicar Cambios", command=self.aplicar_cambios).grid(row=2, column=0, columnspan=3, pady=10)

    def crear_tab_permisos(self):
        permisos_frame = ctk.CTkFrame(self.frame)
        permisos_frame.pack(pady=10, padx=10, fill="x")

        roles = [
            ("Administrador", ["Crear", "Leer", "Actualizar", "Eliminar"]),
            ("Profesor", ["Leer", "Actualizar"]),
            ("Estudiante", ["Leer"])
        ]

        self.tree_roles = ctk.CTkTextbox(permisos_frame, height=100)

        for role in roles:
            role_name = role[0]
            permissions = ", ".join(role[1])
            self.tree_roles.insert("end", f"{role_name}: {permissions}\n")

        self.tree_roles.pack(pady=10, fill="both", expand=True)

    def guardar_cambios(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        contrasena = self.entry_contrasena.get()

        if nombre and correo and contrasena:
            print(f"Nombre: {nombre}, Correo: {correo}, Contraseña: {contrasena}")

    def aplicar_cambios(self):
        tema_seleccionado = self.var_tema.get()
        print(f"Cambios aplicados. Tema seleccionado: {tema_seleccionado}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
