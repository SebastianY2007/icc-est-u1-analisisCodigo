class MetodosOrdenamiento:

    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    # Solo en Python arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

                    aux = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = aux
        return arreglo