from logging import exception


class Exceptions:
    def __init__(self):
        print('--- inicia la clases de exceptions ---')

    def ejemplo1_exception(self):
        print('--- ejemplo 1 ---')
        try:
            print(var)
        except NameError:
            var = "Hola mundo"
        print(var)

    def ejempl2_exception(self):
        print('--- ejemplo 2 ---')
        print("Sentencias de codigo antes del try")
        try:
            print("Codigo antes de la excepcion")
            10 + "3"
            print("Codigo despues de la excepcion")
        except TypeError:
            print("No se puede sumar un numero entero y un string")
        print("Sentencias de codigo despues del except")

    def ejempl3_exception(self):
        print('--- ejemplo 3 ---')
        try:
            10 + "3"
        except:
            print("No se puede sumar un entero y un string")

    def ejempl4_exception(self):
        print('--- ejemplo 4 ---')
        try:
            50 / 0
        except NameError:
            print("Gestionando excepcion NameError")
        except TypeError:
            print("Gestionando execpcion Type Error")
        except ZeroDivisionError:
            print("No puedes dividir un numero por 0")

    def ejempl5_exception(self):
        print('--- ejemplo 5 ---')
        try:
            print(variable)
        except NameError as error:
            print("Objeto de tipo:", type(error))
            print("La excepcion consiste en:", error)
    def ejempl6_exception(self):
        print('--- ejemplo 6 ---')
        colores_permitidos = ("azul", "verde", "rojo")
        color = "amarillo"
        if color not in colores_permitidos:
            raise Exception("El color {} no se encuentra en la lista de colores permitidos".format(color))

    def ejempl7_exception(self):
        print('--- ejemplo 7 ---')
        colores_permitidos = ("azul", "verde", "rojo")
        color = "verde"
        if color not in colores_permitidos:
            raise Exception("El color {} no se encuentra en la lista de colores permitidos".format(color))

        print('El color {} si se encuentra en la lista de colores permitidos'.format(color))

ex = Exceptions()
ex.ejemplo1_exception()
ex.ejempl2_exception()
ex.ejempl3_exception()
ex.ejempl4_exception()
ex.ejempl5_exception()
try:
    ex.ejempl6_exception()
except Exception as error:
    print("La excepcion consiste en:", error)

ex.ejempl7_exception()




