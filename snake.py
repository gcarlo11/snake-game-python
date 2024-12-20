from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = [(0, 0), (-20, 0), (-40, 0)]
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]
        self.last_segment = self.all_segments[len(self.all_segments) - 1]

    def create_snake(self):
        for position in self.snake_body:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def reset(self):
        for segment in self.all_segments:
            segment.goto(1000,1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for segment_num in range(len(self.all_segments) - 1, 0, -1):
            x_cor = self.all_segments[segment_num - 1].xcor()
            y_cor = self.all_segments[segment_num - 1].ycor()
            self.all_segments[segment_num].goto(x_cor, y_cor)
        self.all_segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
