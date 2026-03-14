from turtle import Turtle,Screen
from snake import Snake
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()

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




# tim.shapesize(20,20)




screen.exitonclick()