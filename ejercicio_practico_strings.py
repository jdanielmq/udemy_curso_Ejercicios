class GeneradorNombresUsuario:
    def __init__(self, nombre, apellido, año):
        self._nombre = nombre
        self._apellido = apellido
        self._año = año
        self._nombre_completo = ""
        return

    def generar_nombre_usuario(self):
        nombre_completo = self._nombre.lower() + " " + self._apellido.upper() + " " + self._año
        return self.validar_nombre_usuario(nombre_completo.replace(" ", ""))



    def validar_nombre_usuario(self, nombre_completo):
        largo_nombre = len(nombre_completo.strip())
        if largo_nombre < 8:
            print('El nombre de usuario no cumple con los criterios de validación.')
            return False

        final_cadena = nombre_completo[-4:]
        if final_cadena.isdigit() == False:
            print('El nombre de usuario no cumple con los criterios de validación.')
            return False


        self._nombre_completo =  (nombre_completo.strip()).replace(" ", "")
        return True

    def mostrar_nombre_usuario(self):
        if self.generar_nombre_usuario() == True:
            print(f'Nombre de usuario generado: ', self._nombre_completo)

        return


usuario = GeneradorNombresUsuario("JUAN", "muñoz", "1981")
usuario.generar_nombre_usuario()
usuario.mostrar_nombre_usuario()




