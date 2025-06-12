def simulador_alarma(tiempo_total):
    segundo_actual = 0
    pausar_alarma = 10
    while segundo_actual <= tiempo_total:
        segundo_actual += 1
        if segundo_actual == pausar_alarma:
            print('Omitiendo alarma en segundo ', segundo_actual)
            pausar_alarma += 10
            continue
        elif segundo_actual == tiempo_total:
            print('Alarma activada, segundo actual: ', segundo_actual)
            break
        else:
            print('Alarma activada, segundo actual: ', segundo_actual)

    print(f'Alarma desactivada a los {segundo_actual} segundos')


simulador_alarma(21)