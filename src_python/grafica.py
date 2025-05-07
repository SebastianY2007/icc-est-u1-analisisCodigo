import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y, label = "Linea 1", color = "blue")

# Agregar Parametros

plt.title("Primer Grafico")
plt.xlabel("Datos eje X")
plt.ylabel("Datos eje Y")

plt.legend()
plt.show()