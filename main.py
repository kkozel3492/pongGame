from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard, DrawLines
import time
from ball import Ball

#Create the Screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)


#Creates the players, balls, line, and scoreboards
playerOne = Paddle('playerOne')
playerTwo = Paddle('PlayerOne')
ball = Ball()
playerOneScore = Scoreboard('playerOne')
playerTwoScore = Scoreboard('playerTwo')
lines = DrawLines()

#Set the sleep time
screen.update()
time.sleep(.1)


#Play the game
gameIsOn = True
while gameIsOn:
    time.sleep(ball.moveSpeed)
    ball.move()
    screen.listen()
    screen.onkey(playerOne.moveUp, "w")
    screen.onkey(playerOne.moveDown, "s")
    screen.onkey(playerTwo.moveUp, "Up")
    screen.onkey(playerTwo.moveDown, "Down")
    screen.update()

    #Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Add Score
    if ball.xcor() > 380:
        playerOneScore.increaseScore()
        ball.resetPosition()
    if ball.xcor() < -380:
        playerTwoScore.increaseScore()
        ball.resetPosition()

    #hit paddle
    if ball.distance(playerOne) < 40 and ball.xcor() < -320 or ball.distance(playerTwo) < 40 and ball.xcor() > 320:
        ball.hit()

screen.exitonclick()