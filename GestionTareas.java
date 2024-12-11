import java.util.ArrayList;
import java.util.Scanner;

class Tarea {
    String nombre;
    boolean completada;

    Tarea(String nombre) {
        this.nombre = nombre;
        this.completada = false;
    }
}

public class GestionTareas {
    static ArrayList<Tarea> tareas = new ArrayList<>();

    public static void agregarTarea(String nombre) {
        tareas.add(new Tarea(nombre));
        System.out.println("Tarea agregada exitosamente.");
    }

    public static void listarTareas() {
        System.out.println("Lista de Tareas:");
        for (int i = 0; i < tareas.size(); i++) {
            Tarea tarea = tareas.get(i);
            System.out.printf("%d. %s [%s]%n", i + 1, tarea.nombre, tarea.completada ? "Completada" : "Pendiente");
        }
    }

    public static void completarTarea(int indice) {
        if (indice >= 0 && indice < tareas.size()) {
            tareas.get(indice).completada = true;
            System.out.println("Tarea completada.");
        } else {
            System.out.println("Índice no válido.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Agregar Tarea");
            System.out.println("2. Listar Tareas");
            System.out.println("3. Completar Tarea");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine();  // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    System.out.print("Nombre de la Tarea: ");
                    String nombre = scanner.nextLine();
                    agregarTarea(nombre);
                    break;
                case 2:
                    listarTareas();
                    break;
                case 3:
                    System.out.print("Índice de la Tarea a completar: ");
                    int indice = scanner.nextInt();
                    completarTarea(indice - 1);
                    break;
                case 4:
                    System.out.println("Saliendo...");
                    return;
                default:
                    System.out.println("Opción no válida, por favor intente de nuevo.");
            }
        }
    }
}
