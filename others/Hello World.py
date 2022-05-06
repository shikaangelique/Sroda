import turtle

# sroda = input("what is your name? ")
# like = input("what do you like? ")

# ninja = turtle.Turtle()  # relevant
screen = turtle.Screen()  # relevant

# ninja.penup()
# ninja.goto(-150, -100)
#
# ninja.pendown()
# ninja.forward(300)
# ninja.left(90)
# ninja.forward(200)
# ninja.left(90)
# ninja.forward(300)
# ninja.left(90)
# ninja.forward(200)
#
# ninja.penup()
# ninja.goto(-25, 0)
#
# # text = sroda, " likes ", like
# text = "Hello World"
# ninja.write(text, font=("Calibri", 10, "bold"))
#
# ninja.penup()
# ninja.goto(-150, -100)
# ninja.ht()

color_one = 'red'
color_two = 'grey'
color_three = 'black'


#
# raddy = 150
# con_circles = turtle.Turtle()
#
# con_circles.speed(0)
# con_circles.pendown()
# con_circles.circle(raddy)
#
#
# for segment in range(36):
#     # ninja.left((360 / segment))
#     if segment % 2 == 0:
#         con_circles.fillcolor(color_one)
#     elif segment % 3 == 0:
#         con_circles.fillcolor(color_two)
#     else:
#         con_circles.fillcolor(color_three)
#     con_circles.begin_fill()
#     con_circles.left(10)
#     con_circles.circle(raddy)
#     con_circles.end_fill()
#
#
# con_circles.penup()
# con_circles.hideturtle()
# #
# tor = turtle.Turtle()
#
# for times in range(36):
#     tor.color("blue")
#     tor.speed(1000)
#     tor.circle(100)
#     tor.color("red")
#     tor.forward(200)
#     tor.left(120)
#     tor.color("orange")
#     tor.forward(100)
#     tor.right(120)
#     tor.left(170)
#     tor.left(20)
#     tor.forward(15)


# t.fillcolor(col)
# t.begin_fill()
# t.circle(r)
# t.end_fill()

def handle_color_change(x, y):
    global ninja_color
    global ninja_color_two
    global ninja_color_three
    print("yessir")
    ninja_color_two = ninja_color
    ninja_color_three = ninja_color

screen.exitonclick()
