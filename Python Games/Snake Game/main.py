# Modules and Class import
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# Screen object setup
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('Snake Game')
my_screen.tracer(0)

# Object Initialization
snake = Snake()
food = Food()
score = Score()

# Snake Controls on Screen
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

# Main Logic
game = True
while game:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Randomizing Food every time snake eats and increasing snake size
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.extend()

    # Collision with WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

    # Collision with Tail
    for num in snake.snakes[1:]:
        if snake.head.distance(num) < 10:
            game = False
            score.game_over()

my_screen.exitonclick()
