# import colorgram
#
# image = "image.jpeg"
# colors = colorgram.extract(image, 30)
#
# color_list = []
#
# for n in range(len(colors)):
#     n_color = colors[n]
#     rgb = n_color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     truble = (r,g,b)
#     color_list.append(truble)

import turtle as t
import random

color_list = [(217, 230, 241), (222, 240, 231), (121, 177, 207), (223, 156, 89), (210, 130, 165), (190, 172, 22), (233, 206, 100), (37, 114, 162), (167, 16, 49), (212, 77, 114), (31, 140, 79), (197, 67, 30), (18, 170, 204), (26, 179, 143), (163, 57, 96), (239, 161, 189), (230, 78, 52), (138, 188, 167), (15, 29, 75), (64, 18, 44), (133, 211, 230), (70, 25, 17), (28, 47, 129), (162, 20, 13), (102, 117, 178), (150, 213, 189), (244, 163, 154), (172, 185, 223)]

turtle = t.Turtle()
turtle.hideturtle()
turtle.speed(0)
t.colormode(255)

# Starting position:
turtle.penup()
turtle.goto(-300, 300)
turtle.penup()


def draw_dots():
    for _ in range(9):
        color = random.choice(color_list)
        turtle.dot(5, color)
        if _ == 8:
            pass
        else:
            turtle.fd(60)

for _ in range(5):
    draw_dots()
    turtle.right(90)
    turtle.fd(59)
    turtle.right(90)
    draw_dots()
    turtle.left(90)
    turtle.fd(59)
    turtle.left(90)


screen = t.Screen()
screen.colormode(255)
screen.screensize(600,600)
screen.exitonclick()
