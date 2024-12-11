import tkinter as tk
from tkinter import ttk, messagebox
import random

class GamifiedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gamificación Educativa")
        self.root.geometry("900x700")

        # Variables de puntos, niveles y desafíos
        self.user_points = 0
        self.user_badges = []
        self.current_level = 1
        self.challenges_completed = 0

        # Configurar la interfaz
        self.create_interface()

    def create_interface(self):
        """Crea la interfaz gráfica principal."""
        # Puntos
        self.points_label = tk.Label(self.root, text=f"Puntos: {self.user_points}", font=("Helvetica", 14))
        self.points_label.pack(pady=10)

        # Nivel
        self.level_label = tk.Label(self.root, text=f"Nivel: {self.current_level}", font=("Helvetica", 14))
        self.level_label.pack(pady=10)

        # Insignias
        self.badges_label = tk.Label(self.root, text="Insignias: Ninguna", font=("Helvetica", 14))
        self.badges_label.pack(pady=10)

        # Desafíos
        self.challenge_frame = tk.Frame(self.root)
        self.challenge_frame.pack(pady=20)

        self.challenge_label = tk.Label(self.challenge_frame, text="Completa un desafío:")
        self.challenge_label.pack(side=tk.LEFT, padx=5)

        self.challenge_button = tk.Button(self.challenge_frame, text="Completar Desafío", command=self.complete_challenge)
        self.challenge_button.pack(side=tk.LEFT, padx=5)

        # Opciones adicionales
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=20)

        self.option1_button = tk.Button(self.options_frame, text="Resolver Quiz", command=self.resolve_quiz)
        self.option1_button.pack(side=tk.LEFT, padx=10)

        self.option2_button = tk.Button(self.options_frame, text="Participar en Competencia", command=self.participate_competition)
        self.option2_button.pack(side=tk.LEFT, padx=10)

        self.option3_button = tk.Button(self.options_frame, text="Revisar Progreso", command=self.show_progress)
        self.option3_button.pack(side=tk.LEFT, padx=10)

        self.option4_button = tk.Button(self.options_frame, text="Tienda de Insignias", command=self.open_store)
        self.option4_button.pack(side=tk.LEFT, padx=10)

    def complete_challenge(self):
        """Completa un desafío y otorga puntos al usuario."""
        self.update_points(20)
        self.challenges_completed += 1
        messagebox.showinfo("Desafío Completado", "¡Has completado un desafío y ganado 20 puntos!")

    def resolve_quiz(self):
        """Simula resolver un quiz y otorga puntos según el resultado."""
        points_earned = random.randint(5, 20)  # Puntos aleatorios entre 5 y 20
        self.update_points(points_earned)
        messagebox.showinfo("Quiz Completado", f"¡Has ganado {points_earned} puntos al resolver el quiz!")

    def participate_competition(self):
        """Simula una competencia interna con puntos aleatorios."""
        points_earned = random.randint(10, 50)  # Puntos aleatorios entre 10 y 50
        self.update_points(points_earned)
        messagebox.showinfo("Competencia", f"¡Felicidades! Ganaste {points_earned} puntos en la competencia.")

    def show_progress(self):
        """Muestra el progreso del usuario en un mensaje."""
        progress_message = (
            f"Puntos totales: {self.user_points}\n"
            f"Nivel actual: {self.current_level}\n"
            f"Insignias obtenidas: {', '.join(self.user_badges) if self.user_badges else 'Ninguna'}\n"
            f"Desafíos completados: {self.challenges_completed}"
        )
        messagebox.showinfo("Progreso del Usuario", progress_message)

    def open_store(self):
        """Abre una ventana para la tienda de insignias."""
        store_window = tk.Toplevel(self.root)
        store_window.title("Tienda de Insignias")
        store_window.geometry("400x300")

        tk.Label(store_window, text="Tienda de Insignias", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(store_window, text="Comprar Insignia de Bronce (50 puntos)", command=lambda: self.purchase_badge("Bronce", 50)).pack(pady=5)
        tk.Button(store_window, text="Comprar Insignia de Plata (100 puntos)", command=lambda: self.purchase_badge("Plata", 100)).pack(pady=5)
        tk.Button(store_window, text="Comprar Insignia de Oro (200 puntos)", command=lambda: self.purchase_badge("Oro", 200)).pack(pady=5)

    def purchase_badge(self, badge_name, cost):
        """Permite al usuario comprar una insignia si tiene suficientes puntos."""
        if self.user_points >= cost:
            if badge_name not in self.user_badges:
                self.user_points -= cost
                self.user_badges.append(badge_name)
                self.points_label.config(text=f"Puntos: {self.user_points}")
                self.badges_label.config(text=f"Insignias: {', '.join(self.user_badges)}")
                messagebox.showinfo("Compra Exitosa", f"¡Has comprado la insignia {badge_name}!")
            else:
                messagebox.showwarning("Ya Comprada", f"Ya tienes la insignia {badge_name}.")
        else:
            messagebox.showwarning("Puntos Insuficientes", "No tienes suficientes puntos para comprar esta insignia.")

    def update_points(self, points):
        """Actualiza los puntos del usuario y verifica niveles e insignias."""
        self.user_points += points
        self.points_label.config(text=f"Puntos: {self.user_points}")

        # Actualizar nivel
        new_level = self.user_points // 100 + 1
        if new_level > self.current_level:
            self.current_level = new_level
            self.level_label.config(text=f"Nivel: {self.current_level}")
            messagebox.showinfo("¡Subiste de Nivel!", f"¡Felicidades! Has alcanzado el Nivel {self.current_level}.")

        # Insignias por puntos acumulados
        if self.user_points >= 50 and "Bronce" not in self.user_badges:
            self.user_badges.append("Bronce")
            self.show_badge_message("¡Felicidades! Has obtenido la insignia de Bronce.")
        elif self.user_points >= 100 and "Plata" not in self.user_badges:
            self.user_badges.append("Plata")
            self.show_badge_message("¡Felicidades! Has obtenido la insignia de Plata.")
        elif self.user_points >= 200 and "Oro" not in self.user_badges:
            self.user_badges.append("Oro")
            self.show_badge_message("¡Felicidades! Has obtenido la insignia de Oro.")

        # Actualizar etiqueta de insignias
        if self.user_badges:
            self.badges_label.config(text=f"Insignias: {', '.join(self.user_badges)}")

    def show_badge_message(self, message):
        """Muestra un mensaje cuando se gana una insignia."""
        messagebox.showinfo("Nueva Insignia", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GamifiedApp(root)
    root.mainloop()
