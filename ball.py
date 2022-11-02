from turtle import Turtle

#Create the ball that will be used
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(40)
        self.moveSpeed = 0.1
        self.penup()
        self.xMove = 10
        self.yMove = 10



    #Moves the ball by getting a new x and y coordinate
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    #Bounce and hit will detect a collision with the wall or paddle
    #It will reverse the direction by mulitplying by -1
    def bounce(self):
        self.yMove *= -1

    def hit(self):
        self.moveSpeed *= 0.9
        self.xMove *= -1

    #Resets the position and changes direction of the ball after a score
    def resetPosition(self):
        self.goto(0,0)
        self.moveSpeed = 0.1
        self.hit()