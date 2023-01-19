import turtle

def playerpaddleup():
    #stores current value of y cordinate into a variable
    y=playerPaddle.ycor()
    y+=20
    playerPaddle.sety(y)

def playerpaddledown():
    #stores current value of y cordinate into a variable
    y=playerPaddle.ycor()
    y-=20
    playerPaddle.sety(y)
    
def computerpaddleup():
    #stores current value of y cordinate into a variable
    y=computerPaddle.ycor()
    y+=20
    computerPaddle.sety(y)

def computerpaddledown():
    #stores current value of y cordinate into a variable
    y=computerPaddle.ycor()
    y-=20
    computerPaddle.sety(y)

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

#to detect keypress on the window
wn.listen()
wn.onkeypress(playerpaddleup,"w")
wn.onkeypress(playerpaddledown,"x")
wn.onkeypress(computerpaddleup,"Up")
wn.onkeypress(computerpaddledown,"Down")

while True:
    wn.update()



turtle.done()