
from turtle import Turtle,Screen

from orca.flat_review import Line

from snake import Snake
import time
from food import Food
from score_board import *



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
food.refresh()
score = scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.update()
# i=0
game = True
while game:


    screen.update()

    time.sleep(0.1)
    snake.move()

    # Detect if snake eat food
    if snake.head.distance(food) < 15:
        print("Nom Nom")
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 275 or snake.head.ycor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() < -275 :
        score.goto(0, 0)
        score.game_over()
        game = False



# tim.shapesize(20,20)




screen.exitonclick()


#Current issues:
# 1. Response time of snake turning is too long
# 2. Draw Borderds
# 3. Add way so that if snake touches wall it teleports