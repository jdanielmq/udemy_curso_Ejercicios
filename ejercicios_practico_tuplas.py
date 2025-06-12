class AnalisisVentas:
    def __init__(self, datos_ventas):
        self.datos_ventas = datos_ventas

    def venta_maxima(self):
        valor_max = max(self.datos_ventas)
        indice_max = self.datos_ventas.index(valor_max)
        return indice_max, valor_max

    def venta_minima(self):
        valor_min = min(self.datos_ventas)
        indice_min = self.datos_ventas.index(valor_min)
        return indice_min, valor_min

    def frecuencia_venta(self,venta):
        return self.datos_ventas.count(venta)


datos_ventas = (100,150,150,50,250,300,100,350,200,200,150)
analisis = AnalisisVentas(datos_ventas)
indice_max, venta_max = analisis.venta_maxima()
indice_min, venta_min = analisis.venta_minima()
valor_venta = 200
frec_venta = analisis.frecuencia_venta(valor_venta)

print("Ventas totales:", datos_ventas)
print(f"La venta máxima tiene el índice {indice_max} y es {venta_max}.")
print(f"La venta mínima tiene el índice {indice_min} y es {venta_min}.")
print(f"Frecuencia de la venta por un valor de {valor_venta} es {frec_venta}.")