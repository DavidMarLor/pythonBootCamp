from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_mode = 10
        self.y_mode = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_mode
        new_y = self.ycor() + self.y_mode
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mode *= -1

    def bounce_x(self):
        self.x_mode *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()