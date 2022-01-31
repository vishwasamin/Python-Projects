from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Screen Setup
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title('Pong')
my_screen.tracer(0)

# Object Initialization
l_paddle = Paddle((-360, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

# Screen Control Setup
my_screen.listen()
my_screen.onkeypress(r_paddle.up, "Up")
my_screen.onkeypress(r_paddle.down, "Down")
my_screen.onkeypress(l_paddle.up, "w")
my_screen.onkeypress(l_paddle.down, "s")

# Main Logic
game = True
while game:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        score.update_score()

    # Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        score.update_score()

    # Updating Score for Left Player and Resetting the ball
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()

    # Updating Score for Right Player and Resetting the ball
    if ball.xcor() < -400:
        ball.reset()
        score.r_point()

my_screen.exitonclick()
