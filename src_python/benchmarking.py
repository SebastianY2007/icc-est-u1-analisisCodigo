import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:

    def __init__(self):
        print('Bench inicializado')

    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()

        arreglo = self.build_arreglo(1000)
        
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        
        
        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        medir_tiempo = self.medir_tiempo(tarea, arreglo)

        print(medir_tiempo)

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
    
    def medir_tiempo(self, tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio