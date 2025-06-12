class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._habitat = habitat

    def mostrar_info(self):
        print(f"--> Nombre: {self._nombre}\nEspecie: {self._especie}\nEdad: {self._edad}\nHábitat: {self._habitat._tipo_habitat}, {self._habitat._temperatura}")


class Habitat:
    def __init__(self, tipo, temperatura):
        self._tipo_habitat = tipo
        self._temperatura = temperatura

class Mamifero(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_pelaje):
        super().__init__(nombre,especie,edad,habitat)
        self._tipo_pelaje = tipo_pelaje

    def mostrar_info(self):
        super().mostrar_info()
        print('Tipo de pelaje: {}'.format(self._tipo_pelaje))


class Ave(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        super().__init__(nombre,especie,edad,habitat)
        self._tipo_plumaje = tipo_plumaje

    def mostrar_info(self):
        super().mostrar_info()
        print('Tipo de plumaje: {}'.format(self._tipo_plumaje))


class Zoologico:
    def __init__(self, nombre):
        self._nombre = nombre
        self._animales = []

    def añadir_animal(self, animal):
        self._animales.append(animal)

    def mostrar_animales(self):
        print('Animales en {}'.format(self._nombre))
        for animal in self._animales:
            animal.mostrar_info()



zoologico = Zoologico('Zoologico Metropolitano')

habitat1 = Habitat('Sabana','Calido')
habitat2 = Habitat('Bosque','Templado')

leon = Mamifero('Simba','Leon',5, habitat1,'Corto')
canario = Ave('Piolin','Canario',2,habitat2,'Suave')

zoologico.añadir_animal(leon)
zoologico.añadir_animal(canario)
zoologico.mostrar_animales()



