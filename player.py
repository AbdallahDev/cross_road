import turtle
from turtle import Turtle

from global_constants import PLAYER_STEPS, PLAYER_SHAPE1, HEADINGS, PLAYER_DEFAULT_POSITION

turtle.addshape(PLAYER_SHAPE1)


class Player(Turtle):
    """Represents the player"""""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(PLAYER_SHAPE1)
        self.goto(PLAYER_DEFAULT_POSITION)
        self.steps = PLAYER_STEPS

    def go_up(self):
        """moves the player up"""""
        self.move(heading=HEADINGS['up'])

    def go_down(self):
        """moves the player down"""""
        self.move(heading=HEADINGS['down'])

    def go_right(self):
        """moves the player right"""""
        self.move(heading=HEADINGS['right'])

    def go_left(self):
        """moves the player left"""""
        self.move(heading=HEADINGS['left'])

    def move(self, heading):
        """moves the player to a specified direction"""""
        self.seth(heading)
        self.forward(self.steps)
