from turtle import Turtle

FONT = ('Arial', 32, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()

        # Set the score's initial position and color.
        self.goto(0, 300)
        self.color('white')

        # Hide the turtle cursor.
        self.hideturtle()

        # Initialize the scores.
        self.score_l = 0
        self.score_r = 0

        # Write the initial scores to the screen.
        self.make_write()

    def make_write(self):
        # Clear the screen.
        self.clear()

        # Write the scores to the screen.
        self.write(align='center', arg=f'{self.score_l}     {self.score_r}', font=FONT)

    def score_update_r(self):
        # Increment the right player's score.
        self.score_r += 1

        # Update the score on the screen.
        self.make_write()

    def score_update_l(self):
        # Increment the left player's score.
        self.score_l += 1

        # Update the score on the screen.
        self.make_write()