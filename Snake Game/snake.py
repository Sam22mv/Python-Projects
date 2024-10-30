from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP  = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
            self.timm = []
            self.create_snake()
            self.head = self.timm[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_tim(position)

    def add_tim(self,position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.timm.append(tim)

    def reset(self):
        for t in self.timm:
            t.goto(1000,1000)
        self.timm.clear()
        self.create_snake()
        self.head = self.timm[0]

    def extend(self):
        self.add_tim(self.timm[-1].position())

    def move(self):
        for tim_num in range(len(self.timm) - 1, 0, -1):
            new_x = self.timm[tim_num - 1].xcor()
            new_y = self.timm[tim_num - 1].ycor()
            self.timm[tim_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
