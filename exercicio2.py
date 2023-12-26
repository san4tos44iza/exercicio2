from turtle import Turtle,onscreenclick, onkey, listen, Screen
turtle = Turtle ()
tela = Screen()
turtle.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2

def jogar(x, y):
    turtle.penup()
    turtle.goto(x, y)
    if resultado == 0:
       circulo()

r = 10

def circulo():
    turtle.color('blue')
    turtle.right(90)
    turtle.forward(45)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(r)

def up():
    global r 
    r = r + 5

tela.onscreenclick(jogar)
onkey(up,'Up')
listen()

listen (xdummy=None, ydummy=None)
tela.mainloop()