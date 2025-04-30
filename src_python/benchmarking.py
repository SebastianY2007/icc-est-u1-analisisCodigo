import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print('Bench inicializado')
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.build_arreglo(50000)
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)

        print(f"Tiempo en Millis {tiempoMillis}s")
        print(f"Tiempo en Nano {tiempoNano}s")

    def build_arreglo(self, size):
        array = []
        for i in range(size):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0