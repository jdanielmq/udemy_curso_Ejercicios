class GestionAsistencia:
    def __init__(self):
        self.asistentes_actividad_A = set()
        self.asistentes_actividad_B = set()

    def añadir_asistente(self, actividad, estudiante):
        if actividad == 'A':
            self.asistentes_actividad_A.add(estudiante)
        elif actividad == 'B':
            self.asistentes_actividad_B.add(estudiante)

    def asistencia_total(self):
        return self.asistentes_actividad_A.union(self.asistentes_actividad_B)

    def asistencia_comun(self):
        return self.asistentes_actividad_A.intersection(self.asistentes_actividad_B)

    def diferencia_actividad_A(self):
        return self.asistentes_actividad_A.difference(self.asistentes_actividad_B)

    def diferencia_actividad_B(self):
        return self.asistentes_actividad_B.difference(self.asistentes_actividad_A)



gestion = GestionAsistencia()
gestion.añadir_asistente('A','Juan')
gestion.añadir_asistente('A','Ana')
gestion.añadir_asistente('B','Ana')
gestion.añadir_asistente('B','Luis')

print("Asistentes actividad A:", gestion.asistentes_actividad_A)
print("Asistentes actividad B:", gestion.asistentes_actividad_B)
print("Asistencia total:", gestion.asistencia_total())
print("Asistencia común:", gestion.asistencia_comun())
print("Diferencia actividad A:", gestion.diferencia_actividad_A())
print("Diferencia actividad B:", gestion.diferencia_actividad_B())