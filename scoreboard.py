from turtle import Turtle

#Constants
PLAYER_SCOREBOARD = (-300, 245)
COMPUTER_SCOREBOARD = (300, 245)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
LINES = (0 , -400)


#Draw two Scoreboards
class Scoreboard(Turtle):

    def __init__(self, player):
        super().__init__()
        if player == 'playerOne':
            self.goto(PLAYER_SCOREBOARD)
        else:
            self.goto(COMPUTER_SCOREBOARD)
        self.score = 0
        self.color("White")
        self.updateScoreboard()
        self.hideturtle()

    #Update scoreboard
    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    #Increase the score after each win
    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()


#Draw the lines for the pong game
class DrawLines(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.width(1)
        self.goto(LINES)
        self.color('white')
        self.setheading(90)
        self.hideturtle()
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
