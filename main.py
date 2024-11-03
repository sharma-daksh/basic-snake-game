from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen
screen=Screen()
screen.setup(600,600) #(width,height)
screen.bgcolor("darkblue")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

# key presses to control the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

# start the game loop
game_on=True
while game_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
            game_on = False
            scoreboard.game_over()

    # detect collision with snake's own body
    for body_parts in snake.body_parts[1:]:
         if snake.head.distance(body_parts)<10:
              game_on=False
              scoreboard.game_over()



screen.exitonclick()
