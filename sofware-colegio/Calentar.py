mport tkinter as tk
from tkinter import ttk, messagebox
import calendar
import datetime

class SchoolCalendar:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendario Escolar")

        # Variables
        self.current_year = datetime.datetime.now().year
        self.current_month = datetime.datetime.now().month
        self.events = {}

        # Configurar el marco principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="NSEW")

        # Encabezado del calendario
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.grid(row=0, column=0, columnspan=7)

        self.prev_button = ttk.Button(self.header_frame, text="<", command=self.prev_month)
        self.prev_button.grid(row=0, column=0)

        self.month_label = ttk.Label(self.header_frame, text="", font=("Arial", 16))
        self.month_label.grid(row=0, column=1, columnspan=5)

        self.next_button = ttk.Button(self.header_frame, text=">", command=self.next_month)
        self.next_button.grid(row=0, column=6)

        # Crear la cuadrícula del calendario
        self.calendar_frame = ttk.Frame(self.main_frame)
        self.calendar_frame.grid(row=1, column=0, columnspan=7)

        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for i, day in enumerate(days):
            ttk.Label(self.calendar_frame, text=day, anchor="center", width=10).grid(row=0, column=i)

        self.day_buttons = []
        for row in range(1, 7):
            for col in range(7):
                button = ttk.Button(self.calendar_frame, text="", width=10, command=lambda r=row, c=col: self.select_day(r, c))
                button.grid(row=row, column=col)
                self.day_buttons.append(button)

        # Entrada para agregar eventos
        self.event_frame = ttk.Frame(self.main_frame)
        self.event_frame.grid(row=2, column=0, columnspan=7, pady=10)

        ttk.Label(self.event_frame, text="Evento:").grid(row=0, column=0, sticky="E")
        self.event_entry = ttk.Entry(self.event_frame, width=40)
        self.event_entry.grid(row=0, column=1, columnspan=4, sticky="W")

        self.add_event_button = ttk.Button(self.event_frame, text="Agregar Evento", command=self.add_event)
        self.add_event_button.grid(row=0, column=5)

        # Lista de eventos
        self.events_frame = ttk.Frame(self.main_frame)
        self.events_frame.grid(row=3, column=0, columnspan=7, pady=10)

        self.events_tree = ttk.Treeview(self.events_frame, columns=("Fecha", "Evento"), show="headings", height=8)
        self.events_tree.heading("Fecha", text="Fecha")
        self.events_tree.heading("Evento", text="Evento")
        self.events_tree.column("Fecha", width=100, anchor="center")
        self.events_tree.column("Evento", width=300, anchor="w")
        self.events_tree.grid(row=0, column=0, columnspan=6)

        self.delete_event_button = ttk.Button(self.events_frame, text="Eliminar Evento", command=self.delete_event)
        self.delete_event_button.grid(row=1, column=5)

        # Estado actual del día seleccionado
        self.selected_date = None

        # Renderizar el mes actual
        self.render_calendar()

    def render_calendar(self):
        self.month_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        for button in self.day_buttons:
            button.config(text="", state="disabled", style="")

        first_day_of_month = datetime.date(self.current_year, self.current_month, 1)
        start_day = (first_day_of_month.weekday() + 1) % 7
        num_days = calendar.monthrange(self.current_year, self.current_month)[1]

        for day in range(1, num_days + 1):
            btn_index = start_day + day - 1
            button = self.day_buttons[btn_index]
            button.config(text=str(day), state="normal")

            date = datetime.date(self.current_year, self.current_month, day)
            if date in self.events:
                button.config(style="Highlighted.TButton")

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.render_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.render_calendar()

    def select_day(self, row, col):
        day = self.day_buttons[(row - 1) * 7 + col].cget("text")
        if day:
            self.selected_date = datetime.date(self.current_year, self.current_month, int(day))
            messagebox.showinfo("Día seleccionado", f"Has seleccionado el {self.selected_date.strftime('%d/%m/%Y')}")

    def add_event(self):
        if not self.selected_date:
            messagebox.showerror("Error", "Debe seleccionar una fecha antes de agregar un evento.")
            return

        event = self.event_entry.get()
        if not event:
            messagebox.showerror("Error", "Debe escribir un evento.")
            return

        if self.selected_date not in self.events:
            self.events[self.selected_date] = []
        self.events[self.selected_date].append(event)

        self.events_tree.insert("", "end", values=(self.selected_date.strftime('%d/%m/%Y'), event))
        self.event_entry.delete(0, tk.END)
        self.render_calendar()

    def delete_event(self):
        selected_item = self.events_tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar un evento para eliminar.")
            return

        for item in selected_item:
            values = self.events_tree.item(item, "values")
            date = datetime.datetime.strptime(values[0], "%d/%m/%Y").date()
            event = values[1]

            self.events[date].remove(event)
            if not self.events[date]:
                del self.events[date]

            self.events_tree.delete(item)

        self.render_calendar()

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.configure("Highlighted.TButton", background="lightblue")

    app = SchoolCalendar(root)
    root.mainloop()
