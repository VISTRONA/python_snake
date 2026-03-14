from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()

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




# tim.shapesize(20,20)




screen.exitonclick()


#Current issues:
# 1. Response time of snake turning is too long