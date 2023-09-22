from turtle import Turtle

# This is the speed at which the paddles can move.
PADDLE_MOVEMENT_SPEED = 20

class Padel(Turtle):
    # This is the constructor for the Padel class.
    def __init__(self, pos):
        super().__init__()

        # Set the paddle's shape, size, and color.
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.color('white')
        self.penup()

        # Go to the specified position.
        self.goto(pos)

    # This method moves the paddle up.
    def move_up(self):
        new = self.ycor() + PADDLE_MOVEMENT_SPEED
        self.goto(self.xcor(), new)

    # This method moves the paddle down.
    def move_down(self):
        new = self.ycor() - PADDLE_MOVEMENT_SPEED
        self.goto(self.xcor(), new)