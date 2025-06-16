
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import Score
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_starts = True

while game_starts:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment()

    # Increase snake speed
    # if score.score == 10:
    #     snake.speed()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snake()

    # Detect collision with self
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 8:
            score.reset()
            snake.reset_snake()


screen.exitonclick()
