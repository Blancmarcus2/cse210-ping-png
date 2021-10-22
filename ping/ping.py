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
