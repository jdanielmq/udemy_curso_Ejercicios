def recomendar_pelicula(genero, edad):
    if genero == 'accion' and edad >= 13:
        return 'Deadpool'
    elif genero == 'accion' and edad < 13:
        return 'Regreso al futuro'
    elif genero == 'comedia':
        return 'Aterriza como puedas'
    else:
        return 'Explorar otros generos'


def solicitar_datos():
    genero_favorito = input('ingrese el genero favorito: ')
    edad_usuario = input('ingrese su edad actual: ')

    return genero_favorito, edad_usuario


genero_favorito, edad_usuario = solicitar_datos()

pelicula_recomendada = recomendar_pelicula(genero_favorito, edad_usuario)
print(
    f'Teniendo en cuenta tu edad ({edad_usuario}) y tu genero favorito {genero_favorito}, te recomiendo la siguiente pelicula: {pelicula_recomendada}')


