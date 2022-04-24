from turtle import Turtle, Screen
from Snake import *
from Food import *
from Score import *
import time

# ------------------SCREEN SETUP---------------
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# ------------------SNAKE-OBJECT---------------
snake = Snake()
# -------------------FOOD-OBJECT------------------
food = Food()
# -------------------SCORE-OBJECT---------------------
score = Score()

# -------------------KEYBOARD ACCESS----------
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# -----------------------MAIN-----------------------
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()    # MOVING CONSTANTLY

    if snake.segments[0].distance(food) < 15:   # EATING FOOD
        food.Eaten()
        snake.tail()
        score.score_increament()

    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290) or \
            (snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290):    # FRAME-DEFINING
        game_is_on = False
        score.GameOver()

    for i in snake.segments:  # IF SNAKE ENCOUNTERS WITH ITS TAIL
        if i == snake.segments[0]:
            pass
        elif snake.segments[0].distance(i) < 10:
            game_is_on = False
            score.GameOver()

screen.exitonclick()
