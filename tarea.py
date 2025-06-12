
def cabecera():
    a = """
        ██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗ █████╗ ██╗      ██████╗
        ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔════╝
        ███████║███████║███████╗███████║██║     ███████║██║     ██║     
        ██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██║██║     ██║     
        ██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║███████╗╚██████╗
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
                                              <Juan Daniel>                         
        """
    print(a)


# Saco por pantalla la cabecera de la aplicación
cabecera()
# Solicito al usuario el mensaje
mensaje = input("Introduce un mensaje: ")
# Obtengo el hash del mensaje
hash_value = hash(mensaje)
# Saco por pantalla el hash
print("\nEl hash del mensaje es:", hash_value)
