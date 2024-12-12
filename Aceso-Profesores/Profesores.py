import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Profesor:
    def __init__(self, nombre, materia, horario):
        self.nombre = nombre    # Indentado 4 espacios
        self.materia = materia  # Indentado 4 espacios
        self.horario = horario  # Indentado 4 espacios

class GestionProfesores:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Profesores")
        self.root.geometry("600x500")
        
        # Lista de profesores
        self.profesores = []

        # Frame para los botones y las acciones
        self.frame_acciones = tk.Frame(self.root)
        self.frame_acciones.pack(pady=10)

        self.btn_registrar = tk.Button(self.frame_acciones, text="Registrar Profesor", width=20, command=self.registrar_profesor)
        self.btn_registrar.grid(row=0, column=0, padx=10)

        self.btn_listar = tk.Button(self.frame_acciones, text="Listar Profesores", width=20, command=self.listar_profesores)
        self.btn_listar.grid(row=0, column=1, padx=10)

        # Área de listado
        self.lista_frame = tk.Frame(self.root)
        self.lista_frame.pack(pady=20)

    def registrar_profesor(self):
        """Registra un nuevo profesor"""
        nombre = simpledialog.askstring("Registro", "Nombre del profesor:")
        if nombre:
            materia = simpledialog.askstring("Registro", "Materia que enseña:")
            if materia:
                horario = simpledialog.askstring("Registro", "Horario (ejemplo: Lunes 8:00 AM):")
                if horario:
                    nuevo_profesor = Profesor(nombre, materia, horario)
                    self.profesores.append(nuevo_profesor)
                    messagebox.showinfo("Éxito", f"Profesor {nombre} registrado correctamente")
                else:
                    messagebox.showerror("Error", "El horario es obligatorio.")
            else:
                messagebox.showerror("Error", "La materia es obligatoria.")
        else:
            messagebox.showerror("Error", "El nombre es obligatorio.")

    def listar_profesores(self):
        """Lista a los profesores registrados con opciones para editar o eliminar"""
        for widget in self.lista_frame.winfo_children():
            widget.destroy()  # Limpiar los registros previos en la lista

        if not self.profesores:
            messagebox.showinfo("Información", "No hay profesores registrados.")
            return
        
        for i, profesor in enumerate(self.profesores):
            profesor_label = tk.Label(self.lista_frame, text=f"{profesor.nombre} - {profesor.materia} - {profesor.horario}")
            profesor_label.grid(row=i, column=0, sticky="w", padx=10)
            
            btn_editar = tk.Button(self.lista_frame, text="Editar", command=lambda i=i: self.editar_profesor(i))
            btn_editar.grid(row=i, column=1, padx=10)

            btn_eliminar = tk.Button(self.lista_frame, text="Eliminar", command=lambda i=i: self.eliminar_profesor(i))
            btn_eliminar.grid(row=i, column=2, padx=10)

    def editar_profesor(self, indice):
        """Edita los detalles de un profesor"""
        profesor = self.profesores[indice]
        nuevo_nombre = simpledialog.askstring("Editar", "Nuevo nombre:", initialvalue=profesor.nombre)
        if nuevo_nombre:
            nueva_materia = simpledialog.askstring("Editar", "Nueva materia:", initialvalue=profesor.materia)
            if nueva_materia:
                nuevo_horario = simpledialog.askstring("Editar", "Nuevo horario:", initialvalue=profesor.horario)
                if nuevo_horario:
                    profesor.nombre = nuevo_nombre
                    profesor.materia = nueva_materia
                    profesor.horario = nuevo_horario
                    self.listar_profesores()
                    messagebox.showinfo("Éxito", "Profesor actualizado correctamente.")
                else:
                    messagebox.showerror("Error", "El horario es obligatorio.")
            else:
                messagebox.showerror("Error", "La materia es obligatoria.")
        else:
            messagebox.showerror("Error", "El nombre es obligatorio.")

    def eliminar_profesor(self, indice):
        """Elimina un profesor"""
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este profesor?"):
            del self.profesores[indice]
            self.listar_profesores()
            messagebox.showinfo("Éxito", "Profesor eliminado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    gestion = GestionProfesores(root)
    root.mainloop()

