path_archivo = 'agendaDigital'
agenda_digital = {
    # primer contacto de la agenda
    'Juan Daniel' : {
        "direccion" : 'Carlos dittborn 500',
        'email' : 'jdannymq@gmail.com',
        "telefono" : '1234567890'
    },
    'Francisco Adrian' : {
        "direccion": 'vicuña mackenna 1575',
        'email': 'francisco@gmail.com',
        "telefono": '0987654321'
    }
}

def escribir_agenda(nombre_agenda, agenda_digital):
    """ Escribir la agenda en un fichero de texto
        Parametros posicionales
        nombre_agenda = str que representa el nombre de la agenda en disco
        agenda_digital = disccionario que representa la agenda digital y contactos
    """
    agenda_fichero = open(nombre_agenda,'w')
    agenda_fichero.write(str(agenda_digital))
    agenda_fichero.close()

def leer_agenda(nombre_agenda):
    agenda_fichero = open(nombre_agenda,'r')
    agenda_fichero_data = agenda_fichero.readlines()
    agenda_fichero.close()
    return eval(agenda_fichero_data[0])

def solicitar_contacto_agenda():
    """ Esta función es para solicitar los nuevos usuarios para la agenda"""
    nombre = input('Introducce el nombre: ')
    direccion = input('Introducce el dirección: ')
    correo = input('Introducce el correo: ')
    telefono = input('Introducce el telefono: ')
    # construccion de diccionario
    contacto = {
        'nombre': nombre,
        'direccion' : direccion,
        'email': correo,
        'telefono': telefono
    }
    return contacto

def crear_contacto(agenda_digital, nuevo_contacto):
    """ introduce un nuevo contacto agregado por el usuario"""
    agenda_digital[nuevo_contacto['nombre']] = {
        'direccion' :  nuevo_contacto['direccion'],
        'email' : nuevo_contacto['email'],
        'telefono' : nuevo_contacto['telefono']
    }
    escribir_agenda(path_archivo, agenda_digital)
    return agenda_digital

def consultar_contacto_agenda(agenda_digital):
    """esta funcion consultar un registro de la agenda digital almacenada en el disco"""
    nombre = input('Ingresa el nombre a buscar: ')
    print('\n[+]', nombre)
    print('\tDirección: ',agenda_digital[nombre]['direccion'])
    print('\tEmal: ',agenda_digital[nombre]['email'])
    print('\tTelefono: ',agenda_digital[nombre]['telefono'])



opcion = input('Sr usuario seleccione la opcion ingresar un registro [I] o consultar un registro [C] :')
if opcion == 'I' or opcion == 'i':
    print('\n')
    agenda_digital = leer_agenda(path_archivo)
    nuevo_contacto = solicitar_contacto_agenda()
    agenda_digital = crear_contacto(agenda_digital, nuevo_contacto)
    escribir_agenda(path_archivo, agenda_digital)
else:
    print('\n')
    agenda_digital = leer_agenda(path_archivo)
    consultar_contacto_agenda(agenda_digital)


