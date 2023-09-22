from turtle import Turtle,Screen
from padel import Padel
from ball import Ball
from score_table import Score
import time

# Create the game screen.
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=700)
screen.title('PONG GAME')
screen.tracer(0)

# Draw the center line.
line = Turtle()
line.goto(0, 350)
line.setheading(270)
line.width(2)
line.hideturtle()
line.color('white')
line.speed(0)
for _ in range(22):
    line.penup()
    line.forward(15)
    line.pendown()
    line.forward(15)

# Create the paddles and the ball.
r_padel = Padel((570, 0))
l_padel = Padel((-570, 0))
ball = Ball()

# Create the score table.
score = Score()

# Register the key bindings for moving the paddles.
screen.listen()
screen.onkey(key='Up', fun=r_padel.move_up)
screen.onkey(key='Down', fun=r_padel.move_down)
screen.onkey(key='w', fun=l_padel.move_up)
screen.onkey(key='s', fun=l_padel.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    ball.check_screen()
    if ball.distance(r_padel) < 70 and ball.xcor() > +550 or  ball.distance(l_padel) < 70 and ball.xcor() > -550:
        ball.move_after_hit()
        ball.move_speed *= 0.9
        if ball.move_speed < 0:
            ball.move_speed = 0


    if ball.xcor()>580:
        score.score_update_l()
        ball.reset_ball()
    elif ball.xcor() < -580:
        score.score_update_r()
        ball.reset_ball()





screen.exitonclick()