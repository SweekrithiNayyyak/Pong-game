import turtle

def playerpaddleup():
    #stores current value of y cordinate into a variable
    y=playerPaddle.ycor()
    y+=40
    playerPaddle.sety(y)

def playerpaddledown():
    #stores current value of y cordinate into a variable
    y=playerPaddle.ycor()
    y-=40
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
ball.speed(2)
ball.shape("square")
ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=-2

#to detect keypress on the window
wn.listen()
wn.onkeypress(playerpaddleup,"w")
wn.onkeypress(playerpaddledown,"x")
wn.onkeypress(computerpaddleup,"Up")
wn.onkeypress(computerpaddledown,"Down")

while True:
    wn.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.setx(0)
        ball.sety(0)
    
    #computerPaddle.sety(ball.ycor())
    
    
    
    #paddle and ball collisions
    if ball.xcor()>340 and ball.ycor()<computerPaddle.ycor()+50 and ball.ycor() > computerPaddle.ycor()-50:
        ball.dx*=-1
    
    if ball.xcor()<-340 and ball.ycor()<playerPaddle.ycor()+50 and ball.ycor()>playerPaddle.ycor()-50:
        ball.dx*=-1
    
    



turtle.done()