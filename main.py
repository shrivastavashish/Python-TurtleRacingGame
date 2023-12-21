import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Your Bet", prompt="Choose Your turtle? For that Enter Your Color: ")
color = ["red", "blue", "green", "orange", "magenta"]
y_position = [-70, -40, -10, 20, 50]
all_turtle = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on= True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON the RACE! The {winning_color} turtle is the WINNER!")
            else:
                print(f"Yoy've LOST the RACE! The {winning_color} turtle is the WINNER")
        random_distance= random.randint(0, 10)
        turtle.forward((random_distance))










screen.exitonclick()
