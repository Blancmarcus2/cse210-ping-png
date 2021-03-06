""" Documentation checker

A command-line tool for checking source code documentation requirements.

Authors:
  - Ogunniyi Owamamwen
  - Marcus Blanc
  -
"""

import turtle as cse
import os


def get_ping():
    player_score_a = 0
    player_score_b = 0

    pong = cse.Screen()    # Window
    pong.title("Team9 Ping Pong")  # Name of the game header.
    pong.bgcolor('black')    # Backgroung color
    pong.setup(width=800, height=600)  # Size of the game panel
    pong.tracer(0)   # Speed up's the game.

    # Left paddle for the game

    paddle_left = cse.Turtle()
    paddle_left.speed(0)
    paddle_left.shape('square')
    paddle_left.color('blue')
    paddle_left.shapesize(stretch_wid=5, stretch_len=1)
    paddle_left.penup()
    paddle_left.goto(-350, 0)

    # Right paddle for the game

    paddle_right = cse.Turtle()
    paddle_right.speed(0)
    paddle_right.shape('square')
    paddle_right.shapesize(stretch_wid=5, stretch_len=1)
    paddle_right.color('yellow')
    paddle_right.penup()
    paddle_right.goto(350, 0)

    # Creating a pong ball for the game

    ball = cse.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.goto(0, 0)
    ball_dx = 1.5   # Setting up the pixels for the ball movement.
    ball_dy = 1.5

    # Creating a pen for updating the Score

    pen = cse.Turtle()
    pen.speed(0)
    pen.color('skyblue')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0                    Player B: 0 ",
              align="center", font=('Monaco', 25, "normal"))

    # Left Paddle moving using the keyboard

    def paddle_left_up():
        y = paddle_left.ycor()
        y = y + 15
        paddle_left.sety(y)

    # Moving the left paddle down

    def paddle_left_down():
        y = paddle_left.ycor()
        y = y - 15
        paddle_left.sety(y)

    # Moving the right paddle up

    def paddle_right_up():
        y = paddle_right.ycor()
        y = y + 15
        paddle_right.sety(y)

    # Moving right paddle down

    def paddle_right_down():
        y = paddle_right.ycor()
        y = y - 15
        paddle_right.sety(y)

    # Keyboard binding

    pong.listen()
    pong.onkeypress(paddle_left_up, "u")
    pong.onkeypress(paddle_left_down, "e")
    pong.onkeypress(paddle_right_up, "Up")
    pong.onkeypress(paddle_right_down, "Down")


# Main Game Loop

    while True:
        pong.update()  # This methods is mandatory to run any game

        # Moving the ball
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        # setting up the border

        if ball.ycor() > 290:   # Right top paddle Border
            ball.sety(290)
            ball_dy = ball_dy * -1

        if ball.ycor() < -290:  # Left top paddle Border
            ball.sety(-290)
            ball_dy = ball_dy * -1

        if ball.xcor() > 390:   # right width paddle Border
            ball.goto(0, 0)
            ball_dx = ball_dx * -1
            player_score_a = player_score_a + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(
                player_score_a, player_score_b), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay ping/wallhit.wav&")

        if(ball.xcor()) < -390:  # Left width paddle Border
            ball.goto(0, 0)
            ball_dx = ball_dx * -1
            player_score_b = player_score_b + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(
                player_score_a, player_score_b), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay ping/wallhit.wav&")

        # Handling the collisions with paddles.

        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
            ball.setx(340)
            ball_dx = ball_dx * -1
            os.system("afplay ping/paddle.wav&")

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
            ball.setx(-340)
            ball_dx = ball_dx * -1
            os.system("afplay ping/paddle.wav&")
