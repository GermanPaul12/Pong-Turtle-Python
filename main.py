from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(1440, 900)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((680, 0))
left_paddle = Paddle((-680, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

t = Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(0, 450)
t.setheading(270)
t.pencolor('white')
for i in range(9):
    t.pendown()
    t.forward(50)
    t.penup()
    t.forward(50)




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall 
    if ball.ycor() < -355 or 360 < ball.ycor():
        #ball should bounce
        ball.bounce_y()
    #detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 650:
        ball.bounce_x()
        
    if ball.distance(left_paddle) < 50 and ball.xcor() < -650:
        ball.bounce_x()  
    
    if ball.xcor() > 700:
        ball.reset_position()   
        scoreboard.l_point()
        
    if ball.xcor() < -700:
        ball.reset_position()   
        scoreboard.r_point()        
    

screen.exitonclick()