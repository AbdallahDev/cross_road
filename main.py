import time
import turtle

from global_constants import TRACER_DEFAULT_VALUE, KEYS, SLEEP_TIME, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
turtle.tracer(TRACER_DEFAULT_VALUE)

player = Player()

turtle.listen()
turtle.onkeypress(fun=player.go_up, key=KEYS['up'])
turtle.onkeypress(fun=player.go_down, key=KEYS['down'])
turtle.onkeypress(fun=player.go_right, key=KEYS['right'])
turtle.onkeypress(fun=player.go_left, key=KEYS['left'])

game_on = True
while game_on:
    turtle.update()
    time.sleep(SLEEP_TIME)

turtle.mainloop()
