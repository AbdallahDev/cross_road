import turtle
from turtle import Turtle

turtle.addshape("chicken.gif")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('chicken.gif')
