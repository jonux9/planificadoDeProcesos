from typing import List, Dict


class Process:
    """
    Representa un proceso dentro del sistema de planificación Round-Robin.

    Atributos:
        pid (str): Identificador del proceso (ej. "P1").
        arrival_time (int): Tiempo de llegada del proceso al sistema.
        burst_time (int): Tiempo total de ejecución necesario (tiempo de ráfaga).
        remaining_time (int): Tiempo restante de ejecución.
        completion_time (int): Tiempo en el que el proceso terminó.
        start_times (List[int]): Lista de tiempos de inicio por cada ejecución.
        end_times (List[int]): Lista de tiempos de finalización por cada ejecución.
    """
    def __init__(self, pid: str, arrival_time: int, burst_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.start_times = []
        self.end_times = []

    def is_completed(self) -> bool:
        """
        Verifica si el proceso ha finalizado su ejecución.

        Returns:
            bool: True si el proceso terminó, False en caso contrario.
        """
        return self.remaining_time == 0


def round_robin_scheduler(processes: List[Process], quantum: int) -> Dict:
    """
    Ejecuta la planificación Round-Robin apropiativa sobre una lista de procesos.

    Args:
        processes (List[Process]): Lista de procesos a planificar.
        quantum (int): Tiempo máximo de ejecución por proceso antes de ser interrumpido.

    Returns:
        Dict: Contiene dos claves:
            - 'processes': Lista de diccionarios con métricas por proceso.
            - 'execution_log': Lista de ejecuciones con PID y rangos de tiempo.
    """
    time = 0
    queue = []
    completed = []
    execution_log = []

    processes = sorted(processes, key=lambda p: p.arrival_time)
    i = 0  # Índice del siguiente proceso por llegar

    while len(completed) < len(processes):
        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1  # Tiempo muerto si no hay procesos en cola
            continue

        current = queue.pop(0)
        exec_time = min(current.remaining_time, quantum)

        current.start_times.append(time)
        time += exec_time
        current.remaining_time -= exec_time
        current.end_times.append(time)

        execution_log.append({
            'pid': current.pid,
            'start': current.start_times[-1],
            'end': current.end_times[-1]
        })

        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not current.is_completed():
            queue.append(current)
        else:
            current.completion_time = time
            completed.append(current)

    results = []
    for p in processes:
        turnaround = p.completion_time - p.arrival_time
        waiting = turnaround - p.burst_time
        results.append({
            'pid': p.pid,
            'arrival_time': p.arrival_time,
            'burst_time': p.burst_time,
            'completion_time': p.completion_time,
            'turnaround_time': turnaround,
            'waiting_time': waiting
        })

    return {
        'processes': results,
        'execution_log': execution_log
    }
