class MetodosOrdenamiento:

    def sort_bubble(self, arreglo):
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
    
    def sort_selection(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n - 1):
            minIdx = i
            for j in range(n):
                if arreglo[minIdx] > arreglo[j]:
                    minIdx = j
            if minIdx != i:
                # arreglo[minIdx], arreglo[i] = arreglo[i], arreglo[minIdx]
                
                aux = arreglo[minIdx]
                arreglo[minIdx] = arreglo [i]
                arreglo[i] = aux

        return arreglo