
from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """Initializing snake body structure here."""
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Creating snake body structure here."""
        for position in SNAKE_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        """Adding snake body structure here."""
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        """Increase snake body structure here."""
        self.add_snake(self.snake_body[-1].position())

    def reset_snake(self):
        """Returning snake structure to starting stage."""
        for snake in self.snake_body:
            snake.goto(10000, 10000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def snake_move(self):
        """Moves snake to the next position."""
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_num - 1].xcor()
            new_y = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def speed(self):
        self.head.forward(MOVE_SPEED + 10)

    def up(self):
        """Moves snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
