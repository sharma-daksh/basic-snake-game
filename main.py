from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600) #(w,h)
screen.bgcolor("darkblue")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on=True
while game_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
            scoreboard.reset()
            snake.reset()
    for body_parts in snake.body_parts[1:]:
         if snake.head.distance(body_parts)<10:
              scoreboard.reset()
              snake.reset()


screen.exitonclick()
