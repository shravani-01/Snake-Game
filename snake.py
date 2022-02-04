from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for p in STARTING_POSITIONS:
            self.add_segment(p)

    def add_segment(self, p):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(p)
        self.segment_list.append(segment)


    def extend(self):
        self.add_segment(self.segment_list[-1].position())


    def move(self):
        for s in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[s - 1].xcor()
            new_y = self.segment_list[s - 1].ycor()
            self.segment_list[s].goto(new_x, new_y)
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
