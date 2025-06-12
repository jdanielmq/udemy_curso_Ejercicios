class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = disponible

    def información(self):
        print('Información del Libro: ', self._titulo)
        print('Titulo:', self._titulo)
        print('Autor:', self._autor)
        print('ISBN:', self._isbn)
        if self._disponible is True:
            print('Disponibilidad del Libro: Disponible')
        else:
            print('Disponibilidad del Libro: Prestado')

    def prestar_libro(self):
        if self._disponible is False:
            print('Este libro ya está prestado')
            return
        else:
            self._disponible = False
            print('El libro {} ha sido prestado'.format(self._titulo))
            self.información()
            return

    def devolver_libro(self):
        if self._disponible is True:
            print('Este libro ya está en la biblioteca')
            return
        else:
            self._disponible = True
            print('El libro {} ha sido devuelto a la biblioteca.'.format(self._titulo))
            self.información()
            return




libro1 = Libro("Harry Potter y la piedra filosofal",'J.K. Rowling','978-0747532743')
libro2 = Libro('1984','George Orwell', '978-0451524935')

libro1.prestar_libro()
libro1.devolver_libro()

libro2.prestar_libro()
libro2.devolver_libro()




