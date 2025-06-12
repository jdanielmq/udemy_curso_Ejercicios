class SistemaCalificaciones:
    def __init__(self):
        self.calificaciones = []

    def añadir_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_calificaciones(self):
        for calificacion in self.calificaciones:
            print(calificacion)

    def calificacion_promedio(self):
        if len(self.calificaciones) == 0:
            return 0

        return sum(self.calificaciones) / len(self.calificaciones)

    def ordenar_calificaciones(self):
        self.calificaciones.sort()


sistema = SistemaCalificaciones()
sistema.añadir_calificacion(8)
sistema.añadir_calificacion(9.5)
sistema.añadir_calificacion(7)
sistema.añadir_calificacion(10)

print('Calificaciones Originales:')
sistema.mostrar_calificaciones()

print('Promedio : ', sistema.calificacion_promedio())
sistema.ordenar_calificaciones()

print('Calificaciones Ordenadas:')
sistema.mostrar_calificaciones()

