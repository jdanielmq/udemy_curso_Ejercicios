def validar_inscripcion(edad, experencia):
    try:
        assert edad >= 18, 'Debe tener al menos 18 años para inscribirse.'
        assert experencia >= 5, 'Necesita un nivel de experiencia mínimo de 5 para inscribirse.'
    except AssertionError as e:
        print("Error en la inscripción:", e)
    else:
        print('Inscripción realizada con éxito. ¡Bienvenido al torneo!')
    finally:
        print('Proceso de inscripción finalizado.')


# ingresando participante con los siguientes datos
# 20 años y 6 de experencias
# 16 años y 10 de experencias


validar_inscripcion(20,6)
validar_inscripcion(16,10)

