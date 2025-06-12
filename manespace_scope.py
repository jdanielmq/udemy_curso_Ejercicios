recursos_ecosistema = {
    'agua': 1000,
    'alimento': 800
}

def animal_interactua(tipo_animal, cantidad_alimento, agua_consumida=None):
    if agua_consumida is None: agua_consumida = 0
    agua = recursos_ecosistema['agua']
    alimento = recursos_ecosistema['alimento']

    if agua_consumida > agua or cantidad_alimento > alimento:
        print('Recursos insuficientes en el ecosistema')
    else:
        if tipo_animal == 'herbívoro':
            recursos_ecosistema['agua'] =   recursos_ecosistema['agua'] - agua_consumida
            recursos_ecosistema['alimento'] = recursos_ecosistema['alimento'] - cantidad_alimento
            print('Un herbívoro ha consumido {} de agua y {} de alimento.'.format(agua_consumida, cantidad_alimento))
        elif tipo_animal == 'carnívoro':
            recursos_ecosistema['alimento'] = recursos_ecosistema['alimento'] - cantidad_alimento
            print('Un carnívoro ha consumido {} de alimento.'.format(cantidad_alimento))

    print('Estado actual del ecosistema: ', recursos_ecosistema)


def lluvia(agua=0):
    if agua == 0:
        print('al dia de hoy no ha llovido!!!')
        return
    else:
        recursos_ecosistema['agua'] += agua
        print('¡Ha llovido! Se añadieron {} unidades de agua al ecosistema.'.format(agua))
        return





print('Inicio del día en el ecosistema: ', recursos_ecosistema)
animal_interactua('herbívoro',200,200)
animal_interactua('carnívoro',200,300)
lluvia(1000)
print('Fin del día en el ecosistema: ',recursos_ecosistema)