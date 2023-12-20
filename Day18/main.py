import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color =  (r, g, b)
    return color



tim.speed("fastest")
for i in range(1, 361):
    tim.circle(100)
    tim.setheading(i)
    tim.color(random_color())




# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()







screen = t.Screen()
screen.exitonclick()