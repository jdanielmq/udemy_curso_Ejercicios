def mover_ascensor(piso_actual, piso_deseado):
    piso = piso_actual
    if piso_actual < piso_deseado:
        print('El asensor va subiendo')
        while piso < piso_deseado:
            print(f'Subiendo al piso {piso_deseado}. Piso actual: {piso}')
            piso += 1

        print(f'Piso {piso} alcanzado')
    else:
        print('El asensor va bajando')
        while piso > piso_deseado:
            print(f'Bajando al piso {piso_deseado}. Piso actual: {piso}')
            piso -= 1

        print(f'Piso {piso} alcanzado')


mover_ascensor(2, 6)
mover_ascensor(10, 4)
