from turtle import Turtle

# Starting point for players
PLAYER_START = (-350, 0)
PLAYER_TWO_START = (350, 0)


class Paddle(Turtle):

    # Creates the paddle, takes argument to decide if computer or player
    def movePaddle(self, player):
        if player == 'playerOne':
            for i in PLAYER_START:
                self.goto(PLAYER_START)
        else:
            for i in PLAYER_TWO_START:
                self.goto(PLAYER_TWO_START)

    def __init__(self, player):
        super().__init__()
        self.createPaddle()
        self.movePaddle(player)

    def createPaddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    #Movement of the paddles
    def moveUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def moveDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
