import tkinter as tk
from tkinter import ttk, messagebox
from scheduler import Process, round_robin_scheduler


class RoundRobinApp:
    """
    Interfaz gráfica principal de la aplicación Round-Robin usando Tkinter.

    Permite al usuario:
        - Ingresar procesos
        - Definir el quantum
        - Ejecutar el algoritmo
        - Visualizar los resultados
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Planificador Round Robin")

        self.processes = []

        # Entrada de Quantum
        tk.Label(root, text="Quantum:").grid(row=0, column=0, sticky="e")
        self.quantum_entry = tk.Entry(root)
        self.quantum_entry.grid(row=0, column=1)

        # Entrada de Tiempo de Llegada
        tk.Label(root, text="Tiempo de llegada:").grid(row=1, column=0, sticky="e")
        self.arrival_entry = tk.Entry(root)
        self.arrival_entry.grid(row=1, column=1)

        # Entrada de Duración
        tk.Label(root, text="Duración:").grid(row=2, column=0, sticky="e")
        self.burst_entry = tk.Entry(root)
        self.burst_entry.grid(row=2, column=1)

        # Botón para agregar proceso
        tk.Button(root, text="Agregar Proceso", command=self.agregar_proceso).grid(row=3, column=0, columnspan=2, pady=5)

        # Tabla con procesos agregados
        self.tree = ttk.Treeview(root, columns=("Llegada", "Duración"), show="headings")
        self.tree.heading("Llegada", text="Llegada")
        self.tree.heading("Duración", text="Duración")
        self.tree.grid(row=4, column=0, columnspan=2, pady=10)

        # Botón para ejecutar el algoritmo
        tk.Button(root, text="Ejecutar", command=self.ejecutar_planificacion).grid(row=5, column=0, columnspan=2)

        # Área de resultados
        self.result_text = tk.Text(root, height=15, width=60)
        self.result_text.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_proceso(self):
        """
        Agrega un proceso a la lista y actualiza la tabla.
        """
        try:
            arrival = int(self.arrival_entry.get())
            burst = int(self.burst_entry.get())
            pid = f"P{len(self.processes) + 1}"
            self.processes.append(Process(pid, arrival, burst))
            self.tree.insert("", "end", values=(arrival, burst))
            self.arrival_entry.delete(0, tk.END)
            self.burst_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Los campos deben ser números enteros")

    def ejecutar_planificacion(self):
        """
        Ejecuta el algoritmo Round-Robin y muestra los resultados en la interfaz.
        """
        try:
            quantum = int(self.quantum_entry.get())
            if not self.processes:
                messagebox.showwarning("Atención", "Agrega al menos un proceso")
                return

            result = round_robin_scheduler(self.processes, quantum)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "=== Resultados ===\n")
            for p in result["processes"]:
                self.result_text.insert(
                    tk.END,
                    f"{p['pid']} | Llegada: {p['arrival_time']} | Duración: {p['burst_time']} | "
                    f"Finaliza: {p['completion_time']} | Turnaround: {p['turnaround_time']} | "
                    f"Espera: {p['waiting_time']}\n"
                )

            self.result_text.insert(tk.END, "\n=== Log de ejecución ===\n")
            for log in result["execution_log"]:
                self.result_text.insert(tk.END, f"{log['pid']} ejecutó de t={log['start']} a t={log['end']}\n")

        except ValueError:
            messagebox.showerror("Error", "Quantum debe ser un número entero")


if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinApp(root)
    root.mainloop()
