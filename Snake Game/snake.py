from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.highscore = 0
        self.create_snake()
        self.head = self.snakes[0]
        self.move()

    # Snake Object Creation and addition to the list
    def create_snake(self):
        for num in POSITIONS:
            self.add_num(num)

    def add_num(self, num):
        snake = Turtle(shape="square")
        snake.color('white')
        snake.penup()
        snake.goto(num)
        self.snakes.append(snake)

    # Adding snake segment at end of the snake list
    def extend(self):
        self.add_num(self.snakes[-1].position())

    # Moving snake's each segment to second last position of the snake body to move forward
    def move(self):
        for each_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[each_num - 1].xcor()
            new_y = self.snakes[each_num - 1].ycor()
            self.snakes[each_num].goto(new_x, new_y)
        self.snakes[0].forward(20)

    # Snake Control Logic
    def up(self):
        if self.head.heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].setheading(RIGHT)
