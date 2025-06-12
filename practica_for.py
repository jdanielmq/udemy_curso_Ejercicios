def añadir_tarea(tarea):
    tareas_fichero = open('tareas.txt', 'r')
    lista_tareas = tareas_fichero.readlines()
    tareas_fichero.close()
    lista_tareas += [tarea]
    return lista_tareas


def gestionar_tareas(tareas):
    print('Tareas pendientes de realizar:')
    num_tareas = 0
    for tarea_pendiente in tareas:
        num_tareas += 1
        print(f'{num_tareas}. {tarea_pendiente}')

    print(f'Hay {num_tareas} tareas pendientes de realizar.')


tareas = añadir_tarea('Pagar la factura de internet.')
gestionar_tareas(tareas)