#  Planificador de procesos (Python + Tkinter)

Este proyecto es un **Planificador procesos** utilizando el algoritmo **Round-Robin apropiativo**, desarrollado en **Python** con una interfaz gráfica construida con **Tkinter**.

---

##  Características

- Ingreso de procesos con tiempo de llegada y duración (burst time).
- Ingreso del quantum del sistema operativo.
- Ejecución de la planificación Round-Robin.
- Visualización de:
  - Tiempos de ejecución de cada proceso
  - Tiempos de espera y turnaround
  - Log de ejecución paso a paso
- Interfaz gráfica amigable
- Implementado con buenas prácticas y estructura clara.

---

##  Tecnologías utilizadas

- Python 3.11+
- Tkinter (interfaz gráfica)
- pipenv (gestión de entorno y dependencias)

---

##  Ejecución del proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/jomax96/round-robin-scheduler.git
cd round-robin-scheduler
```

### 2. Crea entorno con pipenv

```bash
pipenv install --python 3.11
pipenv shell
```

### 3. Ejecuta la interfaz gráfica

```bash
pipenv run python ui.py
```

---

##  Capturas de pantalla

<!-- Agrega aquí una imagen si lo deseas -->
<!-- ![Interfaz](./screenshot.png) -->

---

##  Teoría del algoritmo Round-Robin

- Cada proceso se ejecuta por un tiempo fijo (quantum).
- Si el proceso no finaliza, se interrumpe y vuelve al final de la cola.
- Se repite el ciclo hasta que todos los procesos estén completados.
- Es un algoritmo apropiativo, justo y útil en sistemas multitarea.

---

##  Estructura del proyecto

```
round-robin-scheduler/
│
├── scheduler.py      # Lógica del algoritmo Round-Robin
├── main.py           # Versión en consola
├── ui.py             # Interfaz gráfica con Tkinter
├── Pipfile           # Dependencias (pipenv)
├── README.md         # Este archivo
└── .gitignore
```

---

##  Autor

- **[@jomax96](https://github.com/jomax96)**

---

##  Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
