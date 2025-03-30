from typing import List, Dict


class Process:
    def __init__(self, pid: str, arrival_time: int, burst_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.start_times = []
        self.end_times = []

    def is_completed(self):
        return self.remaining_time == 0


def round_robin_scheduler(processes: List[Process], quantum: int) -> Dict:
    time = 0
    queue = []
    completed = []
    execution_log = []

    processes = sorted(processes, key=lambda p: p.arrival_time)
    i = 0  # índice para los procesos que aún no llegan

    while len(completed) < len(processes):
        # Añadir nuevos procesos al tiempo actual
        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1  # tiempo muerto
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

        # Añadir nuevos procesos que llegaron durante esta ejecución
        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not current.is_completed():
            queue.append(current)
        else:
            current.completion_time = time
            completed.append(current)

    # Cálculos finales
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
