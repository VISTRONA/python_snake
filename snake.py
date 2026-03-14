from turtle import Turtle, Screen
import time

Up = 90
Down = 270
Left = 180
Right = 00

starting_position = [(00, 00), (-20, 00), (-40, 0)]
move = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.length = len(self.segments)
        self.head = self.segments[0]


    def create_snake(self):
        for position in starting_position:
            self.extend_snake(position)


    def extend(self):
        self.extend_snake(self.segments[-1].position())


    def extend_snake(self,position):
        snake_block = (Turtle())
        snake_block.color("white")
        snake_block.penup()
        snake_block.shape("square")
        snake_block.goto(position)

        self.segments.append(snake_block)



    def move(self):

        for block_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[block_num - 1].xcor()
            new_y = self.segments[block_num - 1].ycor()
            self.segments[block_num].goto(new_x, new_y)

        self.head.forward(move)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)


