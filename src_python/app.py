from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("Funciona")

    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    size = 50000
    arreglo_base = benchmark.build_arreglo(size)

    metodos = {
        "Burbuja": metodos.sort_bubble,
        "Seleccion": metodos.sort_selection
    }

    resultados = []

    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tupla_resultado = (size, nombre, tiempo)
        resultados.append(tupla_resultado)

    for resultado in resultados:
        size, nombre, tiempo = resultado
        print(f"Tamaño: {size}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")