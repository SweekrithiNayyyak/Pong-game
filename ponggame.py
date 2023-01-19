import turtle
wn=turtle.Screen()
wn.title("Pong by Sweek")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

playerPaddle=turtle.Turtle()
playerPaddle.speed(0)
playerPaddle.shape("square")
playerPaddle.shapesize(stretch_wid=5,stretch_len=1)
playerPaddle.color("white")
playerPaddle.penup()
playerPaddle.goto(-350,100)

computerPaddle=turtle.Turtle()
computerPaddle.speed(0)
computerPaddle.shape("square")
computerPaddle.shapesize(stretch_wid=5,stretch_len=1)
computerPaddle.color("white")
computerPaddle.penup()
computerPaddle.goto(350,100)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
ball.color("white")
ball.penup()
ball.goto(0,0)

while True:
    wn.update()

turtle.done()