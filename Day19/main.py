from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():

    tim.forward(10)

def move_backwards():

    tim.backward(10)


def turn_right():

    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():

    new_heading_2 = tim.heading() + 10
    tim.setheading(new_heading_2)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()



