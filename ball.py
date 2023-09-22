from turtle import Turtle
MOVE_YCOR = 10
class Ball(Turtle):
    # This is the constructor for the Ball class.
    def __init__(self):
        super().__init__()

        # Set the ball's shape, size, and color.
        self.shape('circle')
        self.color('white')
        self.penup()

        # Set the ball's initial movement speed.
        self.move_ycor = 10
        self.move_xcor = 10
        self.move_speed = 0.1

    # This method moves the ball.
    def move_ball(self):
        x = self.xcor() + self.move_xcor
        y = self.ycor() + self.move_ycor
        self.goto(x, y)

    # This method checks if the ball has collided with a paddle or the screen.
    def check_collision(self, paddle):
        if self.distance(paddle) < 70:
            self.move_after_hit()
            self.move_speed *= 0.9
            if self.move_speed < 0:
                self.move_speed = 0

    # This method checks if the ball has hit the top or bottom of the screen.
    def check_screen(self):
        if self.ycor() > 330 or self.ycor() < -330:
            self.move_ycor *= -1

    # This method reverses the ball's horizontal movement direction.
    def move_after_hit(self):
        self.move_xcor *= -1

    # This method resets the ball to its initial position.
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
