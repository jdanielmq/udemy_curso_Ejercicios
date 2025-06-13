menu = {
    'Pizza Margarita': 8.99,
    'Hamburguesa Clásica': 5.99,
    'Ensalada César': 7.5,
    'Agua Mineral': 1.5
}

def realizar_pedido(alimento_seleccionado,dinero):

    print('Menu de Alimentos:')
    for alimento, precio in menu.items():
        print('{}: {}'.format(alimento, precio))

    try:
        if alimento_seleccionado not in menu:
            raise ValueError('El alimento seleccionado no está en el menú.\n')

        if menu[alimento_seleccionado] >  dinero:
            raise ValueError('No se disponen de suficientes fondos para realizar el pedido \n')

        coste_total = menu[alimento_seleccionado]
        print(f'\nPedido realizado con éxito. Alimento seleccionado: {alimento_seleccionado}, Total a pagar: ${coste_total:.2f} \n')

    except ValueError as e:
        print('Error en el pedido: {}'.format(e))


alimento_1 = 'Pizza Margarita'
dinero_1 = 10
realizar_pedido(alimento_1,dinero_1)

alimento_2 = 'Pizza Margarita'
dinero_2 = 2
realizar_pedido(alimento_2,dinero_2)

alimento_3 = 'Sandwich mixto'
dinero_3 = 10
realizar_pedido(alimento_3,dinero_3)
