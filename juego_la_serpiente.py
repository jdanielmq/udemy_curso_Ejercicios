import turtle
import time
import random

class SnakeGame:
    def __init__(self, width=600, height=600, color='green'):
        """ inicializa los componentes del juego
        """
        # inicializan el lienzo de la pantalla
        self._ancho = width
        self._alto = height
        self.screen = turtle.Screen()
        self.screen.bgcolor(color)
        self.screen.setup(width,height)
        self.screen.title("Juego Snake")
        self.screen.tracer(0) # evita que se actualice automaticamente

        # inicializa la serpiente
        self.snake = turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape('square')
        self.snake.color('black')
        self.snake.penup()
        self.snake.goto(0,0)

        #inicializar el texto que se muestra en la pantalla
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.shape('square')
        self.texto.color('white')
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(0, (height / 2) - 40)
        self.texto.write('Puntos: 0 Record: 0', align='center', font=('Courier', 24, 'normal'))

        #inicializa la comida de la serpiente
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape('circle')
        self.comida.color('red')
        self.comida.penup()
        self.comida.goto(0, 100)

        # atributos de la clase
        self._direccion = None
        self._delay = 0.1
        self._score = 0
        self._high_score = 0
        self.shake_cuerpo = []

        # asociacion de los movientos y teclas
        self.screen.listen()
        self.screen.onkeypress(self.arriba, 'w')
        self.screen.onkeypress(self.abajo, 's')
        self.screen.onkeypress(self.izquierda, 'a')
        self.screen.onkeypress(self.derecha, 'd')

        #sacamos el texto por pantalla
        self._print_score()

    def arriba(self):
        """ Este metodo define el movimiento hacia arriba de la serpiente"""
        if self._direccion != 'abajo':
            self._direccion = 'arriba'

    def abajo(self):
        if self._direccion != 'arriba':
            self._direccion = 'abajo'

    def izquierda(self):
        if self._direccion != 'derecha':
            self._direccion = 'izquierda'

    def derecha(self):
        if self._direccion != 'izquierda':
            self._direccion = 'derecha'

    def mover(self):
        # Obtener las coordenadas de la cabeza de la serpiente
        hx, hy = self.snake.xcor(), self.snake.ycor()

        # movemos el cuerpo de la serpiente
        for i in range(len(self.shake_cuerpo) - 1, 0, -1):
            x = self.shake_cuerpo[i -1].xcor()
            y = self.shake_cuerpo[i - 1].ycor()
            self.shake_cuerpo[i].goto(x, y)

        # mover el segmento mas cercano a la cabeza
        if len(self.shake_cuerpo) > 0:
            self.shake_cuerpo[0].goto(hx, hy)

        if self._direccion == 'arriba':
            self.snake.sety(hy + 20)
        elif self._direccion == 'abajo':
            self.snake.sety(hy - 20)
        elif self._direccion == 'izquierda':
            self.snake.setx(hx - 20)
        elif self._direccion == 'derecha':
            self.snake.setx(hx + 20)

    def jugar(self):
        while True:
            self.screen.update()
            self.colision_borde()
            self.colision_comida()
            time.sleep(self._delay)
            self.mover()
        self.screen.mainloop()

    def colision_borde(self):
        bxcor = (self._ancho // 2) - 10
        bycor = (self._alto // 2) - 10

        if self.snake.xcor() > bxcor or self.snake.xcor() < -bxcor or self.snake.ycor() > bycor or self.snake.ycor() < -bycor:
            time.sleep(1)
            self.snake.goto(0, 0)
            self._direccion = None
            for s in self.shake_cuerpo:
                s.ht() # oculta el segmento

            self.shake_cuerpo.clear()

            #se reinicia el delay
            self._delay = 0.1
            # se reinicia el score
            if self._score > self._high_score:
                self._high_score = self._score
            self._score = 0
            self._print_score()

    def colision_comida(self):
        if self.snake.distance(self.comida) < 20:
            # mover la comida a un lugar aletorio
            bxcor = (self._ancho // 2) - 10
            bycor = (self._alto // 2) - 10
            x = random.randint(-bxcor, bxcor)
            y = random.randint(-bycor, bycor)
            self.comida.goto(x, y)
            #incremenmtarb cuerpo de la serpiente
            self.incrementar_cuerpo()
            # reducir el delay
            self._delay -= 0.001
            # aumentar el score
            self._score += 10
            self._print_score()

    def incrementar_cuerpo(self):
        segmento = turtle.Turtle()
        segmento.speed(0)
        segmento.shape('square')
        segmento.color('grey')
        segmento.penup()
        self.shake_cuerpo.append(segmento)


    def _print_score(self):
        self.texto.clear()
        self.texto.write('Puntos: {} Record: {}'.format(self._score, self._high_score), align='center', font=('Courier', 24, 'normal'))



juego_snake = SnakeGame()
juego_snake.jugar()

