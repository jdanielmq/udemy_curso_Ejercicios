def formato_notificacion(func):
    def wrapper(self, plataforma):
        print(f"***** NUEVO EVENTO en {plataforma} *****")
        func(self, plataforma)
        print(f"***** FIN DEL EVENTO en {plataforma} *****\n")
    return wrapper

class NotificadorRedSocial:
    def __init__(self):
        self.evento = "Lanzamiento de un nuevo libro"

    @formato_notificacion
    def notificar_evento(self, plataforma):
        if plataforma == "Twitter":
            print(f"Tweet: {self.evento}")
        elif plataforma == "Instagram":
            print(f"Instagram Story: {self.evento}")
        elif plataforma == "Facebook":
            print(f"Post en Facebook: {self.evento}")
        else:
            print("Plataforma no soportada")


# Simulación de envío de notificaciones
notificador = NotificadorRedSocial()
plataformas = ["Twitter", "Instagram", "Facebook", "LinkedIn"]
for plataforma in plataformas:
    notificador.notificar_evento(plataforma)