import turtle
wn=turtle.Screen()
wn.title("Pong by Sweek")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

playerPaddle=turtle.Turtle()
playerPaddle.speed(0)
playerPaddle.shape("square")
playerPaddle.color("white")
playerPaddle.penup()
playerPaddle.goto(-350,0)

while True:
    wn.update()