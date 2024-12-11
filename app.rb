require 'tk'
require 'sqlite3'
require_relative 'config_db'

def connect_db
  SQLite3::Database.new 'students.db'
end

def add_student
  db = connect_db
  db.execute "INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)",
             [first_name_entry.value, last_name_entry.value, email_entry.value]
  Tk.messageBox('type' => 'ok', 'icon' => 'info', 'title' => 'Éxito', 'message' => 'Estudiante añadido exitosamente')
  list_students
end

def list_students
  db = connect_db
  students_list.delete(0, 'end')
  db.execute "SELECT * FROM students" do |row|
    students_list.insert('end', row.join(' | '))
  end
end

def delete_student
  db = connect_db
  db.execute "DELETE FROM students WHERE id=?", [id_entry.value]
  Tk.messageBox('type' => 'ok', 'icon' => 'info', 'title' => 'Éxito', 'message' => 'Estudiante eliminado exitosamente')
  list_students
end

def update_student
  db = connect_db
  db.execute "UPDATE students SET first_name=?, last_name=?, email=? WHERE id=?",
             [first_name_entry.value, last_name_entry.value, email_entry.value, id_entry.value]
  Tk.messageBox('type' => 'ok', 'icon' => 'info', 'title' => 'Éxito', 'message' => 'Estudiante actualizado exitosamente')
  list_students
end

root = TkRoot.new { title "Gestión de Estudiantes" }

TkLabel.new(root) { text 'ID' }.grid('row' => 0, 'column' => 0)
id_entry = TkEntry.new(root).grid('row' => 0, 'column' => 1)

TkLabel.new(root) { text 'Nombre' }.grid('row' => 1, 'column' => 0)
first_name_entry = TkEntry.new(root).grid('row' => 1, 'column' => 1)

TkLabel.new(root) { text 'Apellido' }.grid('row' => 2, 'column' => 0)
last_name_entry = TkEntry.new(root).grid('row' => 2, 'column' => 1)

TkLabel.new(root) { text 'Correo Electrónico' }.grid('row' => 3, 'column' => 0)
email_entry = TkEntry.new(root).grid('row' => 3, 'column' => 1)

TkButton.new(root) { text 'Añadir Estudiante'; command { add_student } }.grid('row' => 4, 'column' => 0)
TkButton.new(root) { text 'Eliminar Estudiante'; command { delete_student } }.grid('row' => 4, 'column' => 1)
TkButton.new(root) { text 'Actualizar Estudiante'; command { update_student } }.grid('row' => 4, 'column' => 2)

students_list = TkListbox.new(root).grid('row' => 5, 'column' => 0, 'columnspan' => 3)

list_students

Tk.mainloop




