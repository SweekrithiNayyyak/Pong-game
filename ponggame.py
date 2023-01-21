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

def moveball():
    ball.dx=3
    ball.dy=3
    pen2.clear()
    
wn=turtle.Screen()
wn.title("Pong by Sweek")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

playerScore=0
computerScore=0
gameState="start"

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
ball.dx=0
ball.dy=0

#scoring board
pen=turtle.Turtle()
pen.speed(0.5)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#pen.write("player : 0   computer:0", align="center",font=("Courier",24,"normal"))


pen2=turtle.Turtle()
pen.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
pen2.write("Press space to start",align="center",font=("Courier",20,"normal"))
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
    # if gameState=="start":
    #     ball.dx=0
    #     ball.dy=0
    #     ball.goto(0,0)
        
    if gameState=="start":
        wn.onkeypress(moveball,"space")
        gameState="play"
        
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    pen.write(f"player : {playerScore}   computer:{computerScore}", align="center",font=("Courier",24,"normal"))
    
    if ball.xcor()>380 and gameState=="play":
        ball.goto(0,0)
        ball.dx=0
        ball.dy=0
        gameState="start"
        playerScore+=1
        pen.clear()
    
    if ball.xcor()<-380 and gameState=="play":
        ball.goto(0,0)
        ball.dx=0
        ball.dy=0
        gameState="start"
        computerScore+=1
        pen.clear()
    
    #computerPaddle.sety(ball.ycor())
    
    if computerScore==2 or playerScore==2:
        gameState="end"
        ball.hideturtle()
        pen2.clear()
        if computerScore>playerScore:
            pen2.write("Computer won",align="center",font=("Courier",24,"normal"))
        else:
            pen2.write("player won")
    
    #paddle and ball collisions
    if ball.xcor()>340 and ball.ycor()<computerPaddle.ycor()+50 and ball.ycor() > computerPaddle.ycor()-50:
        ball.dx*=-1
    
    if ball.xcor()<-340 and ball.ycor()<playerPaddle.ycor()+50 and ball.ycor()>playerPaddle.ycor()-50:
        ball.dx*=-1
    
    



turtle.done()