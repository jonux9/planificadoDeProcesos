from scheduler import Process, round_robin_scheduler


def get_process_input():
    print("=== INGRESO DE PROCESOS ===")
    num = int(input("¿Cuántos procesos deseas ingresar?: "))
    processes = []

    for i in range(num):
        print(f"\n--- Proceso P{i + 1} ---")
        arrival = int(input("Tiempo de llegada: "))
        burst = int(input("Duración (burst time): "))
        processes.append(Process(pid=f'P{i + 1}', arrival_time=arrival, burst_time=burst))

    return processes


def main():
    print("===== PLANIFICADOR ROUND ROBIN (APROPIATIVO) =====")
    quantum = int(input("Ingresa el quantum del sistema: "))
    processes = get_process_input()

    result = round_robin_scheduler(processes, quantum)

    print("\n=== RESULTADOS ===")
    for p in result['processes']:
        print(
            f"{p['pid']} | Llegada: {p['arrival_time']} | Duración: {p['burst_time']} | "
            f"Finaliza: {p['completion_time']} | Turnaround: {p['turnaround_time']} | "
            f"Espera: {p['waiting_time']}"
        )

    print("\n=== LOG DE EJECUCIÓN ===")
    for log in result['execution_log']:
        print(f"{log['pid']} ejecutó de t={log['start']} a t={log['end']}")


if __name__ == "__main__":
    main()
