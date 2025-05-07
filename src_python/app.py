from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona")

    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    size = 1000

    sizes = [500, 1000, 2000]
    resultados = []

    for size in sizes:
        arreglo_base = benchmark.build_arreglo(size)

        metodos_ordenamiento = {
            "Burbuja": metodos.sort_bubble,
            "Seleccion": metodos.sort_selection
        }

        for nombre, metodo in metodos_ordenamiento.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (size, nombre, tiempo)
            resultados.append(tupla_resultado)

        for resultado in resultados:
            size, nombre, tiempo = resultado
            print(f"Tamaño: {size}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodos = {
        "Burbuja" : [],
        "Seleccion" : []
    }

    # Clasificar los tiempos segun el metodo

    for size, nombre, tiempo in resultados:
        tiempos_by_metodos[nombre].append(tiempo)

    # Crear una grafica 

    plt.figure(figsize = (10, 6))

    # Graficar una linea de tiempo para cada metodo
    # El Y sean los tiempos obtenidos
    # El X sea el tamaño del arreglo

    for nombre, tiempos in tiempos_by_metodos.items():
        plt.plot(sizes, tiempos, label = nombre, marker = 'o')

    # Agregar los Parametros
    
    plt.xlabel("Tamaño del Arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparativa Metodos")
    plt.grid()
    plt.show()