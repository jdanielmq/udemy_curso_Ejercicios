from IPython.display import clear_output

def crear_tablero(filas, columnas):
    tablero = [None] * filas
    for f in range(filas):
        tablero[f] = ['.'] * columnas

    return tablero

def muestra_tablero(tablero):
    for num in range(len(tablero[0])):
        print(num, end='  ')

    for fila in tablero:
        print("")
        for casilla in fila:
            print(casilla, end='  ')


def introducir_ficha(tablero, columna, color):
    if columna > len(tablero[0]) or  columna < 0:
        print('ERROR: Numero de columna esta fuera de rango')
        return
    elif tablero[0][columna] != '.':
        print('ERROR: Numero de columna esta ocupada con fichas')
        return
    else:
        for fila in range(len(tablero)-1,-1,-1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = color
                return tablero

def revisar_filas(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for r in range(num_filas):
       for c in range(num_columnas - 3):
           if tablero[r][c] == color and tablero[r][c + 1] == color and tablero[r][c + 2] == color and tablero[r][c + 3] == color:
               return True

def revisar_columnas(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas):
        for r in range(num_filas - 3):
            if tablero[r][c] == color and tablero[r + 1][c] == color and tablero[r + 2][c] == color and tablero[r + 3][c] == color:
                return True


def revisar_diagonal_derecha(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas - 3):
        for r in range(num_filas - 1, 2, -1):
            if tablero[r][c] == color and  tablero[r-1][c+1] == color and tablero[r-2][c+2] == color and tablero[r-3][c+3] == color:
                return True


def revisar_diagonal_izquierda(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas - 1,2,-1):
        for r in range(num_filas - 1, 2, -1):
            if tablero[r][c] == color and tablero[r-1][c-1] == color and tablero[r-2][c-2] == color and tablero[r-3][c-3] == color:
                return True


def comprobar_ganador(tablero, color):
    return (revisar_filas(tablero, color) or
            revisar_columnas(tablero, color) or
            revisar_diagonal_derecha(tablero, color) or
            revisar_diagonal_izquierda(tablero, color))



tablero = crear_tablero(6, 7)
turno = 'R'
sig_turno = 'A'
while True:
    turno = sig_turno
    muestra_tablero(tablero)
    if turno == 'R':
        columna = int(input('Turno del rojo: '))
        sig_turno = 'A'
    elif turno == 'A':
        columna = int(input('Turno del Amarillo: '))
        sig_turno = 'R'

    introducir_ficha(tablero, columna, turno)
    clear_output(wait=False)
    if comprobar_ganador(tablero, turno):
        print('Turno ganado ', turno, '\n\n')
        muestra_tablero(tablero)
        break



