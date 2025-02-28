from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
scoreboard=Scoreboard()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("My ping pong game")
screen.tracer(0)
ball=Ball()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))





screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50 :
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    if scoreboard.l_score >9 or scoreboard.r_score >9:
        game_is_on=False
        scoreboard.mention()


screen.exitonclick()