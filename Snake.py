from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.CreateSnake()
        self.segments[0].color("red")
        self.CurrentDirection = ""

    def CreateSnake(self):
        for position in STARTING_POSITIONS:
            self.add_object(position)

    def add_object(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def tail(self):
        self.add_object(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(SPEED)

    def up(self):
        if self.CurrentDirection != "DOWN":
            self.segments[0].setheading(90)
            self.CurrentDirection = "UP"

    def down(self):
        if self.CurrentDirection != "UP":
            self.segments[0].setheading(270)
            self.CurrentDirection = "DOWN"

    def right(self):
        if self.CurrentDirection != "LEFT":
            self.segments[0].setheading(360)
            self.CurrentDirection = "RIGHT"

    def left(self):
        if self.CurrentDirection != "RIGHT":
            self.segments[0].setheading(180)
            self.CurrentDirection = "LEFT"
