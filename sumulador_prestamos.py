class SimuladorPrestamo:
    def __init__(self, detalles_prestamo, años=30, precio_vivienda=300000):
        self.tasa_mensual = detalles_prestamo.imag / 12 / 100
        self.numero_pagos = años * 12
        self.entrada = detalles_prestamo.real
        self.prestamo = precio_vivienda - self.entrada
        self.precio_vivienda = precio_vivienda
        self.cuota_mensual = 0
        self.años = años
        self.tasa_interes = detalles_prestamo.imag

    def mostrar_resultados(self):
        print(f"----- Simulación Hipoteca -----")
        print(f"Para una vivienda de {self.precio_vivienda} euros, aportando una entrada de {self.entrada} euros y con una tasa de interés del {self.tasa_interes}% anual durante {self.años} años:")
        print(f"Cuota mensual a pagar: {self.cuota_mensual} euros")
        print(f"----- Fin de la Simulación -----")


    def calcular_pago_total(self):
        self.cuota_mensual = self.prestamo * (self.tasa_mensual * (1 + self.tasa_mensual) ** self.numero_pagos) / (
                    (1 + self.tasa_mensual) ** self.numero_pagos - 1)

detalles_prestamo = 50000 + 2.5j
años = 30
precio_vivienda = 300000

simulador = SimuladorPrestamo(detalles_prestamo,años,precio_vivienda)
simulador.calcular_pago_total()
simulador.mostrar_resultados()


